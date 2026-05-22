<!---
Markdown description for SystemRDL register map.

Don't override. Generated from: openENOC
  - src/openENOC.rdl
-->

## openENOC address map

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x20000008

|  Offset  |Identifier|Name|
|----------|----------|----|
|0x00000000|   imem   |imem|
|0x10000000|   dmem   |dmem|
|0x20000000|    csr   | csr|

## imem memory

- Absolute Address: 0x0
- Base Offset: 0x0
- Size: 0x8000

<p>CPU Program Memory</p>

No supported members.


## dmem memory

- Absolute Address: 0x10000000
- Base Offset: 0x10000000
- Size: 0x8000

<p>CPU Data Memory</p>

No supported members.


## csr address map

- Absolute Address: 0x20000000
- Base Offset: 0x20000000
- Size: 0x8

<p>openENOC CSR</p>

|Offset|Identifier|    Name    |
|------|----------|------------|
|  0x0 | test_reg |csr.test_reg|
|  0x4 |   regB   |      —     |

### test_reg register

- Absolute Address: 0x20000000
- Base Offset: 0x0
- Size: 0x4

<p>Test register</p>

|Bits|Identifier|Access|Reset|             Name            |
|----|----------|------|-----|-----------------------------|
|31:0|test_field|  rw  | 0x0 |csr.test_reg.test_field[31:0]|

#### test_field field

<p>4-byte test field</p>

### regB register

- Absolute Address: 0x20000004
- Base Offset: 0x4
- Size: 0x4

| Bits|Identifier|Access|Reset|Name|
|-----|----------|------|-----|----|
| 7:0 |    f0    |  rw  | 0x0 |  — |
| 15:8|    f1    |  rw  | 0x0 |  — |
|23:16|    f2    |  rw  | 0x0 |  — |
|31:24|    f3    |  rw  | 0x0 |  — |
