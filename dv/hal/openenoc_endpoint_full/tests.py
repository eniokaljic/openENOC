# SPDX-FileCopyrightText: 2026 Enio Kaljic
# SPDX-License-Identifier: AGPL-3.0-or-later


def test1(csr):
    csr.test_reg.test_field.write(123)
    assert csr.test_reg.test_field.read() == 123


def test2(csr):
    csr.regB.f0.write(45)
    assert csr.regB.f0.read() == 45

    csr.regB.f1.write(67)
    assert csr.regB.f1.read() == 67

    assert csr.regB.f2.read() == 0

    assert csr.regB.f3.read() == 0


def test_rmem_timeout_cycles(csr):
    config = csr.endpoint_interface.config
    assert config.rmem_timeout.cycles.read() == 0
    for cycles in [1, 1024, 0xA5A55A5A, 0xFFFFFFFF, 0]:
        config.rmem_timeout.cycles.write(cycles)
        assert config.rmem_timeout.cycles.read() == cycles
        assert config.non_oetp_control.receive_mode.read() == 1
        assert config.mac_address.lo_word.read() == 0
        assert config.mac_address.hi_word.read() == 0
        assert config.multicast_address.lo_word.read() == 0
        assert config.multicast_address.hi_word.read() == 0
        assert config.dma_timeout.cycles.read() == 0


def test_config_mac_and_timeouts(csr):
    config = csr.endpoint_interface.config
    assert config.multicast_address.read() == 0
    assert config.dma_timeout.cycles.read() == 0

    config.mac_address.write(0x020E0C000001)
    config.multicast_address.write(0x030E0C000010)
    config.non_oetp_control.receive_mode.write(2)
    config.rmem_timeout.cycles.write(1024)

    for cycles in [1, 0xA5A55A5A, 0xFFFFFFFF, 0]:
        config.dma_timeout.cycles.write(cycles)
        assert config.dma_timeout.cycles.read() == cycles
        assert config.rmem_timeout.cycles.read() == 1024
        assert config.mac_address.read() == 0x020E0C000001
        assert config.multicast_address.read() == 0x030E0C000010
        assert config.non_oetp_control.receive_mode.read() == 2

    config.multicast_address.write(0xFFFFFFFFFFFF)
    assert config.multicast_address.read() == 0xFFFFFFFFFFFF
    config.multicast_address.write(0)
    assert config.multicast_address.read() == 0
    assert config.mac_address.read() == 0x020E0C000001
    assert config.rmem_timeout.cycles.read() == 1024

    config.mac_address.write(0x020E0C000002)
    assert config.mac_address.read() == 0x020E0C000002
    assert config.multicast_address.read() == 0

    for peer in csr.endpoint_interface.peers.entry:
        assert peer.dma.error.read() == 0
        assert peer.dma.error_code.read() == 0
        assert peer.dma.clear_error.read() == 0
    irq = csr.endpoint_interface.irq
    irq.event_enable.rmem_error.write(1)
    assert irq.event_enable.rmem_error.read() == 1
    assert irq.event_enable.peer_dma_complete.read() == 0
    irq.event_enable.rmem_error.write(0)
    assert irq.event_enable.rmem_error.read() == 0


def test_dma_max_fragment_size_bytes(csr):
    endpoint = csr.endpoint_interface
    config = endpoint.config
    register = config.dma_max_fragment_size
    maximum = ((endpoint.info.max_dma_frame_size_bytes.read() - 32) // 4) * 4
    assert maximum == 8160
    assert register.bytes.read() == maximum
    assert register.address == config.dma_timeout.address + 4
    config.dma_timeout.cycles.write(0x12345678)
    endpoint.axis_if.source.data.tdata.write(0xA5A55A5A)
    for value in (
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        31,
        1480,
        maximum,
        maximum + 1,
        maximum + 3,
        maximum + 4,
        0xFFFFFFFF,
    ):
        register.bytes.write(value)
        assert register.bytes.read() == value
        assert config.dma_timeout.cycles.read() == 0x12345678
        assert endpoint.axis_if.source.data.tdata.read() == 0xA5A55A5A
    register.bytes.write(maximum)
