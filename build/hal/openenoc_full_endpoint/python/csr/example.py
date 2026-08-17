

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""





from .lib import NormalCallbackSet

from .reg_model.csr import csr_cls
from .sim.csr import csr_simulator_cls

if __name__ == '__main__':

    sim = csr_simulator_cls(address=0)

    # create an instance of the class
    reg_model = csr_cls(callbacks=NormalCallbackSet(read_callback=sim.read,
                                                                       write_callback=sim.write))