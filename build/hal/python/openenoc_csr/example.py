

"""
Python Wrapper for the openenoc_csr register model

This code was generated from the PeakRDL-python package version 3.1.1

"""





from .lib import NormalCallbackSet

from .reg_model.openenoc_csr import openenoc_csr_cls
from .sim.openenoc_csr import openenoc_csr_simulator_cls

if __name__ == '__main__':

    sim = openenoc_csr_simulator_cls(address=0)

    # create an instance of the class
    reg_model = openenoc_csr_cls(callbacks=NormalCallbackSet(read_callback=sim.read,
                                                                       write_callback=sim.write))