


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



from ..lib import Node, NodeArray, Base
from ..lib import UDPStruct

from ..lib  import AddressMapArray, RegFileArray
from ..lib import Memory, MemoryArray
from ..lib import AddressMap
from ..lib import RegFile
from ..lib  import AddressMapArray
from ..lib  import RegFileArray
from ..lib import MemoryReadOnly, MemoryWriteOnly, MemoryReadWrite
from ..lib import MemoryReadOnlyArray, MemoryWriteOnlyArray, MemoryReadWriteArray
from ..lib import Reg, RegArray
from ..lib import RegReadOnly, RegWriteOnly, RegReadWrite
from ..lib import RegReadOnlyArray, RegWriteOnlyArray, RegReadWriteArray
from ..lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field

from ..lib import ReadableRegister, WritableRegister
from ..lib import ReadableMemory, WritableMemory
from ..lib import ReadableRegisterArray, WriteableRegisterArray



from ..lib import NormalCallbackSet, NormalCallbackSetLegacy





from ._registers import csr_test_reg_neg_0x11ed3ba64059592c_cls
from ._memories import openENOC_imem_neg_0x51cfe0763150725f_cls
from ._memories import openENOC_dmem_neg_0x5514bdc66237be6d_cls


# addrmap, regfile, memor and register definitions
    
    
class csr_neg_0x3e881fb4dd77046b_cls(AddressMap):
    """
    Class to represent a address map in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr                                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>openENOC CSR</p>                                                |
    +--------------+-------------------------------------------------------------------------+
    """

    __slots__ : list[str] = ['__test_reg']

    def __init__(self, *,
                 address:int,
                 logger_handle:str,
                 inst_name:str,
                 callbacks: Optional[Union[NormalCallbackSet, NormalCallbackSetLegacy]]=None,
                 parent:Optional[AddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (NormalCallbackSet, NormalCallbackSetLegacy)):
                raise TypeError(f'callbacks should be NormalCallbackSet, NormalCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
            
        self.__test_reg:csr_test_reg_neg_0x11ed3ba64059592c_cls = csr_test_reg_neg_0x11ed3ba64059592c_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.test_reg',
                                                                     inst_name='test_reg', parent=self)
        

    @property
    def size(self) -> int:
        return 4
    @property
    def test_reg(self) -> 'csr_test_reg_neg_0x11ed3ba64059592c_cls':
        """
        Property to access test_reg 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr.test_reg                                                       |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>Test register</p>                                               |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__test_reg
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'test_reg':'test_reg',
            }

    
    
    
    
    
    
                
    def get_child_by_system_rdl_name(self, name: Any) -> 'csr_test_reg_neg_0x11ed3ba64059592c_cls':
        return super().get_child_by_system_rdl_name(name)
                
    


    

    
    

    @property
    def rdl_name(self) -> str:
        return "csr"
    @property
    def rdl_desc(self) -> str:
        return "openENOC CSR"
    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.test_reg
        
        
    

    
    
class openENOC_neg_0x3a6b88f20b05c507_cls(AddressMap):
    """
    Class to represent a address map in the register model

    
    """

    __slots__ : list[str] = ['__imem', '__dmem', '__csr']

    def __init__(self, *,
                 address:int=0,
                 logger_handle:str='reg_model.openENOC',
                 inst_name:str='openENOC',
                 callbacks: Optional[Union[NormalCallbackSet, NormalCallbackSetLegacy]]=None,
                 parent:Optional[AddressMap]=None):

        if callbacks is not None:
            if not isinstance(callbacks, (NormalCallbackSet, NormalCallbackSetLegacy)):
                raise TypeError(f'callbacks should be NormalCallbackSet, NormalCallbackSetLegacy got {type(callbacks)}')

        super().__init__(callbacks=callbacks,
                         address=address,
                         logger_handle=logger_handle,
                         inst_name=inst_name,
                         parent=parent)

        
        self.__imem:openENOC_imem_neg_0x51cfe0763150725f_cls = openENOC_imem_neg_0x51cfe0763150725f_cls(
                                                                     address=self.address+0,
                                                                     logger_handle=logger_handle+'.imem',
                                                                                       inst_name='imem', parent=self)
        
        self.__dmem:openENOC_dmem_neg_0x5514bdc66237be6d_cls = openENOC_dmem_neg_0x5514bdc66237be6d_cls(
                                                                     address=self.address+268435456,
                                                                     logger_handle=logger_handle+'.dmem',
                                                                                       inst_name='dmem', parent=self)
        self.__csr:csr_neg_0x3e881fb4dd77046b_cls = csr_neg_0x3e881fb4dd77046b_cls(
                                                                                address=self.address+536870912,
                                                                                logger_handle=logger_handle+'.csr',
                                                                                inst_name='csr',
                                                                                parent=self)
        

    @property
    def size(self) -> int:
        return 536870916
    @property
    def imem(self) -> 'openENOC_imem_neg_0x51cfe0763150725f_cls':
        """
        Property to access imem 

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
        return self.__imem
        
    @property
    def dmem(self) -> 'openENOC_dmem_neg_0x5514bdc66237be6d_cls':
        """
        Property to access dmem 

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
        return self.__dmem
        
    @property
    def csr(self) -> 'csr_neg_0x3e881fb4dd77046b_cls':
        """
        Property to access csr 

        +--------------+-------------------------------------------------------------------------+
        | SystemRDL    | Value                                                                   |
        | Field        |                                                                         |
        +==============+=========================================================================+
        | Name         | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      csr                                                                |
        +--------------+-------------------------------------------------------------------------+
        | Description  | .. raw:: html                                                           |
        |              |                                                                         |
        |              |      <p>openENOC CSR</p>                                                |
        +--------------+-------------------------------------------------------------------------+
        """
        return self.__csr
        

    
    @property
    def systemrdl_python_child_name_map(self) -> dict[str, str]:
        return {'imem':'imem','dmem':'dmem','csr':'csr',
            }

    
    
    
    
    
    
    # nodes:3
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["imem"]) -> 'openENOC_imem_neg_0x51cfe0763150725f_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["dmem"]) -> 'openENOC_dmem_neg_0x5514bdc66237be6d_cls': ...
                
                
    @overload
    def get_child_by_system_rdl_name(self, name: Literal["csr"]) -> 'csr_neg_0x3e881fb4dd77046b_cls': ...
                

    @overload
    def get_child_by_system_rdl_name(self, name: str) -> Union['openENOC_imem_neg_0x51cfe0763150725f_cls', 'openENOC_dmem_neg_0x5514bdc66237be6d_cls', 'csr_neg_0x3e881fb4dd77046b_cls', ]: ...

    def get_child_by_system_rdl_name(self, name: Any) -> Any:
        return super().get_child_by_system_rdl_name(name)
    


    

    
    

    
    

    
    def __iter__(self) -> Iterator[Union[Node, NodeArray]]:
        
        
        yield self.imem
        yield self.dmem
        yield self.csr
        
        
    


openENOC_cls = openENOC_neg_0x3a6b88f20b05c507_cls

if __name__ == '__main__':
    # dummy functions to demonstrate the class
    def read_addr_space(addr: int, width: int, accesswidth: int) -> int:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits

        Returns:
            value inputted by the used
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        return int(input('value to read from address:0x%X'%addr))

    def write_addr_space(addr: int, width: int, accesswidth: int, data: int) -> None:
        """
        Callback to simulate the operation of the package, everytime the read is called, it will
        request the user input the value to be read back.

        Args:
            addr: Address to write to
            width: Width of the register in bits
            accesswidth: Minimum access width of the register in bits
            data: value to be written to the register

        Returns:
            None
        """
        assert isinstance(addr, int)
        assert isinstance(width, int)
        assert isinstance(accesswidth, int)
        assert isinstance(data, int)
        print('write data:0x%X to address:0x%X'%(data, addr))

    # create an instance of the class
    openENOC = openENOC_cls(callbacks = NormalCallbackSet(read_callback=read_addr_space,
                                                                                                     write_callback=write_addr_space))