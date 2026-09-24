# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

from __future__ import annotations

import ctypes
from dataclasses import dataclass
from enum import IntEnum
from pathlib import Path

ABI_VERSION = 1
OK = 0
NOT_READY = 1


class RunState(IntEnum):
    READY = 0
    RUNNING = 1
    WAITING_MMIO = 2
    COMPLETED = 3
    STOPPED = 4
    ERROR = 5


class RequestKind(IntEnum):
    DATA_READ = 1
    DATA_WRITE = 2


class ResponseStatus(IntEnum):
    OK = 0
    BUS_ERROR = 1
    CANCELLED = 2


class _Config(ctypes.Structure):
    _fields_ = [
        ("abi_version", ctypes.c_uint32),
        ("struct_size", ctypes.c_uint32),
        ("endpoint_id", ctypes.c_uint32),
        ("reserved", ctypes.c_uint32),
        ("imem_base", ctypes.c_uint64),
        ("imem_size", ctypes.c_uint64),
        ("reset_pc", ctypes.c_uint64),
    ]


class _Request(ctypes.Structure):
    _fields_ = [
        ("abi_version", ctypes.c_uint32),
        ("struct_size", ctypes.c_uint32),
        ("endpoint_id", ctypes.c_uint32),
        ("kind", ctypes.c_uint32),
        ("epoch", ctypes.c_uint64),
        ("request_id", ctypes.c_uint64),
        ("address", ctypes.c_uint64),
        ("pc", ctypes.c_uint64),
        ("size_bytes", ctypes.c_uint32),
        ("byte_enable", ctypes.c_uint32),
        ("data", ctypes.c_uint8 * 4),
        ("reserved", ctypes.c_uint8 * 4),
    ]


class _Response(ctypes.Structure):
    _fields_ = [
        ("abi_version", ctypes.c_uint32),
        ("struct_size", ctypes.c_uint32),
        ("endpoint_id", ctypes.c_uint32),
        ("status", ctypes.c_uint32),
        ("epoch", ctypes.c_uint64),
        ("request_id", ctypes.c_uint64),
        ("axi_resp", ctypes.c_uint32),
        ("size_bytes", ctypes.c_uint32),
        ("data", ctypes.c_uint8 * 4),
        ("reserved", ctypes.c_uint8 * 4),
        ("accepted_sim_tick", ctypes.c_uint64),
        ("completed_sim_tick", ctypes.c_uint64),
    ]


class _State(ctypes.Structure):
    _fields_ = [
        ("abi_version", ctypes.c_uint32),
        ("struct_size", ctypes.c_uint32),
        ("endpoint_id", ctypes.c_uint32),
        ("run_state", ctypes.c_uint32),
        ("epoch", ctypes.c_uint64),
        ("step_count", ctypes.c_uint64),
        ("pc", ctypes.c_uint64),
        ("pending_request_id", ctypes.c_uint64),
    ]


assert ctypes.sizeof(_Config) == 40
assert ctypes.sizeof(_Request) == 64
assert ctypes.sizeof(_Response) == 64
assert ctypes.sizeof(_State) == 48


@dataclass(frozen=True)
class Request:
    endpoint_id: int
    kind: RequestKind
    epoch: int
    request_id: int
    address: int
    pc: int
    size_bytes: int
    byte_enable: int
    data: bytes


@dataclass(frozen=True)
class State:
    endpoint_id: int
    run_state: RunState
    epoch: int
    step_count: int
    pc: int
    pending_request_id: int


class IssError(RuntimeError):
    def __init__(self, operation: str, status: int, message: str):
        super().__init__(f"{operation} failed: {message} ({status})")
        self.operation = operation
        self.status = status


class IssLibrary:
    def __init__(self, path: str | Path):
        self._native = ctypes.CDLL(str(Path(path).resolve()))
        self._declare_api()
        version = self._native.openenoc_iss_abi_version()
        if version != ABI_VERSION:
            raise RuntimeError(
                f"ISS ABI mismatch: expected {ABI_VERSION}, found {version}"
            )

    def _declare_api(self) -> None:
        native = self._native
        native.openenoc_iss_abi_version.argtypes = []
        native.openenoc_iss_abi_version.restype = ctypes.c_uint32
        native.openenoc_iss_status_string.argtypes = [ctypes.c_int32]
        native.openenoc_iss_status_string.restype = ctypes.c_char_p
        native.openenoc_iss_create.argtypes = [
            ctypes.POINTER(_Config),
            ctypes.POINTER(ctypes.c_void_p),
        ]
        native.openenoc_iss_create.restype = ctypes.c_int32
        native.openenoc_iss_destroy.argtypes = [ctypes.c_void_p]
        native.openenoc_iss_destroy.restype = None
        native.openenoc_iss_load_image.argtypes = [
            ctypes.c_void_p,
            ctypes.c_uint64,
            ctypes.POINTER(ctypes.c_uint8),
            ctypes.c_uint64,
        ]
        native.openenoc_iss_load_image.restype = ctypes.c_int32
        native.openenoc_iss_start.argtypes = [
            ctypes.c_void_p,
            ctypes.c_uint64,
            ctypes.c_uint64,
        ]
        native.openenoc_iss_start.restype = ctypes.c_int32
        native.openenoc_iss_request_stop.argtypes = [ctypes.c_void_p]
        native.openenoc_iss_request_stop.restype = ctypes.c_int32
        native.openenoc_iss_try_poll.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(_Request),
        ]
        native.openenoc_iss_try_poll.restype = ctypes.c_int32
        native.openenoc_iss_complete.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(_Response),
        ]
        native.openenoc_iss_complete.restype = ctypes.c_int32
        native.openenoc_iss_try_state.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(_State),
        ]
        native.openenoc_iss_try_state.restype = ctypes.c_int32
        native.openenoc_iss_read_register.argtypes = [
            ctypes.c_void_p,
            ctypes.c_uint32,
            ctypes.POINTER(ctypes.c_uint64),
        ]
        native.openenoc_iss_read_register.restype = ctypes.c_int32

    def _check(self, operation: str, status: int) -> None:
        if status == OK:
            return
        message = self._native.openenoc_iss_status_string(status).decode()
        raise IssError(operation, status, message)

    def create_endpoint(
        self,
        endpoint_id: int,
        *,
        imem_base: int = 0,
        imem_size: int = 32 * 1024,
        reset_pc: int = 0,
    ) -> Endpoint:
        config = _Config(
            abi_version=ABI_VERSION,
            struct_size=ctypes.sizeof(_Config),
            endpoint_id=endpoint_id,
            imem_base=imem_base,
            imem_size=imem_size,
            reset_pc=reset_pc,
        )
        handle = ctypes.c_void_p()
        self._check(
            "create endpoint",
            self._native.openenoc_iss_create(
                ctypes.byref(config), ctypes.byref(handle)
            ),
        )
        return Endpoint(self, handle)


class Endpoint:
    def __init__(self, library: IssLibrary, handle: ctypes.c_void_p):
        self._library = library
        self._handle = handle

    def __enter__(self) -> Endpoint:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.close()

    def close(self) -> None:
        if self._handle:
            self._library._native.openenoc_iss_destroy(self._handle)
            self._handle = ctypes.c_void_p()

    def load_image(self, image: bytes, address: int = 0) -> None:
        if not image:
            raise ValueError("image must not be empty")
        payload = (ctypes.c_uint8 * len(image)).from_buffer_copy(image)
        self._library._check(
            "load image",
            self._library._native.openenoc_iss_load_image(
                self._handle, address, payload, len(image)
            ),
        )

    def start(self, *, entry_pc: int = 0, max_steps: int) -> None:
        self._library._check(
            "start endpoint",
            self._library._native.openenoc_iss_start(
                self._handle, entry_pc, max_steps
            ),
        )

    def request_stop(self) -> None:
        self._library._check(
            "request stop",
            self._library._native.openenoc_iss_request_stop(self._handle),
        )

    def poll(self) -> Request | None:
        native_request = _Request(
            abi_version=ABI_VERSION,
            struct_size=ctypes.sizeof(_Request),
        )
        status = self._library._native.openenoc_iss_try_poll(
            self._handle, ctypes.byref(native_request)
        )
        if status == NOT_READY:
            return None
        self._library._check("poll request", status)
        return Request(
            endpoint_id=native_request.endpoint_id,
            kind=RequestKind(native_request.kind),
            epoch=native_request.epoch,
            request_id=native_request.request_id,
            address=native_request.address,
            pc=native_request.pc,
            size_bytes=native_request.size_bytes,
            byte_enable=native_request.byte_enable,
            data=bytes(native_request.data[: native_request.size_bytes]),
        )

    def complete(
        self,
        request: Request,
        *,
        data: bytes = b"",
        status: ResponseStatus = ResponseStatus.OK,
        axi_resp: int = 0,
        accepted_sim_tick: int = 0,
        completed_sim_tick: int = 0,
    ) -> None:
        if (status == ResponseStatus.OK and
                request.kind == RequestKind.DATA_READ and
                len(data) != request.size_bytes):
            raise ValueError("successful read response has the wrong size")
        if len(data) > 4:
            raise ValueError("response data exceeds the RV32 payload size")

        native_response = _Response(
            abi_version=ABI_VERSION,
            struct_size=ctypes.sizeof(_Response),
            endpoint_id=request.endpoint_id,
            status=status,
            epoch=request.epoch,
            request_id=request.request_id,
            axi_resp=axi_resp,
            size_bytes=request.size_bytes,
            accepted_sim_tick=accepted_sim_tick,
            completed_sim_tick=completed_sim_tick,
        )
        for index, value in enumerate(data):
            native_response.data[index] = value

        self._library._check(
            "complete request",
            self._library._native.openenoc_iss_complete(
                self._handle, ctypes.byref(native_response)
            ),
        )

    def state(self) -> State:
        native_state = _State(
            abi_version=ABI_VERSION,
            struct_size=ctypes.sizeof(_State),
        )
        self._library._check(
            "read state",
            self._library._native.openenoc_iss_try_state(
                self._handle, ctypes.byref(native_state)
            ),
        )
        return State(
            endpoint_id=native_state.endpoint_id,
            run_state=RunState(native_state.run_state),
            epoch=native_state.epoch,
            step_count=native_state.step_count,
            pc=native_state.pc,
            pending_request_id=native_state.pending_request_id,
        )

    def read_register(self, index: int) -> int:
        value = ctypes.c_uint64()
        self._library._check(
            f"read x{index}",
            self._library._native.openenoc_iss_read_register(
                self._handle, index, ctypes.byref(value)
            ),
        )
        return value.value