

"""
Python Wrapper for the openENOC register model

This code was generated from the PeakRDL-python package version 3.1.1

"""











from typing import Iterator
from typing import Optional
from typing import Union
from typing import Type
from typing import overload
from typing import Literal
from typing import Any
from typing import NoReturn
import warnings


from ...lib import Node, NodeArray, Base
from ...lib import UDPStruct

from ...lib import Memory, MemoryArray
from ...lib import AddressMap
from ...lib import MemoryReadOnly, MemoryWriteOnly, MemoryReadWrite
from ...lib import MemoryReadOnlyArray, MemoryWriteOnlyArray, MemoryReadWriteArray
from ...lib import Reg, RegArray





# memory definitions
    
    
class openENOC_imem_neg_0x51cfe0763150725f_cls(MemoryReadWrite):
    """
    Class to represent a memory in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      imem                                                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>CPU Program Memory</p>                                          |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent:AddressMap):

        super().__init__(address=address,
                         entries=8192,
                         accesswidth=32,
                         width=32,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        

    
    def __iter__(self) -> Iterator[Union[Reg,RegArray]]:
        
        
        # Empty generator in case there are no children of this type
        if False: yield
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {
            }

    
    
    
    
    
    
    def get_child_by_system_rdl_name(self, name: Any) -> NoReturn:
        raise KeyError('This node has no children')
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "imem"
    @property
    def rdl_desc(self) -> str:
        return "CPU Program Memory"
    
    
    

    
    
class openENOC_dmem_neg_0x5514bdc66237be6d_cls(MemoryReadWrite):
    """
    Class to represent a memory in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      dmem                                                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>CPU Data Memory</p>                                             |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = []

    def __init__(self,
                 address: int,
                 logger_handle: str,
                 inst_name: str,
                 parent:AddressMap):

        super().__init__(address=address,
                         entries=8192,
                         accesswidth=32,
                         width=32,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        

    
    def __iter__(self) -> Iterator[Union[Reg,RegArray]]:
        
        
        # Empty generator in case there are no children of this type
        if False: yield
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {
            }

    
    
    
    
    
    
    def get_child_by_system_rdl_name(self, name: Any) -> NoReturn:
        raise KeyError('This node has no children')
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "dmem"
    @property
    def rdl_desc(self) -> str:
        return "CPU Data Memory"
    
    
    


if __name__ == '__main__':
    pass