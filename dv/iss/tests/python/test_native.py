# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

import os
import struct
import time
import unittest

from openenoc_iss import IssLibrary, RequestKind, RunState


class NativeApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.library = IssLibrary(os.environ["OPENENOC_ISS_LIBRARY"])

    def test_worker_mmio_round_trip(self):
        image = struct.pack(
            "<5I",
            0x100000B7,
            0x02A00113,
            0x0020A023,
            0x0000A183,
            0x00118213,
        )
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


if __name__ == "__main__":
    unittest.main()