.. SPDX-FileCopyrightText: 2026 Enio Kaljic
.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _rtl-rr-arbiter:

Round-robin arbiter -- openenoc_rr_arbiter
==========================================

.. index::
   single: openenoc_rr_arbiter

Selects requesting clients fairly using a rotating priority pointer.

**Source:** :download:`openenoc_rr_arbiter.sv <../../../hw/rtl/core/openenoc_rr_arbiter.sv>`.

Parameters
----------

.. list-table:: Parameters
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 14 22 22 42

   * - Name
     - Default value
     - Allowed values
     - Description
   * - ``PORTS``
     - ``2``
     - Integer >= 1
     - Number of round-robin requesters.
   * - ``INDEX_W``
     - ``PORTS > 1 ? $clog2(PORTS) : 1``
     - >= max(1, ceil(log2(PORTS)))
     - Width of the winning requester index.

Signals
-------

.. list-table:: Public signals and interfaces
   :class: rtl-reference-table
   :header-rows: 1
   :widths: 18 26 17 39

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
     - Active-high synchronous priority reset; combinational grants remain visible.
   * - ``request``
     - ``logic [PORTS-1:0]``
     - input
     - Active requester bitmap.
   * - ``accept``
     - ``logic``
     - input
     - Consumer accepts the current winning grant.
   * - ``grant``
     - ``logic [PORTS-1:0]``
     - output
     - One-hot winning requester bitmap.
   * - ``grant_valid``
     - ``logic``
     - output
     - At least one requester is selected.
   * - ``grant_index``
     - ``logic [INDEX_W-1:0]``
     - output
     - Index of the winning requester.

Architecture and operation
--------------------------

The arbiter selects combinationally from the live request bitmap, scanning
from a registered rotating priority and wrapping at ``PORTS``. ``grant``
is one-hot and ``grant_index`` is its encoded port number when
``grant_valid`` is high. An empty request vector produces zero grant and
low grant-valid; the index then reflects the retained starting priority
and must not be treated as a winner.

At a rising edge, ``accept && grant_valid`` advances priority to the port
after the accepted winner. No acceptance, or acceptance with no requester,
leaves it unchanged. Persistent requesters receive turns as grants are
accepted. ``PORTS`` need not be a power of two; wrapping uses its actual
value. ``INDEX_W`` must encode every port, with a minimum of one bit.

The selected grant is not retained under backpressure. Even with ACCEPT
low, changing the request vector can change the combinational winner.
An owner that needs a stable transaction selection must retain it at the
surrounding handshake boundary. The arbiter itself owns only rotating
priority, not transaction state.

RST synchronously resets priority to port 0 and overrides acceptance at
that edge. It does not mask the combinational grant, so requests can still
produce a grant while RST is high. Only grant-valid qualifies the index.

Functional scenarios
--------------------

The examples use ``PORTS = 3`` and ``INDEX_W = 2``. Bit 0 corresponds to port
0. Request and grant bitmaps use the ``0b`` prefix; the encoded grant index
is shown only with grant-valid. Ticks are intervals ending at rising
sampling edges. Reset has already been released except where shown.

Three-port rotation and wraparound
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All three ports request in ticks 1 through 7 and every grant is accepted.
Winners are 0, 1, 2, 0, 1, 2, 0, demonstrating wrap at three ports.
With no request from tick 8, grant-valid falls and ACCEPT cannot advance
priority by itself.

.. wavedrom::
    :name: memory-arbiter-rotate-timing
    :caption: Accepted grants rotate across three ports and wrap without a bubble
    :alt: Accepted grants rotate across three ports and wrap without a bubble.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p.........."},
            {"name": "rst", "wave": "0.........."},
            {"name": "request", "wave": "==......=..", "data": ["0b000", "0b111", "0b000"]},
            {"name": "accept", "wave": "01........."},
            {},
            {
                "name": "grant",
                "wave": "=========..",
                "data": ["0b000", "0b001", "0b010", "0b100", "0b001", "0b010", "0b100", "0b001", "0b000"]
            },
            {"name": "grant_valid", "wave": "01......0.."},
            {
                "name": "grant_index",
                "wave": "x=======x..",
                "data": ["0b00", "0b01", "0b10", "0b00", "0b01", "0b10", "0b00"]
            },
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

An unaccepted winner can change with the requests
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With priority initially at zero, request ``0b100`` selects port 2 in tick 1.
ACCEPT is low. Changing the bitmap to ``0b110`` in tick 2 changes the winner
to port 1 without a clocked acceptance. Port 1 is accepted in tick 3,
moving priority to port 2.

Port 2 wins with all ports requesting in tick 4. In tick 5, only port 0
requests and it wins even though ACCEPT remains low. When all request again
in tick 6, port 2 wins and is accepted. The empty vector in tick 7 leaves
priority at zero, so port 0 wins in tick 8.

.. wavedrom::
    :name: memory-arbiter-unaccepted-timing
    :caption: Live request changes can change a grant before acceptance
    :alt: Live request changes can change a grant before acceptance.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            {"name": "rst", "wave": "0........."},
            {
                "name": "request",
                "wave": "===.======",
                "data": ["0b000", "0b100", "0b110", "0b111", "0b001", "0b111", "0b000", "0b111", "0b000"]
            },
            {"name": "accept", "wave": "0..10.1..0"},
            {},
            {
                "name": "grant",
                "wave": "===.======",
                "data": ["0b000", "0b100", "0b010", "0b100", "0b001", "0b100", "0b000", "0b001", "0b000"]
            },
            {"name": "grant_valid", "wave": "01.....010"},
            {
                "name": "grant_index",
                "wave": "x==.===x=x",
                "data": ["0b10", "0b01", "0b10", "0b00", "0b10", "0b00"]
            },
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }

Synchronous reset changes priority without masking grant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Port 1 is accepted in tick 1, placing port 2 first in tick 2. RST rises in
tick 3 while every port requests; the combinational winner is still port 2.
The reset edge restores priority to zero, so port 0 wins in tick 4 even
though RST remains high. Reset overrides the ACCEPT asserted in tick 3.

After release, port 0 is accepted in tick 5. An empty vector in tick 6
does not advance priority. Port 2 can then win alone in tick 7 and wrap
priority to zero for the all-requesting tick 8.

.. wavedrom::
    :name: memory-arbiter-reset-timing
    :caption: Reset restores priority at the edge while combinational grants remain
    :alt: Reset restores priority at the edge while combinational grants remain.
    :align: center

    {
        "signal": [
            {"name": "clk", "wave": "p........."},
            {"name": "rst", "wave": "0..1.0...."},
            {
                "name": "request",
                "wave": "===...====",
                "data": ["0b000", "0b010", "0b111", "0b000", "0b100", "0b111", "0b000"]
            },
            {"name": "accept", "wave": "010101...0"},
            {},
            {
                "name": "grant",
                "wave": "===.=.====",
                "data": ["0b000", "0b010", "0b100", "0b001", "0b000", "0b100", "0b001", "0b000"]
            },
            {"name": "grant_valid", "wave": "01....01.0"},
            {
                "name": "grant_index",
                "wave": "x==.=.x==x",
                "data": ["0b01", "0b10", "0b00", "0b10", "0b00"]
            },
            {}
        ],
        "head": {"tick": 0},
        "config": {"hscale": 2}
    }
