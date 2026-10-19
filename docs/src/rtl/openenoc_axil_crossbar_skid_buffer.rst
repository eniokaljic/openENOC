.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-axil-crossbar-skid-buffer:

Crossbar elastic buffer -- openenoc_axil_crossbar_skid_buffer
=============================================================

.. index::
   single: openenoc_axil_crossbar_skid_buffer

Provides an elastic pipeline boundary that absorbs delayed downstream
backpressure.

**Source:** :download:`openenoc_axil_crossbar_skid_buffer.sv <../../../hw/rtl/core/openenoc_axil_crossbar_skid_buffer.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 14 18 20 48

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``DATA_W``
     - ``1``
     - Integer >= 1
     - Packed channel payload width in bits.

Signals
-------

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 14 24 17 45

   * - Name
     - Type
     - Direction / role
     - Description
   * - ``clk``
     - ``logic``
     - input
     - Clock for this component or interface domain.
   * - ``rst``
     - ``logic``
     - input
     - Active-high synchronous reset of VALID and READY state.
   * - ``s_data``
     - ``logic [DATA_W-1:0]``
     - input
     - Packed upstream payload.
   * - ``s_valid``
     - ``logic``
     - input
     - Upstream payload is valid.
   * - ``s_ready``
     - ``logic``
     - output
     - Registered upstream acceptance indication.
   * - ``m_data``
     - ``logic [DATA_W-1:0]``
     - output
     - Packed downstream payload.
   * - ``m_valid``
     - ``logic``
     - output
     - Downstream payload is valid.
   * - ``m_ready``
     - ``logic``
     - input
     - Downstream acceptance indication.

Architecture and operation
--------------------------

This two-entry elastic register slice stores packed AXI4-Lite channel payloads
of ``DATA_W`` bits. The output payload and VALID, and the upstream READY,
are registered. With continuous readiness, a payload accepted in one interval
is presented downstream in the next, and both sides can transfer once per
cycle after the initial fill. Only VALID qualifies the payload.

When downstream READY falls, the already registered upstream READY can still
accept one more payload. The second entry retains it while the output entry
holds its older payload stable. Upstream READY then falls to prevent overflow.
When downstream consumption resumes, the two stored entries can drain on
consecutive edges. Upstream acceptance resumes after READY has been registered
high again; the stored second entry covers that recovery interval.

Reset synchronously clears both VALID states and upstream READY. Payload
registers are not cleared. Buffered transfers are discarded at the reset edge;
the producer must coordinate reset rather than replaying an aborted transfer
implicitly. After reset release, one edge is needed to restore READY.

Functional scenarios
--------------------

The examples use ``DATA_W = 32`` and symbolic payloads ``D0``, ``D1``, ... .
A numbered tick is an interval ending at a rising sampling edge. Transfers
occur when the corresponding VALID and READY are high. ``x`` marks payloads
without VALID. Source payload and VALID remain stable while awaiting READY.

Startup and continuous transfers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

RST is high in ticks 0 and 1. The source offers ``D0`` from tick 2, after
reset is released. READY is still low in tick 2 and becomes high in tick 3.
The source then transfers ``D0`` through ``D3`` in ticks 3 through 6.
The downstream side transfers them in ticks 4 through 7, one per cycle.

.. wavedrom::
    :name: memory-skid-flow-timing
    :caption: Registered readiness recovers after reset before continuous transfers
    :alt: Registered readiness recovers after reset before continuous transfers.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            {"name": "rst", "wave": "1.0......."},
            {"name": "s_valid", "wave": "0.1....0.."},
            {"name": "s_data", "wave": "x.=.===x..", "data": ["D0", "D1", "D2", "D3"]},
            {"name": "s_ready", "wave": "0..1......"},
            {},
            {"name": "m_valid", "wave": "0...1...0."},
            {"name": "m_data", "wave": "x...====x.", "data": ["D0", "D1", "D2", "D3"]},
            {"name": "m_ready", "wave": "1........."},
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

The second entry absorbs delayed backpressure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The source offers six payloads, ``D0`` through ``D5``. Downstream READY is
low in ticks 3 through 5. ``D0`` has already transferred downstream in
tick 2; ``D1`` is held at the output in ticks 3 through 6. The source can
still transfer ``D2`` in tick 3 before its registered READY falls.

``D3`` waits at the input in ticks 4 through 6. When downstream READY rises
in tick 6, ``D1`` transfers but upstream READY is still low. ``D2`` follows
in tick 7 while the source finally transfers ``D3``. Output transfers then
continue through ``D5`` in tick 10 without another gap.

.. wavedrom::
    :name: memory-skid-stall-timing
    :caption: The second entry absorbs a transfer before upstream READY falls
    :alt: The second entry absorbs a transfer before upstream READY falls.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p..........."},
            {"name": "rst", "wave": "0..........."},
            {"name": "s_valid", "wave": "01........0."},
            {"name": "s_data", "wave": "x====...==x.", "data": ["D0", "D1", "D2", "D3", "D4", "D5"]},
            {"name": "s_ready", "wave": "1...0..1...."},
            {},
            {"name": "m_valid", "wave": "0.1........0"},
            {"name": "m_data", "wave": "x.==...====x", "data": ["D0", "D1", "D2", "D3", "D4", "D5"]},
            {"name": "m_ready", "wave": "1..0..1....."},
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Reset discards both retained payloads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With downstream READY low, the buffer accepts ``D0`` and ``D1`` in ticks
1 and 2. RST is asserted in ticks 3 and 4. The held output VALID is still
visible in tick 3 and clears at that interval's ending edge. Neither stored
payload is delivered after reset.

The source offers new payload ``D2`` from tick 5 after reset release.
READY recovers in tick 6, and ``D2`` transfers downstream in tick 7.

.. wavedrom::
    :name: memory-skid-reset-timing
    :caption: Reset discards held payloads and accepts new data after READY recovers
    :alt: Reset discards held payloads and accepts new data after READY recovers.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            {"name": "rst", "wave": "0..1.0...."},
            {"name": "s_valid", "wave": "01.0.1.0.."},
            {"name": "s_data", "wave": "x==x.=.x..", "data": ["D0", "D1", "D2"]},
            {"name": "s_ready", "wave": "1..0..1..."},
            {},
            {"name": "m_valid", "wave": "0.1.0..10."},
            {"name": "m_data", "wave": "x.=.x..=x.", "data": ["D0", "D2"]},
            {"name": "m_ready", "wave": "0....1...."},
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }
