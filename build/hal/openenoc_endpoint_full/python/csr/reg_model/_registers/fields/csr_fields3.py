

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions


class openenoc_endpoint_interface_peers_entry_dma_mode_neg_0x7b78380871f25d0e_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].dma.mode[1:0]                                                   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>DMA mode and responder access policy for the remote             |
    |              |      peer:<ul></p> <li>0: Disabled. Locally initiated DMA and           |
    |              |      transparent RMEM operations are disabled, and incoming oETP memory |
    |              |      requests from this peer are rejected.</li>  <li>1: Transparent     |
    |              |      RMEM mode. Accesses to the virtual RMEM region are translated into |
    |              |      individual remote memory accesses. Incoming transparent RMEM read  |
    |              |      and write requests from this peer are permitted. Bulk DMA read and |
    |              |      write requests are rejected.</li>  <li>2: Mirror-to-local mode. A  |
    |              |      locally initiated DMA request fetches the remote memory region     |
    |              |      into the configured local memory region using remote DMA reads. On |
    |              |      the responder side, incoming bulk DMA write requests from this     |
    |              |      peer are permitted and target the configured local memory region.  |
    |              |      Incoming bulk DMA read requests are rejected.</li>  <li>3: Mirror- |
    |              |      to-remote mode. A locally initiated DMA request sends the          |
    |              |      configured local memory region to the remote memory region using   |
    |              |      remote DMA writes. On the responder side, incoming bulk DMA read   |
    |              |      requests from this peer are permitted and source data from the     |
    |              |      configured local memory region. Incoming bulk DMA write requests   |
    |              |      are rejected.</li>  </ul> <p>Consequently, a mirror relationship   |
    |              |      uses complementary modes: an initiator operating in mirror-to-     |
    |              |      local mode communicates with a responder entry configured as       |
    |              |      mirror-to-remote, while an initiator operating in mirror-to-remote |
    |              |      mode communicates with a responder entry configured as mirror-to-  |
    |              |      local.</p>                                                         |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.mode[1:0]"
    @property
    def rdl_desc(self) -> str:
        return "DMA mode and responder access policy for the remote peer:\u003cul\u003e\n\n\u003cli\u003e0: Disabled. Locally initiated DMA and transparent RMEM\noperations are disabled, and incoming oETP memory requests from\nthis peer are rejected.\u003c/li\u003e\n\n\u003cli\u003e1: Transparent RMEM mode. Accesses to the virtual RMEM region\nare translated into individual remote memory accesses. Incoming\ntransparent RMEM read and write requests from this peer are\npermitted. Bulk DMA read and write requests are rejected.\u003c/li\u003e\n\n\u003cli\u003e2: Mirror-to-local mode. A locally initiated DMA request fetches\nthe remote memory region into the configured local memory region\nusing remote DMA reads. On the responder side, incoming bulk DMA\nwrite requests from this peer are permitted and target the\nconfigured local memory region. Incoming bulk DMA read requests\nare rejected.\u003c/li\u003e\n\n\u003cli\u003e3: Mirror-to-remote mode. A locally initiated DMA request sends\nthe configured local memory region to the remote memory region\nusing remote DMA writes. On the responder side, incoming bulk DMA\nread requests from this peer are permitted and source data from\nthe configured local memory region. Incoming bulk DMA write\nrequests are rejected.\u003c/li\u003e\n\n\u003c/ul\u003e\n\nConsequently, a mirror relationship uses complementary modes:\nan initiator operating in mirror-to-local mode communicates with\na responder entry configured as mirror-to-remote, while an\ninitiator operating in mirror-to-remote mode communicates with a\nresponder entry configured as mirror-to-local."






class openenoc_endpoint_interface_peers_entry_dma_irq_enable_0x13adf522afa89a04_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].dma.irq_enable                                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Enables generation of a PEER_DMA_COMPLETE IRQ event for this    |
    |              |      peer. Hardware samples this field together with                    |
    |              |      irq.event_enable.peer_dma_complete when it accepts the peer DMA    |
    |              |      request. Changing the field while a transfer is active does not    |
    |              |      affect that transfer. Disabling the field does not affect DMA      |
    |              |      execution or the done, error, and error_code status fields. For a  |
    |              |      failed incoming bulk DMA request, this field is captured when      |
    |              |      recording the failure and irq.event_enable.peer_dma_complete is    |
    |              |      sampled at IRQ admission. The event identifies this peer by the    |
    |              |      received source MAC. Successful incoming requests generate no      |
    |              |      event. RMEM errors use their separate irq.event_enable.rmem_error  |
    |              |      path.</p>                                                          |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.irq_enable"
    @property
    def rdl_desc(self) -> str:
        return "Enables generation of a PEER_DMA_COMPLETE IRQ event for this peer.\nHardware samples this field together with irq.event_enable.peer_dma_complete\nwhen it accepts the peer DMA request. Changing the field while a transfer is\nactive does not affect that transfer. Disabling the field does not affect\nDMA execution or the done, error, and error_code status fields. For a\nfailed incoming bulk DMA request, this field is captured when recording\nthe failure and irq.event_enable.peer_dma_complete is sampled at IRQ\nadmission. The event identifies this peer by the received source MAC.\nSuccessful incoming requests generate no event. RMEM errors use their\nseparate irq.event_enable.rmem_error path."






class openenoc_endpoint_interface_peers_entry_dma_request_0x62a887a898cd772c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].dma.request[8:8]                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Writing one requests a DMA transfer to or from the remote peer, |
    |              |      according to dma.mode. The field remains asserted until the DMA    |
    |              |      engine accepts and snapshots the request. Hardware clears it upon  |
    |              |      acceptance; while a transfer for this peer is active, a newly      |
    |              |      asserted request remains pending. Software or an RTL controller    |
    |              |      shall read the completion status of the previous request before    |
    |              |      asserting this field for the next request and shall keep the peer  |
    |              |      configuration stable while this field is asserted.</p>             |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.request[8:8]"
    @property
    def rdl_desc(self) -> str:
        return "Writing one requests a DMA transfer to or from the remote peer,\naccording to dma.mode. The field remains asserted until the DMA engine\naccepts and snapshots the request. Hardware clears it upon acceptance;\nwhile a transfer for this peer is active, a newly asserted request remains\npending. Software or an RTL controller shall read the completion status of\nthe previous request before asserting this field for the next request and\nshall keep the peer configuration stable while this field is asserted."






class openenoc_endpoint_interface_peers_entry_dma_clear_error_0x346423c994b788f1_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].dma.clear_error                                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Writing one clears this peer's shared RMEM/DMA error flag and   |
    |              |      error code. The field remains asserted until hardware accepts and  |
    |              |      clears the command. It does not abort an active operation, clear   |
    |              |      done, or complete an IRQ claim. A new failure takes precedence     |
    |              |      over a simultaneous clear. Starting or successfully completing an  |
    |              |      operation does not clear a previously recorded error.</p>          |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.clear_error"
    @property
    def rdl_desc(self) -> str:
        return "Writing one clears this peer\u0027s shared RMEM/DMA error flag and error\ncode. The field remains asserted until hardware accepts and clears the\ncommand. It does not abort an active operation, clear done, or complete\nan IRQ claim. A new failure takes precedence over a simultaneous clear.\nStarting or successfully completing an operation does not clear a\npreviously recorded error."






class openenoc_endpoint_interface_peers_entry_dma_idle_0x9e29a917cec77bb_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].dma.idle[16:16]                                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates whether this peer has no accepted DMA request in      |
    |              |      progress. Hardware deasserts this field when a request is accepted |
    |              |      and asserts it after all fragments of the requested block have     |
    |              |      completed.</p>                                                     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.idle[16:16]"
    @property
    def rdl_desc(self) -> str:
        return "Indicates whether this peer has no accepted DMA request in progress.\nHardware deasserts this field when a request is accepted and asserts it\nafter all fragments of the requested block have completed."






class openenoc_endpoint_interface_peers_entry_dma_done_neg_0x14e1cabbad6c980c_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].dma.done[24:24]                                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sticky successful-completion flag for this peer. Hardware sets  |
    |              |      this field after all fragments of the accepted block transfer      |
    |              |      complete successfully and clears it when the next request is       |
    |              |      accepted.</p>                                                      |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.done[24:24]"
    @property
    def rdl_desc(self) -> str:
        return "Sticky successful-completion flag for this peer. Hardware sets this\nfield after all fragments of the accepted block transfer complete\nsuccessfully and clears it when the next request is accepted."






class openenoc_endpoint_interface_peers_entry_dma_error_0x7b5e53815b0db6f_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].dma.error[25:25]                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Shared sticky RMEM/DMA error flag for this peer. Hardware sets  |
    |              |      this field when a locally initiated RMEM access or bulk DMA        |
    |              |      transfer fails, or when servicing an incoming RMEM or bulk DMA     |
    |              |      request from this peer fails. Received requests are associated by  |
    |              |      source MAC. An incoming failure records its code before exposing   |
    |              |      its error response, independently of IRQ enable; it does not       |
    |              |      change the locally initiated dma.request, idle, or done state. An  |
    |              |      incomplete incoming DMA data frame records remote stream code 10.  |
    |              |      Multicast response suppression does not suppress this local error  |
    |              |      record or an enabled event. Only dma.clear_error or endpoint reset |
    |              |      clears a latched error; starting or successfully completing        |
    |              |      another operation does not clear it. The flag is independent of    |
    |              |      the IRQ event-enable fields.</p>                                   |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error[25:25]"
    @property
    def rdl_desc(self) -> str:
        return "Shared sticky RMEM/DMA error flag for this peer. Hardware sets this\nfield when a locally initiated RMEM access or bulk DMA transfer fails,\nor when servicing an incoming RMEM or bulk DMA request from this peer\nfails. Received requests are associated by source MAC. An incoming failure\nrecords its code before exposing its error response, independently of\nIRQ enable; it does not change the locally initiated dma.request, idle,\nor done state. An incomplete incoming DMA data frame records remote\nstream code 10. Multicast response suppression does not suppress this\nlocal error record or an enabled event.\nOnly dma.clear_error or endpoint reset clears a latched error; starting\nor successfully completing another operation does not clear it. The\nflag is independent of the IRQ event-enable fields."






class openenoc_endpoint_interface_peers_entry_dma_error_code_neg_0x184bb6e8f052f02c_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].dma.error_code[31:28]                                           |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Shared sticky code for the most recent RMEM or bulk DMA failure |
    |              |      for this peer:<ul></p> <li>0: No error.</li> <li>1: Local invalid  |
    |              |      request, configuration, descriptor, or parameters.</li> <li>2:     |
    |              |      Local stream/PDU length or TLAST error.</li> <li>3: Local          |
    |              |      supported-size or buffer-capacity overflow.</li> <li>4: Local AXI  |
    |              |      read SLVERR response.</li> <li>5: Local AXI read DECERR            |
    |              |      response.</li> <li>6: Local AXI write SLVERR response.</li> <li>7: |
    |              |      Local AXI write DECERR response.</li> <li>8: Local peer response   |
    |              |      timeout or Request ID wrap collision. An RMEM access               |
    |              |      terminates through its ACK-only boundary; a bulk DMA timeout       |
    |              |      aborts     the remaining fragments. Hardware does not retry.</li>  |
    |              |      <li>9: Remote invalid request, configuration, descriptor, or       |
    |              |      parameters.</li> <li>10: Remote stream/PDU length or TLAST error.  |
    |              |      Also used directly by     the receiver of an incomplete            |
    |              |      DMA_WRITE_REQ or DMA_READ_RSP,     including missing or incorrect  |
    |              |      EndOfData.</li> <li>11: Remote supported-size or buffer-capacity   |
    |              |      overflow.</li> <li>12: Remote AXI read SLVERR response.</li>       |
    |              |      <li>13: Remote AXI read DECERR response.</li> <li>14: Remote AXI   |
    |              |      write SLVERR response.</li> <li>15: Remote AXI write DECERR        |
    |              |      response.</li> <p></ul> Codes 1-8 describe errors detected by this |
    |              |      endpoint, including malformed responses, local memory failures,    |
    |              |      and failures while servicing received requests. Codes 9-15         |
    |              |      describe failures reported by the responding peer through a valid  |
    |              |      ERROR_RSP. Code 10 additionally reports an incomplete incoming DMA |
    |              |      data frame detected at this endpoint, without requiring an         |
    |              |      ERROR_RSP first. A missing or incorrect EndOfData uses this same   |
    |              |      code even when Ethernet padding masks the short data length. A     |
    |              |      receiver of an incomplete unicast DMA_WRITE_REQ records CSR code   |
    |              |      10 but sends ERROR_RSP wire cause 2; multicast writes generate no  |
    |              |      response. ERROR_RSP carries a 32-bit cause in the range 1-7, which |
    |              |      the initiating oETP engine validates and maps to CSR code = 8 +    |
    |              |      wire code. Values outside 1-7 are invalid response parameters and  |
    |              |      record local code 1; they must not be truncated or mistaken for    |
    |              |      local TIMEOUT = 8. The oETP initiator completion channel carries   |
    |              |      this final CSR encoding for both RMEM and bulk DMA. The responder  |
    |              |      completion channel reports its cause 1-7 for serialization as      |
    |              |      ERROR_RSP; cause 2 on an incomplete received bulk write            |
    |              |      corresponds to receiver CSR code 10. Hardware clears this field    |
    |              |      only on dma.clear_error or endpoint reset. Successful operations   |
    |              |      preserve a recorded failure. A new failure replaces the code and   |
    |              |      takes precedence over a simultaneous clear. A failed streaming     |
    |              |      transfer may have partially modified memory; error reporting does  |
    |              |      not provide rollback or an exact count of modified bytes. Software |
    |              |      manages buffer synchronization and recovery.</p>                   |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].dma.error_code[31:28]"
    @property
    def rdl_desc(self) -> str:
        return "Shared sticky code for the most recent RMEM or bulk DMA failure for this peer:\u003cul\u003e\n\u003cli\u003e0: No error.\u003c/li\u003e\n\u003cli\u003e1: Local invalid request, configuration, descriptor, or parameters.\u003c/li\u003e\n\u003cli\u003e2: Local stream/PDU length or TLAST error.\u003c/li\u003e\n\u003cli\u003e3: Local supported-size or buffer-capacity overflow.\u003c/li\u003e\n\u003cli\u003e4: Local AXI read SLVERR response.\u003c/li\u003e\n\u003cli\u003e5: Local AXI read DECERR response.\u003c/li\u003e\n\u003cli\u003e6: Local AXI write SLVERR response.\u003c/li\u003e\n\u003cli\u003e7: Local AXI write DECERR response.\u003c/li\u003e\n\u003cli\u003e8: Local peer response timeout or Request ID wrap collision. An RMEM access\n    terminates through its ACK-only boundary; a bulk DMA timeout aborts\n    the remaining fragments. Hardware does not retry.\u003c/li\u003e\n\u003cli\u003e9: Remote invalid request, configuration, descriptor, or parameters.\u003c/li\u003e\n\u003cli\u003e10: Remote stream/PDU length or TLAST error. Also used directly by\n    the receiver of an incomplete DMA_WRITE_REQ or DMA_READ_RSP,\n    including missing or incorrect EndOfData.\u003c/li\u003e\n\u003cli\u003e11: Remote supported-size or buffer-capacity overflow.\u003c/li\u003e\n\u003cli\u003e12: Remote AXI read SLVERR response.\u003c/li\u003e\n\u003cli\u003e13: Remote AXI read DECERR response.\u003c/li\u003e\n\u003cli\u003e14: Remote AXI write SLVERR response.\u003c/li\u003e\n\u003cli\u003e15: Remote AXI write DECERR response.\u003c/li\u003e\n\u003c/ul\u003e\nCodes 1-8 describe errors detected by this endpoint, including\nmalformed responses, local memory failures, and failures while servicing\nreceived requests. Codes 9-15 describe\nfailures reported by the responding peer through a valid ERROR_RSP.\nCode 10 additionally reports an incomplete incoming DMA data frame\ndetected at this endpoint, without requiring an ERROR_RSP first.\nA missing or incorrect EndOfData uses this same code even when\nEthernet padding masks the short data length. A receiver of an\nincomplete unicast DMA_WRITE_REQ records CSR code 10 but sends\nERROR_RSP wire cause 2; multicast writes generate no response.\nERROR_RSP carries a 32-bit cause in the range 1-7, which the initiating\noETP engine validates and maps to CSR code = 8 + wire code. Values\noutside 1-7 are invalid response parameters and record local code 1;\nthey must not be truncated or mistaken for local TIMEOUT = 8.\nThe oETP initiator completion channel carries this final CSR encoding\nfor both RMEM and bulk DMA. The responder completion channel reports\nits cause 1-7 for serialization as ERROR_RSP; cause 2 on an incomplete\nreceived bulk write corresponds to receiver CSR code 10. Hardware\nclears this field only on dma.clear_error or endpoint reset. Successful\noperations preserve a recorded failure. A new failure replaces the code\nand takes precedence over a simultaneous clear. A failed streaming\ntransfer may have partially modified memory; error reporting does not\nprovide rollback or an exact count of modified bytes. Software manages\nbuffer synchronization and recovery."






class openenoc_endpoint_interface_rmem_word_data_0x6c032404cbab12f7_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0] |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Data stored in this virtual memory word.</p>                    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.rmem.word[0..RMEM_TOTAL_DEPTH-1].data[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Data stored in this virtual memory word."






class openenoc_switch_interface_info_table_depth_0x6a23b2f2a4e4cad_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.info.table_depth[15:0]                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Depth of the forwarding table in this openENOC Switch instance. |
    |              |      This field reflects the TABLE_DEPTH parameter value.</p>           |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.info.table_depth[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Depth of the forwarding table in this openENOC Switch instance. This field reflects the TABLE_DEPTH parameter value."






class openenoc_switch_interface_info_num_of_interfaces_0x5b8af1cceefaacbb_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.info.num_of_interfaces[21:16]                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number of interfaces in this openENOC Switch instance. This     |
    |              |      field reflects the NUM_OF_INTERFACES parameter value.</p>          |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.info.num_of_interfaces[21:16]"
    @property
    def rdl_desc(self) -> str:
        return "Number of interfaces in this openENOC Switch instance. This field reflects the NUM_OF_INTERFACES parameter value."






class openenoc_switch_interface_forwarding_control_operation_mode_neg_0x2b68b50bbfa32a1c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_control.operation_mode[0:0]        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Mode of operation for the openENOC Switch instance. When set to |
    |              |      1, the switch operates in managed mode, allowing software to       |
    |              |      configure the forwarding table and control forwarding operations.  |
    |              |      When set to 0, the switch operates in unmanaged mode, where        |
    |              |      forwarding state is maintained autonomously by internal hardware   |
    |              |      logic without software intervention.</p>                           |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_control.operation_mode[0:0]"
    @property
    def rdl_desc(self) -> str:
        return "Mode of operation for the openENOC Switch instance. When set to 1, the switch operates in managed mode, allowing software to configure the forwarding table and control forwarding operations. When set to 0, the switch operates in unmanaged mode, where forwarding state is maintained autonomously by internal hardware logic without software intervention."






class openenoc_switch_interface_forwarding_control_pause_request_0x3fca318d6d37e18_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_control.pause_request[7:7]         |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Pause request for the forwarding logic. When set, this field    |
    |              |      requests the switch to pause frame forwarding and clear its        |
    |              |      internal pipeline before forwarding table updates are              |
    |              |      performed.</p>                                                     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_control.pause_request[7:7]"
    @property
    def rdl_desc(self) -> str:
        return "Pause request for the forwarding logic. When set, this field requests the switch to pause frame forwarding and clear its internal pipeline before forwarding table updates are performed."






class openenoc_switch_interface_forwarding_control_pause_done_neg_0x696e866563f40182_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_control.pause_done[15:15]          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Pause done status. When set, this field indicates that the      |
    |              |      switch has paused frame forwarding and reached a safe state for    |
    |              |      forwarding table modification.</p>                                 |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_control.pause_done[15:15]"
    @property
    def rdl_desc(self) -> str:
        return "Pause done status. When set, this field indicates that the switch has paused frame forwarding and reached a safe state for forwarding table modification."






class openenoc_switch_interface_default_forwarding_bitmap_neg_0x7ddef3e68c368f37_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.default_forwarding.bitmap[NUM_OF_INTERFACES-  |
    |              |      1:0]                                                               |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Bitmap selecting the output interface or interfaces to which    |
    |              |      frames that do not match any enabled forwarding table entry are    |
    |              |      forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the    |
    |              |      first interface; bit 0 corresponds to the last interface.</p>      |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.default_forwarding.bitmap[NUM_OF_INTERFACES-1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Bitmap selecting the output interface or interfaces to which frames that do not match any enabled forwarding table entry are forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface."






class openenoc_switch_interface_forwarding_table_entry_mac_address_lo_word_neg_0x1a55655eb47a453c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
    |              |      1].mac_address.lo_word[31:0]                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address stored in this   |
    |              |      forwarding table entry.</p>                                        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address stored in this forwarding table entry."






class openenoc_switch_interface_forwarding_table_entry_mac_address_hi_word_0x71157053d1016d34_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
    |              |      1].mac_address.hi_word[47:32]                                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address stored in this  |
    |              |      forwarding table entry.</p>                                        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address stored in this forwarding table entry."






class openenoc_switch_interface_forwarding_table_entry_iface_bitmap_0x627b1bb55fa275b2_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
    |              |      1].iface.bitmap[NUM_OF_INTERFACES-1:0]                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Bitmap selecting the output interface or interfaces to which a  |
    |              |      matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB,     |
    |              |      corresponds to the first interface; bit 0 corresponds to the last  |
    |              |      interface.</p>                                                     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].iface.bitmap[NUM_OF_INTERFACES-1:0]"
    @property
    def rdl_desc(self) -> str:
        return "Bitmap selecting the output interface or interfaces to which a matching frame is forwarded. Bit NUM_OF_INTERFACES-1, the MSB, corresponds to the first interface; bit 0 corresponds to the last interface."






class openenoc_switch_interface_forwarding_table_entry_config_enabled_0xd904eaff2d4a80d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-        |
    |              |      1].config.enabled                                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Enables this forwarding table entry. When cleared, the entry is |
    |              |      ignored during forwarding table lookup.</p>                        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.switch_interface.forwarding_table.entry[0..TABLE_DEPTH-1].config.enabled"
    @property
    def rdl_desc(self) -> str:
        return "Enables this forwarding table entry. When cleared, the entry is ignored during forwarding table lookup."





if __name__ == '__main__':
    pass