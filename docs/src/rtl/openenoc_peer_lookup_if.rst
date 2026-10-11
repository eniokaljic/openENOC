.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-peer-lookup-if:

Endpoint peer lookup -- openenoc_peer_lookup_if
===============================================

Defines peer queries and coherent configuration responses for endpoint clients.

**Source:** :download:`openenoc_peer_lookup_if.sv <../../../hw/rtl/core/openenoc_peer_lookup_if.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 30 18 22 30

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``NUM_OF_PEERS``
     - ``4``
     - Integer >= 1; match generated CSR array
     - Number of peer-table entries.
   * - ``PEER_IDX_W``
     - ``NUM_OF_PEERS > 1 ? $clog2( NUM_OF_PEERS ) : 1``
     - Integer >= 1; enough bits for the peer count
     - Width of local peer indices; all connected interfaces must agree.
   * - ``ADDR_W``
     - ``32``
     - Integer >= 1
     - Byte-address width in bits; connected interfaces must agree.

Signals
-------

Directions are relative to the named modport. The monitor modport, where
present, observes signals as inputs and does not drive them.

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 26 27 17 30

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``req_valid``
     - ``logic``
     - mst: output; slv: input
     - Request fields are valid and retained until accepted.
   * - ``req_ready``
     - ``logic``
     - mst: input; slv: output
     - Executor accepts the request on this handshake.
   * - ``req_type``
     - ``logic [1:0]``
     - mst: output; slv: input
     - Lookup kind: index, RMEM address, or MAC address.
   * - ``req_mode_mask``
     - ``logic [3:0]``
     - mst: output; slv: input
     - Eligible DMA-mode bitmap; zero permits no entry.
   * - ``req_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - mst: output; slv: input
     - Local peer entry associated with the transaction.
   * - ``req_rmem_addr``
     - ``logic [ADDR_W-1:0]``
     - mst: output; slv: input
     - Scalar memory address to resolve.
   * - ``req_mac_addr``
     - ``logic [47:0]``
     - mst: output; slv: input
     - Source/destination MAC address to resolve.
   * - ``rsp_valid``
     - ``logic``
     - mst: input; slv: output
     - Response snapshot is valid and retained until accepted.
   * - ``rsp_ready``
     - ``logic``
     - mst: output; slv: input
     - Client accepts the response.
   * - ``rsp_hit``
     - ``logic``
     - mst: input; slv: output
     - An eligible peer entry matched.
   * - ``rsp_peer_idx``
     - ``logic [PEER_IDX_W-1:0]``
     - mst: input; slv: output
     - Matched peer entry index; zero on a miss.
   * - ``rsp_mac_addr``
     - ``logic [47:0]``
     - mst: input; slv: output
     - Matched peer MAC address.
   * - ``rsp_rmem_offset``
     - ``logic [ADDR_W-1:0]``
     - mst: input; slv: output
     - Matched virtual scalar-memory base/offset.
   * - ``rsp_local_addr``
     - ``logic [ADDR_W-1:0]``
     - mst: input; slv: output
     - Matched local memory-window base.
   * - ``rsp_remote_addr``
     - ``logic [ADDR_W-1:0]``
     - mst: input; slv: output
     - Matched remote memory-window base.
   * - ``rsp_size``
     - ``logic [ADDR_W-1:0]``
     - mst: input; slv: output
     - Matched memory-window size in bytes.
   * - ``rsp_dma_mode``
     - ``logic [1:0]``
     - mst: input; slv: output
     - Matched peer mode: disabled, RMEM, mirror-to-remote, or mirror-to-local.
   * - ``rsp_irq_enable``
     - ``logic``
     - mst: input; slv: output
     - Matched peer DMA event-enable setting.

Architecture and operation
--------------------------

**Parameters and roles:** ``NUM_OF_PEERS`` defaults to 4; ``PEER_IDX_W`` is
derived with a minimum of one bit; ``ADDR_W`` defaults to 32. Modports are
``mst``, ``slv``, and ``mon``.

Request and response channels use independent ready/valid handshakes. Keep
request fields stable while ``req_valid && !req_ready``, and response fields
stable while ``rsp_valid && !rsp_ready``. The interface permits both the
current registered CAM lookup and implementations with longer latency.

``req_type`` selects ``LOOKUP_BY_INDEX`` (0), ``LOOKUP_BY_RMEM`` (1), or
``LOOKUP_BY_MAC`` (2). Only the selected key, respectively ``req_peer_idx``,
``req_rmem_addr``, or ``req_mac_addr``, is meaningful. ``req_mode_mask[n]``
permits entries whose ``dma.mode`` is n. A zero mask matches nothing; callers
normally leave bit zero clear, and the current lookup block also excludes
disabled entries.

The response is a coherent snapshot: ``rsp_hit``, ``rsp_peer_idx``,
``rsp_mac_addr``, ``rsp_rmem_offset``, ``rsp_local_addr``, ``rsp_remote_addr``,
``rsp_size``, ``rsp_dma_mode``, and ``rsp_irq_enable``. Entry fields are zero
on a miss. The implementation is :ref:`rtl-endpoint-peer-lookup`.

Functional scenarios
--------------------

This section reserves space for scenario descriptions and WaveDrom timing
diagrams. The current outline is:

* Query by peer index, scalar address, or MAC address.
* Mode-filtered hit and deterministic miss response.
* Request/response backpressure and snapshot retention.
