

"""
Python Wrapper for the csr register model

This code was generated from the PeakRDL-python package version 3.1.2

"""









from ....lib import UDPStruct
from ....lib import FieldReadOnly, FieldWriteOnly, FieldReadWrite, Field


# field definitions


class openenoc_endpoint_interface_irq_event_enable_non_oetp_dma_rx_complete_0x6010eb6f58d7cb9d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.event_enable.non_oetp_dma_rx_complete   |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Enables NON_OETP_DMA_RX_COMPLETE events. Hardware samples this  |
    |              |      field when it accepts a non-oETP receive DMA request.</p>          |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.non_oetp_dma_rx_complete"
    @property
    def rdl_desc(self) -> str:
        return "Enables NON_OETP_DMA_RX_COMPLETE events. Hardware samples this field when\nit accepts a non-oETP receive DMA request."






class openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_tx_complete_neg_0x4932758f41036931_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.event_enable.non_oetp_direct_tx_complet |
    |              |      e                                                                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Enables NON_OETP_DIRECT_TX_COMPLETE events. Hardware samples    |
    |              |      this field when the first beat of a direct transmit frame is       |
    |              |      accepted from the CSR-facing AXI4-Stream interface. When enabled,  |
    |              |      the frame start is accepted only after an IRQ FIFO credit has been |
    |              |      reserved. The event is generated when the final beat is accepted   |
    |              |      by the oETP engine.</p>                                            |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.non_oetp_direct_tx_complete"
    @property
    def rdl_desc(self) -> str:
        return "Enables NON_OETP_DIRECT_TX_COMPLETE events. Hardware samples this field when\nthe first beat of a direct transmit frame is accepted from the CSR-facing\nAXI4-Stream interface. When enabled, the frame start is accepted only after an\nIRQ FIFO credit has been reserved. The event is generated when the final beat\nis accepted by the oETP engine."






class openenoc_endpoint_interface_irq_event_enable_non_oetp_direct_rx_available_neg_0x242e0dcdd48d0d6d_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.event_enable.non_oetp_direct_rx_availab |
    |              |      le                                                                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Enables NON_OETP_DIRECT_RX_AVAILABLE events. One event is       |
    |              |      generated when the first beat of a new direct receive frame        |
    |              |      becomes valid on the CSR-facing AXI4-Stream interface. When        |
    |              |      enabled, routing logic does not expose that first TVALID until an  |
    |              |      IRQ FIFO credit is available, so the event cannot be lost. The     |
    |              |      event does not depend on TLAST and therefore supports both cut-    |
    |              |      through and frame-FIFO operation.</p>                              |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.non_oetp_direct_rx_available"
    @property
    def rdl_desc(self) -> str:
        return "Enables NON_OETP_DIRECT_RX_AVAILABLE events. One event is generated when\nthe first beat of a new direct receive frame becomes valid on the CSR-facing\nAXI4-Stream interface. When enabled, routing logic does not expose that first\nTVALID until an IRQ FIFO credit is available, so the event cannot be lost.\nThe event does not depend on TLAST and therefore supports both cut-through and\nframe-FIFO operation."






class openenoc_endpoint_interface_irq_event_enable_rmem_error_neg_0xd42a525ded0713e_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.event_enable.rmem_error                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Enables RMEM_ERROR events for locally initiated RMEM failures,  |
    |              |      including timeout and an accepted ERROR_RSP, and failed incoming   |
    |              |      RMEM requests from a resolved peer. Hardware records the           |
    |              |      associated peer's dma.error and dma.error_code before exposing the |
    |              |      event and terminates the failed RMEM access without waiting for    |
    |              |      IRQ FIFO capacity. For locally initiated failures the enable is    |
    |              |      sampled when the failure is recorded; incoming failures sample it  |
    |              |      at IRQ admission. The bulk DMA per-peer irq_enable does not gate   |
    |              |      RMEM_ERROR. Successful RMEM accesses generate no event.</p>        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.event_enable.rmem_error"
    @property
    def rdl_desc(self) -> str:
        return "Enables RMEM_ERROR events for locally initiated RMEM failures, including\ntimeout and an accepted ERROR_RSP, and failed incoming RMEM requests from a\nresolved peer. Hardware records the associated peer\u0027s\ndma.error and dma.error_code before\nexposing the event and terminates the failed RMEM access without waiting\nfor IRQ FIFO capacity. For locally initiated failures the enable is sampled\nwhen the failure is recorded; incoming failures sample it at IRQ admission.\nThe bulk DMA per-peer irq_enable does not gate RMEM_ERROR.\nSuccessful RMEM accesses generate no event."






class openenoc_endpoint_interface_irq_status_claim_pending_neg_0x1a89fec29eb2077a_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.status.claim_pending                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates that at least one valid event is available in         |
    |              |      irq.claim.</p>                                                     |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.claim_pending"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that at least one valid event is available in irq.claim."






class openenoc_endpoint_interface_irq_status_credit_full_neg_0x64dc71f18f165161_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.status.credit_full                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates that all event FIFO credits are occupied by queued    |
    |              |      claims or reserved for admitted operations. While no credit is     |
    |              |      available, new interrupt-enabled DMA requests are not accepted and |
    |              |      the start of an interrupt-enabled direct AXI4-Stream frame is      |
    |              |      backpressured.</p>                                                 |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.credit_full"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that all event FIFO credits are occupied by queued claims or\nreserved for admitted operations. While no credit is available, new\ninterrupt-enabled DMA requests are not accepted and the start of an\ninterrupt-enabled direct AXI4-Stream frame is backpressured."






class openenoc_endpoint_interface_irq_status_overflow_neg_0x1cf2e3e20d3f23cc_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.status.overflow                         |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sticky internal-error flag indicating that an enabled event     |
    |              |      could not be retained. Correct credit reservation, admission       |
    |              |      control, and AXI4-Stream backpressure make this condition          |
    |              |      unreachable during normal operation. Clear with                    |
    |              |      irq.control.clear_errors.</p>                                      |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.overflow"
    @property
    def rdl_desc(self) -> str:
        return "Sticky internal-error flag indicating that an enabled event could not be\nretained. Correct credit reservation, admission control, and AXI4-Stream\nbackpressure make this condition unreachable during normal operation. Clear with\nirq.control.clear_errors."






class openenoc_endpoint_interface_irq_status_invalid_complete_neg_0x29ba81e00710d8b1_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.status.invalid_complete                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sticky protocol-error flag indicating that irq.complete.valid   |
    |              |      was accepted while no claim was pending or that the completion     |
    |              |      token did not match the current claim. No claim is removed on a    |
    |              |      mismatch. Clear with irq.control.clear_errors.</p>                 |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.invalid_complete"
    @property
    def rdl_desc(self) -> str:
        return "Sticky protocol-error flag indicating that irq.complete.valid was accepted\nwhile no claim was pending or that the completion token did not match the\ncurrent claim. No claim is removed on a mismatch. Clear with\nirq.control.clear_errors."






class openenoc_endpoint_interface_irq_status_irq_asserted_neg_0x51b7d031f64acc37_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.status.irq_asserted                     |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Reflects the current value of the physical endpoint IRQ output  |
    |              |      after application of irq.control.global_enable.</p>                |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.irq_asserted"
    @property
    def rdl_desc(self) -> str:
        return "Reflects the current value of the physical endpoint IRQ output after\napplication of irq.control.global_enable."






class openenoc_endpoint_interface_irq_status_fifo_level_0x226d3ad9bb8e03e4_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.status.fifo_level[7:0]                  |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number of valid claims currently queued in the IRQ event FIFO.  |
    |              |      Values greater than 255 are reported as 255.</p>                   |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.fifo_level[7:0]"
    @property
    def rdl_desc(self) -> str:
        return "Number of valid claims currently queued in the IRQ event FIFO. Values\ngreater than 255 are reported as 255."






class openenoc_endpoint_interface_irq_status_reserved_count_0x460123819538551a_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.status.reserved_count[7:0]              |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Number of event FIFO credits reserved for admitted DMA          |
    |              |      operations or direct transmit frames whose events have not yet     |
    |              |      been queued. Values greater than 255 are reported as 255.</p>      |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.status.reserved_count[7:0]"
    @property
    def rdl_desc(self) -> str:
        return "Number of event FIFO credits reserved for admitted DMA operations or direct\ntransmit frames whose events have not yet been queued. Values greater than 255\nare reported as 255."






class openenoc_endpoint_interface_irq_claim_peer_idx_neg_0x4f359d25dd9f3a5f_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.claim.peer_idx[10:0]                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Zero-based peer index for a PEER_DMA_COMPLETE or RMEM_ERROR     |
    |              |      event, in the range 0 through NUM_OF_PEERS-1. The field is not     |
    |              |      applicable to other event sources and is driven to zero for        |
    |              |      deterministic readback.</p>                                        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim.peer_idx[10:0]"
    @property
    def rdl_desc(self) -> str:
        return "Zero-based peer index for a PEER_DMA_COMPLETE or RMEM_ERROR event, in the range 0 through\nNUM_OF_PEERS-1. The field is not applicable to other event sources and is driven\nto zero for deterministic readback."






class openenoc_endpoint_interface_irq_claim_source_0x3d5467fc226424d6_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.claim.source[3:0]                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>IRQ event source:<ul></p> <li>0: PEER_DMA_COMPLETE. A peer DMA  |
    |              |      request completed with either success or error; peer_idx           |
    |              |      identifies the peer.</li> <li>1: NON_OETP_DMA_TX_COMPLETE. A non-  |
    |              |      oETP transmit DMA request completed with either success or         |
    |              |      error.</li> <li>2: NON_OETP_DMA_RX_COMPLETE. A non-oETP receive    |
    |              |      DMA request completed with either success or error.</li> <li>3:    |
    |              |      NON_OETP_DIRECT_TX_COMPLETE. The final beat of a direct non-oETP   |
    |              |      transmit frame was accepted by the oETP engine.</li> <li>4:        |
    |              |      NON_OETP_DIRECT_RX_AVAILABLE. The first beat of a new direct non-  |
    |              |      oETP receive frame is available on the CSR-facing AXI4-Stream      |
    |              |      interface.</li> <li>5: RMEM_ERROR. A locally initiated RMEM        |
    |              |      operation failed. The cause is recorded in                         |
    |              |      peers.entry[peer_idx].dma; peer_idx identifies the associated      |
    |              |      peer.</li> <li>6-15: Reserved.</li> <p></ul> This field is         |
    |              |      meaningful only when valid is set.</p>                             |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim.source[3:0]"
    @property
    def rdl_desc(self) -> str:
        return "IRQ event source:\u003cul\u003e\n\u003cli\u003e0: PEER_DMA_COMPLETE. A peer DMA request completed with either success or\nerror; peer_idx identifies the peer.\u003c/li\u003e\n\u003cli\u003e1: NON_OETP_DMA_TX_COMPLETE. A non-oETP transmit DMA request completed with\neither success or error.\u003c/li\u003e\n\u003cli\u003e2: NON_OETP_DMA_RX_COMPLETE. A non-oETP receive DMA request completed with\neither success or error.\u003c/li\u003e\n\u003cli\u003e3: NON_OETP_DIRECT_TX_COMPLETE. The final beat of a direct non-oETP transmit\nframe was accepted by the oETP engine.\u003c/li\u003e\n\u003cli\u003e4: NON_OETP_DIRECT_RX_AVAILABLE. The first beat of a new direct non-oETP\nreceive frame is available on the CSR-facing AXI4-Stream interface.\u003c/li\u003e\n\u003cli\u003e5: RMEM_ERROR. A locally initiated RMEM operation failed. The cause is\nrecorded in peers.entry[peer_idx].dma; peer_idx identifies the associated peer.\u003c/li\u003e\n\u003cli\u003e6-15: Reserved.\u003c/li\u003e\n\u003c/ul\u003e\nThis field is meaningful only when valid is set."






class openenoc_endpoint_interface_irq_claim_sequence_0x32fe5d47acab25d7_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.claim.sequence[15:0]                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Monotonically increasing event sequence number, modulo 65536.   |
    |              |      The sequence number distinguishes otherwise identical claims and   |
    |              |      protects against stale or repeated completion requests.</p>        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim.sequence[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Monotonically increasing event sequence number, modulo 65536. The sequence\nnumber distinguishes otherwise identical claims and protects against stale or\nrepeated completion requests."






class openenoc_endpoint_interface_irq_claim_valid_neg_0x6afdb5fd6cd7619b_cls(FieldReadOnly):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.claim.valid                             |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Indicates that this register contains the valid event at the    |
    |              |      head of the IRQ event FIFO. When clear, all other claim fields     |
    |              |      shall be ignored.</p>                                              |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.claim.valid"
    @property
    def rdl_desc(self) -> str:
        return "Indicates that this register contains the valid event at the head of the\nIRQ event FIFO. When clear, all other claim fields shall be ignored."






class openenoc_endpoint_interface_irq_complete_peer_idx_0x13061dca12f481cb_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.complete.peer_idx[10:0]                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Peer-index portion of the claim token.</p>                      |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete.peer_idx[10:0]"
    @property
    def rdl_desc(self) -> str:
        return "Peer-index portion of the claim token."






class openenoc_endpoint_interface_irq_complete_source_0x42454737ca14846c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.complete.source[3:0]                    |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Event-source portion of the claim token.</p>                    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete.source[3:0]"
    @property
    def rdl_desc(self) -> str:
        return "Event-source portion of the claim token."






class openenoc_endpoint_interface_irq_complete_sequence_0xbd1a53b104c3175_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.complete.sequence[15:0]                 |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Sequence-number portion of the claim token.</p>                 |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete.sequence[15:0]"
    @property
    def rdl_desc(self) -> str:
        return "Sequence-number portion of the claim token."






class openenoc_endpoint_interface_irq_complete_valid_neg_0x3bff197b75bcc364_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.irq.complete.valid                          |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Writing one submits the completion token. The field remains     |
    |              |      asserted until hardware validates the token and clears it. A       |
    |              |      matching token removes the current claim and releases its FIFO     |
    |              |      credit; an invalid token leaves the claim unchanged and sets       |
    |              |      irq.status.invalid_complete.</p>                                   |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.irq.complete.valid"
    @property
    def rdl_desc(self) -> str:
        return "Writing one submits the completion token. The field remains asserted until\nhardware validates the token and clears it. A matching token removes the current\nclaim and releases its FIFO credit; an invalid token leaves the claim unchanged\nand sets irq.status.invalid_complete."






class openenoc_endpoint_interface_peers_entry_mac_address_lo_word_0xe1c975d97202fd0_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].mac_address.lo_word[31:0]                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Lower 32 bits [31:0] of the 48-bit MAC address.</p>             |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.lo_word[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Lower 32 bits [31:0] of the 48-bit MAC address."






class openenoc_endpoint_interface_peers_entry_mac_address_hi_word_neg_0x4cc5274056686759_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].mac_address.hi_word[47:32]                                      |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Upper 16 bits [47:32] of the 48-bit MAC address.</p>            |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].mac_address.hi_word[47:32]"
    @property
    def rdl_desc(self) -> str:
        return "Upper 16 bits [47:32] of the 48-bit MAC address."






class openenoc_endpoint_interface_peers_entry_rmem_address_offset_neg_0x6b30420f4eda4c9c_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].rmem_address.offset[31:0]                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>32-bit byte offset of the virtual memory region corresponding   |
    |              |      to the remote peer's memory. The value shall be aligned to a       |
    |              |      32-bit word boundary.</p>                                          |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].rmem_address.offset[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit byte offset of the virtual memory region corresponding to the\nremote peer\u0027s memory. The value shall be aligned to a 32-bit word boundary."






class openenoc_endpoint_interface_peers_entry_local_address_base_neg_0x56ed9909ffe1ca58_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].local_address.base[31:0]                                        |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Word-aligned 32-bit start address of the local memory region    |
    |              |      for DMA transfers.</p>                                             |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].local_address.base[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Word-aligned 32-bit start address of the local memory region for\nDMA transfers."






class openenoc_endpoint_interface_peers_entry_remote_address_base_neg_0x23982d390e4b01f9_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].remote_address.base[31:0]                                       |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>Word-aligned 32-bit start address of the remote peer's memory   |
    |              |      region.</p>                                                        |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].remote_address.base[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "Word-aligned 32-bit start address of the remote peer\u0027s memory region."






class openenoc_endpoint_interface_peers_entry_size_bytes_0x1f61e557cbf457c3_cls(FieldReadWrite):
    """
    Class to represent a register field in the register model

    +--------------+-------------------------------------------------------------------------+
    | SystemRDL    | Value                                                                   |
    | Field        |                                                                         |
    +==============+=========================================================================+
    | Name         | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-                |
    |              |      1].size.bytes[31:0]                                                |
    +--------------+-------------------------------------------------------------------------+
    | Description  | .. raw:: html                                                           |
    |              |                                                                         |
    |              |      <p>32-bit size of the remote peer's memory region in bytes.</p>    |
    +--------------+-------------------------------------------------------------------------+
    """
    __slots__ : list[str] = []






    @property
    def rdl_name(self) -> str:
        return "csr.endpoint_interface.peers.entry[0..NUM_OF_PEERS-1].size.bytes[31:0]"
    @property
    def rdl_desc(self) -> str:
        return "32-bit size of the remote peer\u0027s memory region in bytes."





if __name__ == '__main__':
    pass