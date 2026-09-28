# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import struct
import time
import unittest
from concurrent.futures import ThreadPoolExecutor
from contextlib import ExitStack
from dataclasses import replace
from threading import Barrier

from openenoc_iss import IssError, IssLibrary, RequestKind, ResponseStatus
from openenoc_iss import RunState

POLL_TIMEOUT_SECONDS = 2.0


class NativeApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])

    def wait_for_request(self, endpoint):
        deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            request = endpoint.poll()
            if request is not None:
                return request
            self.assertNotEqual(endpoint.state().run_state, RunState.ERROR)
            time.sleep(0)
        self.fail("timed out waiting for an ISS request")

    def wait_for_state(self, endpoint, expected):
        deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            state = endpoint.state()
            if state.run_state == expected:
                return state
            self.assertNotEqual(state.run_state, RunState.ERROR)
            time.sleep(0)
        self.fail(f"timed out waiting for ISS state {expected.name}")

    def wait_for_steps(self, endpoint, minimum):
        deadline = time.monotonic() + POLL_TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            state = endpoint.state()
            if state.step_count >= minimum:
                return state
            self.assertNotEqual(state.run_state, RunState.ERROR)
            time.sleep(0)
        self.fail(f"timed out waiting for {minimum} ISS steps")

    @staticmethod
    def mmio_program(value):
        return struct.pack(
            "<5I",
            0x100000B7,
            0x00000113 | (value << 20),
            0x0020A023,
            0x0000A183,
            0x00118213,
        )

    def service_round_trip(self, endpoint, expected_value):
        write_request = self.wait_for_request(endpoint)
        self.assertEqual(write_request.kind, RequestKind.DATA_WRITE)
        self.assertEqual(
            write_request.data, expected_value.to_bytes(4, "little")
        )
        endpoint.complete(write_request)

        read_request = self.wait_for_request(endpoint)
        self.assertEqual(read_request.kind, RequestKind.DATA_READ)
        endpoint.complete(
            read_request, data=expected_value.to_bytes(4, "little")
        )
        return write_request, read_request

    def test_worker_mmio_round_trip(self):
        image = self.mmio_program(42)
        seen = []

        with self.library.create_endpoint(13) as endpoint:
            endpoint.load_image(image)
            endpoint.start(entry_pc=0, max_steps=5)

            for _ in range(100_000):
                request = endpoint.poll()
                if request is not None:
                    self.assertEqual(request.endpoint_id, 13)
                    self.assertEqual(request.address, 0x10000000)
                    self.assertEqual(request.size_bytes, 4)
                    seen.append(request.kind)

                    if request.kind == RequestKind.DATA_WRITE:
                        self.assertEqual(request.pc, 8)
                        self.assertEqual(request.data, b"\x2a\x00\x00\x00")
                        endpoint.complete(request)
                    else:
                        self.assertEqual(request.pc, 12)
                        endpoint.complete(request, data=(42).to_bytes(4, "little"))

                state = endpoint.state()
                if state.run_state == RunState.COMPLETED:
                    break
                self.assertNotEqual(state.run_state, RunState.ERROR)
                time.sleep(0)
            else:
                self.fail("timed out waiting for the ISS worker")

            self.assertEqual(
                seen,
                [RequestKind.DATA_WRITE, RequestKind.DATA_READ],
            )
            self.assertEqual(state.step_count, 5)
            self.assertEqual(state.pc, len(image))
            self.assertEqual(endpoint.read_register(3), 42)
            self.assertEqual(endpoint.read_register(4), 43)

    def test_blocked_endpoint_does_not_stall_another(self):
        with (
            self.library.create_endpoint(20) as endpoint_0,
            self.library.create_endpoint(21) as endpoint_1,
        ):
            endpoint_0.load_image(self.mmio_program(40))
            endpoint_1.load_image(self.mmio_program(41))
            endpoint_0.start(entry_pc=0, max_steps=5)
            endpoint_1.start(entry_pc=0, max_steps=5)

            endpoint_0_write = self.wait_for_request(endpoint_0)
            self.assertEqual(endpoint_0_write.endpoint_id, 20)
            self.assertEqual(
                endpoint_0.state().run_state, RunState.WAITING_MMIO
            )

            endpoint_1_write, endpoint_1_read = self.service_round_trip(
                endpoint_1, 41
            )
            endpoint_1_state = self.wait_for_state(
                endpoint_1, RunState.COMPLETED
            )

            self.assertEqual(
                endpoint_0.state().run_state, RunState.WAITING_MMIO
            )
            self.assertEqual(endpoint_1_state.step_count, 5)
            self.assertEqual(endpoint_1.read_register(3), 41)
            self.assertEqual(endpoint_1.read_register(4), 42)
            self.assertEqual(endpoint_1_write.epoch, 1)
            self.assertEqual(endpoint_1_read.epoch, 1)
            self.assertEqual(endpoint_1_write.request_id, 1)
            self.assertEqual(endpoint_1_read.request_id, 2)

            self.assertEqual(endpoint_0_write.kind, RequestKind.DATA_WRITE)
            self.assertEqual(endpoint_0_write.data, (40).to_bytes(4, "little"))
            endpoint_0.complete(endpoint_0_write)
            endpoint_0_read = self.wait_for_request(endpoint_0)
            endpoint_0.complete(
                endpoint_0_read, data=(40).to_bytes(4, "little")
            )
            self.wait_for_state(endpoint_0, RunState.COMPLETED)

            self.assertEqual(endpoint_0_write.epoch, 1)
            self.assertEqual(endpoint_0_read.epoch, 1)
            self.assertEqual(endpoint_0_write.request_id, 1)
            self.assertEqual(endpoint_0_read.request_id, 2)
            self.assertEqual(endpoint_0.read_register(3), 40)
            self.assertEqual(endpoint_0.read_register(4), 41)

    def test_rejects_bad_duplicate_and_stale_responses(self):
        image = self.mmio_program(23)

        with self.library.create_endpoint(22) as endpoint:
            endpoint.load_image(image)
            endpoint.start(entry_pc=0, max_steps=5)
            first_write = self.wait_for_request(endpoint)

            bad_requests = (
                replace(first_write, endpoint_id=first_write.endpoint_id + 1),
                replace(first_write, epoch=first_write.epoch + 1),
                replace(first_write, request_id=first_write.request_id + 1),
                replace(first_write, size_bytes=2),
            )
            for bad_request in bad_requests:
                with self.assertRaises(IssError):
                    endpoint.complete(bad_request)

            with self.assertRaises(IssError):
                endpoint.complete(first_write, status=99)
            with self.assertRaises(IssError):
                endpoint.complete(first_write, axi_resp=2)

            endpoint.complete(first_write)
            with self.assertRaises(IssError):
                endpoint.complete(first_write)

            first_read = self.wait_for_request(endpoint)
            endpoint.complete(first_read, data=(23).to_bytes(4, "little"))
            first_state = self.wait_for_state(endpoint, RunState.COMPLETED)

            endpoint.start(entry_pc=0, max_steps=5)
            second_write = self.wait_for_request(endpoint)
            self.assertEqual(second_write.epoch, first_state.epoch + 1)
            self.assertEqual(second_write.request_id, 1)

            with self.assertRaises(IssError):
                endpoint.complete(first_write)

            endpoint.complete(second_write)
            second_read = self.wait_for_request(endpoint)
            endpoint.complete(second_read, data=(23).to_bytes(4, "little"))
            second_state = self.wait_for_state(endpoint, RunState.COMPLETED)

            self.assertEqual(second_state.epoch, second_write.epoch)
            self.assertEqual(second_read.request_id, 2)
            self.assertEqual(endpoint.read_register(3), 23)
            self.assertEqual(endpoint.read_register(4), 24)

    def test_stops_local_loop_across_repeated_starts(self):
        infinite_loop = struct.pack("<I", 0x0000006F)

        with self.library.create_endpoint(23) as endpoint:
            endpoint.load_image(infinite_loop)

            for expected_epoch in range(1, 9):
                endpoint.start(entry_pc=0, max_steps=1_000_000_000)
                running_state = self.wait_for_steps(endpoint, 10)
                self.assertEqual(running_state.run_state, RunState.RUNNING)
                self.assertEqual(running_state.epoch, expected_epoch)

                with self.assertRaises(IssError):
                    endpoint.start(entry_pc=0, max_steps=1)
                with self.assertRaises(IssError):
                    endpoint.load_image(infinite_loop)

                endpoint.request_stop()
                stopped_state = self.wait_for_state(
                    endpoint, RunState.STOPPED
                )
                self.assertEqual(stopped_state.epoch, expected_epoch)
                self.assertGreaterEqual(stopped_state.step_count, 10)
                self.assertEqual(stopped_state.pending_request_id, 0)

    def test_concurrent_starts_are_serialized(self):
        infinite_loop = struct.pack("<I", 0x0000006F)
        start_barrier = Barrier(2)

        with self.library.create_endpoint(26) as endpoint:
            endpoint.load_image(infinite_loop)

            def start_worker():
                start_barrier.wait()
                try:
                    endpoint.start(entry_pc=0, max_steps=1_000_000_000)
                except IssError as error:
                    return error.status
                return None

            with ThreadPoolExecutor(max_workers=2) as executor:
                results = list(executor.map(lambda _: start_worker(), range(2)))

            self.assertEqual(results.count(None), 1)
            self.assertEqual(len([status for status in results if status == -2]), 1)
            self.wait_for_steps(endpoint, 10)
            endpoint.request_stop()
            self.wait_for_state(endpoint, RunState.STOPPED)

    def test_four_processors_run_concurrently(self):
        infinite_loop = struct.pack("<I", 0x0000006F)

        with ExitStack() as stack:
            endpoints = [
                stack.enter_context(self.library.create_endpoint(30 + index))
                for index in range(4)
            ]
            for endpoint in endpoints:
                endpoint.load_image(infinite_loop)
                endpoint.start(entry_pc=0, max_steps=1_000_000_000)

            states = [self.wait_for_steps(endpoint, 1_000) for endpoint in endpoints]
            self.assertTrue(
                all(state.run_state == RunState.RUNNING for state in states)
            )
            self.assertEqual([state.endpoint_id for state in states], [30, 31, 32, 33])

            for endpoint in endpoints:
                endpoint.request_stop()
            stopped_states = [
                self.wait_for_state(endpoint, RunState.STOPPED)
                for endpoint in endpoints
            ]

            self.assertTrue(
                all(state.step_count >= 1_000 for state in stopped_states)
            )
            self.assertTrue(
                all(state.pending_request_id == 0 for state in stopped_states)
            )

    def test_stops_blocked_mmio_and_restarts(self):
        image = self.mmio_program(31)

        with self.library.create_endpoint(24) as endpoint:
            endpoint.load_image(image)
            endpoint.start(entry_pc=0, max_steps=5)
            cancelled_request = self.wait_for_request(endpoint)

            endpoint.request_stop()
            stopped_state = self.wait_for_state(endpoint, RunState.STOPPED)
            self.assertEqual(stopped_state.epoch, 1)
            self.assertEqual(stopped_state.pending_request_id, 0)
            with self.assertRaises(IssError):
                endpoint.complete(cancelled_request)

            endpoint.start(entry_pc=0, max_steps=5)
            write_request, read_request = self.service_round_trip(endpoint, 31)
            completed_state = self.wait_for_state(
                endpoint, RunState.COMPLETED
            )

            self.assertEqual(completed_state.epoch, 2)
            self.assertEqual(write_request.epoch, 2)
            self.assertEqual(read_request.epoch, 2)
            self.assertEqual(endpoint.read_register(3), 31)
            self.assertEqual(endpoint.read_register(4), 32)

    def test_close_wakes_worker_blocked_on_mmio(self):
        endpoint = self.library.create_endpoint(25)
        endpoint.load_image(self.mmio_program(17))
        endpoint.start(entry_pc=0, max_steps=5)
        self.wait_for_request(endpoint)

        start_time = time.monotonic()
        endpoint.close()
        self.assertLess(time.monotonic() - start_time, POLL_TIMEOUT_SECONDS)

        endpoint.close()
        with self.assertRaises(IssError):
            endpoint.state()


if __name__ == "__main__":
    unittest.main()