

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.1

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions
    
    
class csr_test_reg_test_field_neg_0x6c98d4d4cef03c0c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.test_reg.test_field[31:0]                                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>4-byte test field</p>                                           |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []

    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr.test_reg.test_field[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "4-byte test field"
    
    
    


if __name__ == '__main__':
    pass