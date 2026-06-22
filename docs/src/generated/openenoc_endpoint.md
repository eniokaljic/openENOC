<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openenoc_endpoint
  - /home/enio/Projects/openENOC/hal/src/openenoc.rdl
-->

## openenoc_endpoint address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x800

<p>Control and status register map for an openENOC Endpoint Interface instance.</p>

|Offset|Identifier|         Name         |
|------|----------|----------------------|
| 0x000|   info   |openenoc_endpoint.info|
| 0x400|   rmem   |         rmem         |

### info register

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x4

<p>Read-only information register for this openENOC Endpoint Interface instance.</p>

|Bits| Identifier|Access|Reset|                  Name                  |
|----|-----------|------|-----|----------------------------------------|
|31:0|placeholder|   r  |  —  |openenoc_endpoint.info.placeholder[31:0]|

#### placeholder field

<p>Placeholder field for this openENOC Endpoint Interface instance.</p>

## rmem memory

- Absolute Address: 0x400
- Base Offset: 0x400
- Size: 0x400

<p>Remote Memory</p>

No supported members.

