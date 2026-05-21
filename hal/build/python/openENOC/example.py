

"""
Python Wrapper for the openENOC register model

This code was generated from the PeakRDL-python package version 3.1.1

"""





from .lib import NormalCallbackSet

from .reg_model.openENOC import openENOC_cls
from .sim.openENOC import openENOC_simulator_cls

if __name__ == '__main__':

    sim = openENOC_simulator_cls(address=0)

    # create an instance of the class
    reg_model = openENOC_cls(callbacks=NormalCallbackSet(read_callback=sim.read,
                                                                       write_callback=sim.write))