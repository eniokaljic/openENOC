


"""
Unit Tests for the csr register model Python Wrapper

This code was generated from the PeakRDL-python package version 3.1.2
"""







from array import array as Array

import unittest
import random



from ..lib import RegisterWriteVerifyError

from ..lib import NormalCallbackSet, NormalCallbackSetLegacy



from ..reg_model import RegModel
from ..sim import Simulator
from ..sim_lib.simulator import BaseSimulator

from ..sim_lib.dummy_callbacks import dummy_read as read_addr_space
from ..sim_lib.dummy_callbacks import dummy_write as write_addr_space
from ..sim_lib.dummy_callbacks import dummy_read_block as read_block_addr_space
from ..sim_lib.dummy_callbacks import dummy_write_block as write_block_addr_space
from ..sim_lib.dummy_callbacks import dummy_read_block_legacy as read_block_addr_space_alt
from ..sim_lib.dummy_callbacks import dummy_write_block_legacy as write_block_addr_space_alt
from ..lib_test import LibTestBase as TestCaseBase
BlockTestBase = unittest.TestCase



from ..lib import SystemRDLEnum, SystemRDLEnumEntry


def read_callback(addr: int, width: int, accesswidth: int) -> int:
    return read_addr_space(addr=addr, width=width, accesswidth=accesswidth)

def read_block_callback(addr: int, width: int, accesswidth: int, length: int) -> list[int]:
    return read_block_addr_space(addr=addr, width=width, accesswidth=accesswidth, length=length)

def read_block_callback_alt(addr: int, width: int, accesswidth: int, length: int) -> Array:
    return read_block_addr_space_alt(addr=addr, width=width, accesswidth=accesswidth, length=length)

def write_callback(addr: int, width: int, accesswidth: int,  data: int) -> None:
    write_addr_space(addr=addr, width=width, accesswidth=accesswidth, data=data)

def write_block_callback(addr: int, width: int, accesswidth: int,  data: list[int]) -> None:
    write_block_addr_space(addr=addr, width=width, accesswidth=accesswidth, data=data)

def write_block_callback_alt(addr: int, width: int, accesswidth: int,  data: Array) -> None:
    write_block_addr_space_alt(addr=addr, width=width, accesswidth=accesswidth, data=data)

def random_enum_reg_value(enum_class: type[SystemRDLEnum]) -> SystemRDLEnum:
    return random.choice(list(enum_class))


class csr_TestCase(TestCaseBase): # type: ignore[valid-type,misc]

    def read_callback(self, addr: int, width: int, accesswidth: int) -> int:
        return self.sim.read(addr=addr, width=width, accesswidth=accesswidth)

    def write_callback(self, addr: int, width: int, accesswidth: int,  data: int) -> None:
        return self.sim.write(addr=addr, width=width, accesswidth=accesswidth, data=data)

    @property
    def simulator_instance(self) -> BaseSimulator:
        return self.sim

    @property
    def legacy_block_access(self) -> bool:
        return False

    def setUp(self) -> None:
        self.sim = Simulator(address=0)
        self.dut = RegModel(callbacks=NormalCallbackSet(read_callback=self.outer_read_callback,
                                                          write_callback=self.outer_write_callback))

class csr_TestCase_BlockAccess(BlockTestBase): # type: ignore[valid-type,misc]

    def setUp(self) -> None:
        self.dut = RegModel(callbacks=NormalCallbackSet(read_callback=read_callback,
                                                          write_callback=write_callback,
                                                          read_block_callback=read_block_callback,
                                                          write_block_callback=write_block_callback))

class csr_TestCase_AltBlockAccess(BlockTestBase): # type: ignore[valid-type,misc]
    """
    Based test to use with the alternative call backs, this allow the legacy output API to be tested
    with the new callbacks and visa versa.
    """


    def setUp(self) -> None:
        self.dut = RegModel(callbacks=NormalCallbackSetLegacy(
                                                          read_callback=read_callback,
                                                          write_callback=write_callback,
                                                          read_block_callback=read_block_callback_alt,
                                                          write_block_callback=write_block_callback_alt))




if __name__ == '__main__':
    pass



