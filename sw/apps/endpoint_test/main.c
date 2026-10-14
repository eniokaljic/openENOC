/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <assert.h>
#include <stddef.h>
#include <stdint.h>

#include "csr.h"
#include "memory_map.h"
#include "openenoc_endpoint.h"

#define TEST_POLL_LIMIT 4096U
#define TEST_CONFIG UINT32_C(1)
#define TEST_PEER UINT32_C(2)
#define TEST_RMEM UINT32_C(4)
#define TEST_AXIS UINT32_C(8)
#define TEST_RAW_DMA UINT32_C(16)
#define TEST_PEER_DMA UINT32_C(32)
#define TEST_IRQ UINT32_C(64)
#define FRAME_WORDS 17U
#define FRAME_BYTES 66U

static volatile csr__endpoint_interface_t *endpoint;
static openenoc_endpoint_info_t endpoint_info;
static const openenoc_endpoint_mac_t local_mac = {{0x02, 0x0e, 0x0c, 0x00, 0x00, 0x01}};
#if CSR__HAS_PEER_DMA || CSR__HAS_RMEM
static const openenoc_endpoint_mac_t missing_mac = {{0x02, 0x0e, 0x0c, 0x00, 0x00, 0xfe}};
#endif
#if CSR__HAS_IRQ
static volatile bool irq_error;
static volatile uint32_t event_count[6];
#endif

#if CSR__HAS_DIRECT_AXIS || CSR__HAS_NON_OETP_DMA
static const uint32_t frame_words[FRAME_WORDS] = {
    UINT32_C(0xffffffff), UINT32_C(0x0122ffff), UINT32_C(0x89abcdef),
    UINT32_C(0xffffffff), UINT32_C(0xa5a55a5a), UINT32_C(0x5a5aa5a5),
    UINT32_C(0x00000001), UINT32_C(0x80000000), UINT32_C(0x11111111),
    UINT32_C(0x22222222), UINT32_C(0x33333333), UINT32_C(0x44444444),
    UINT32_C(0xdeadbeef), UINT32_C(0xc001d00d), UINT32_C(0x13579bdf),
    UINT32_C(0x2468ace0), UINT32_C(0x0000beef),
};
#endif

#if CSR__HAS_DIRECT_AXIS
_Alignas(4) static uint8_t axis_tx_bytes[FRAME_BYTES + 8U];
_Alignas(4) static uint8_t axis_rx_bytes[FRAME_BYTES + 8U];
static uint8_t *volatile axis_receive_buffer;
static volatile uint32_t axis_receive_capacity;
static volatile uint32_t axis_received_bytes;
static volatile openenoc_endpoint_status_t axis_receive_status;
static volatile bool axis_frame_received;

static void receive_axis_frame(void) {
    uint32_t received;

    axis_receive_status = openenoc_endpoint_axis_receive_stream(endpoint,
        axis_receive_buffer, axis_receive_capacity, &received);
    axis_received_bytes = received;
    axis_frame_received = true;
}
#endif

#if CSR__HAS_IRQ
static void handle_event(volatile csr__endpoint_interface_t *device,
    const openenoc_endpoint_irq_claim_t *claim, void *context) {
    (void)device;
    (void)context;
    if ((unsigned int)claim->source >= 6U) {
        irq_error = true;
        return;
    }
    ++event_count[claim->source];
#if CSR__HAS_DIRECT_AXIS
    if (claim->source == OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_RX_AVAILABLE) {
        receive_axis_frame();
    }
#endif
}

static void handle_irq_error(openenoc_endpoint_irq_result_t result, void *context) {
    (void)result;
    (void)context;
    irq_error = true;
}

static const openenoc_endpoint_irq_callbacks_t callbacks = {
    .peer_dma_complete = handle_event,
    .non_oetp_dma_tx_complete = handle_event,
    .non_oetp_dma_rx_complete = handle_event,
    .non_oetp_direct_tx_complete = handle_event,
    .non_oetp_direct_rx_available = handle_event,
    .rmem_error = handle_event,
    .error = handle_irq_error,
};

#if CSR__HAS_PEER_DMA || CSR__HAS_NON_OETP_DMA || CSR__HAS_DIRECT_AXIS || CSR__HAS_RMEM
static void wait_for_irq_events(openenoc_endpoint_irq_source_t source, uint32_t expected) {
    for (uint32_t poll = 0; poll < TEST_POLL_LIMIT; ++poll) {
        if (event_count[source] >= expected || irq_error) {
            break;
        }
    }
    assert(!irq_error && event_count[source] == expected);
}
#endif

static void test_irq_configuration_and_empty_claim(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_irq_config_t config = {
        .global_enable = true,
        .peer_dma_complete = CSR__HAS_PEER_DMA != 0U,
        .non_oetp_dma_tx_complete = CSR__HAS_NON_OETP_DMA != 0U,
        .non_oetp_dma_rx_complete = CSR__HAS_NON_OETP_DMA != 0U,
        .non_oetp_direct_tx_complete = CSR__HAS_DIRECT_AXIS != 0U,
        .non_oetp_direct_rx_available = CSR__HAS_DIRECT_AXIS != 0U,
        .rmem_error = CSR__HAS_RMEM != 0U,
    };
    openenoc_endpoint_irq_claim_t claim;

    result = openenoc_endpoint_irq_bind(endpoint, &callbacks);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_irq_set_config(endpoint, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_irq_get_claim(endpoint, &claim);
    assert(result == OPENENOC_ENDPOINT_STATUS_NOT_READY);
    result = openenoc_endpoint_irq_complete(endpoint);
    assert(result == OPENENOC_ENDPOINT_STATUS_NOT_READY);
}

static void test_irq_error_clear_preserves_global_enable(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_irq_config_t config;

    result = openenoc_endpoint_irq_clear_errors(endpoint);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_irq_get_config(endpoint, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(config.global_enable);
}

static void test_irq_controller_idle_after_transfers(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_irq_status_t status;

    result = openenoc_endpoint_irq_set_global_enable(endpoint, false);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_irq_get_status(endpoint, &status);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(!irq_error && !status.overflow && !status.invalid_complete &&
        !status.claim_pending && status.reserved_count == 0U);
    result = openenoc_endpoint_irq_bind(NULL, NULL);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
}
#endif

static void test_endpoint_initialization(void) {
    openenoc_endpoint_status_t result __attribute__((unused));

    result = openenoc_endpoint_init(endpoint);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
}

static void test_endpoint_information(void) {
    openenoc_endpoint_status_t result __attribute__((unused));

    result = openenoc_endpoint_get_info(endpoint, &endpoint_info);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(endpoint_info.peer_count == CSR__NUM_OF_PEERS);
    assert(endpoint_info.rmem_word_count == CSR__RMEM_TOTAL_DEPTH);
    assert(endpoint_info.max_raw_frame_size_bytes == CSR__MAX_RAW_FRAME_SIZE);
    assert(endpoint_info.peer_dma_supported == (CSR__HAS_PEER_DMA != 0U));
    assert(endpoint_info.non_oetp_dma_supported == (CSR__HAS_NON_OETP_DMA != 0U));
    assert(endpoint_info.direct_axis_supported == (CSR__HAS_DIRECT_AXIS != 0U));
    assert(endpoint_info.rmem_supported == (CSR__HAS_RMEM != 0U));
    assert(endpoint_info.irq_supported == (CSR__HAS_IRQ != 0U));
}

static void test_endpoint_configuration_readback(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_config_t config;
    openenoc_endpoint_config_t readback;
    const openenoc_endpoint_mac_t group = {{0x03, 0x0e, 0x0c, 0, 0, 1}};

    result = openenoc_endpoint_get_config(endpoint, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    config.mac_address = local_mac;
    config.multicast_address = group;
    config.receive_mode = OPENENOC_ENDPOINT_RECEIVE_PROMISCUOUS;
    config.rmem_timeout_cycles = 1024U;
    config.dma_timeout_cycles = 1024U;
    result = openenoc_endpoint_set_config(endpoint, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_get_config(endpoint, &readback);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    for (unsigned int octet = 0; octet < 6; ++octet) {
        assert(readback.mac_address.octet[octet] == local_mac.octet[octet]);
        assert(readback.multicast_address.octet[octet] == group.octet[octet]);
    }
    assert(readback.receive_mode == config.receive_mode);
    assert(readback.rmem_timeout_cycles == config.rmem_timeout_cycles);
    assert(readback.dma_timeout_cycles == config.dma_timeout_cycles);
}

static void test_unicast_mac_address_validation(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    const openenoc_endpoint_mac_t group = {{0x03, 0x0e, 0x0c, 0, 0, 1}};

    result = openenoc_endpoint_set_mac_address(endpoint, &group);
    assert(result == OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT);
    result = openenoc_endpoint_set_mac_address(endpoint, &local_mac);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
}

static void test_multicast_mac_address_validation_and_disable(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    const openenoc_endpoint_mac_t disabled = {{0}};

    result = openenoc_endpoint_set_multicast_address(endpoint, &local_mac);
    assert(result == OPENENOC_ENDPOINT_STATUS_INVALID_ARGUMENT);
    result = openenoc_endpoint_set_multicast_address(endpoint, &disabled);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
}

static void test_receive_mode_configuration(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_config_t config;

    result = openenoc_endpoint_set_receive_mode(endpoint, OPENENOC_ENDPOINT_RECEIVE_FILTERED);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_get_config(endpoint, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(config.receive_mode == OPENENOC_ENDPOINT_RECEIVE_FILTERED);
}

#if CSR__HAS_RMEM
static void test_rmem_timeout_configuration(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_config_t config;

    result = openenoc_endpoint_set_rmem_timeout(endpoint, 1024U);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_get_config(endpoint, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(config.rmem_timeout_cycles == 1024U);
}
#endif

#if CSR__HAS_PEER_DMA
static void test_peer_dma_timeout_configuration(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_config_t config;

    result = openenoc_endpoint_set_dma_timeout(endpoint, 1024U);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_get_config(endpoint, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(config.dma_timeout_cycles == 1024U);
}

static void test_peer_dma_fragment_size_rounding_and_bounds(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_config_t config;
    uint32_t effective = 0U;
    uint32_t requested = endpoint_info.max_peer_fragment_size_bytes + 3U;

    result = openenoc_endpoint_set_dma_max_fragment_size(endpoint, requested, &effective);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(effective == endpoint_info.max_peer_fragment_size_bytes);
    result = openenoc_endpoint_set_dma_max_fragment_size(endpoint, 3U, &effective);
    assert(result == OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE);
    result = openenoc_endpoint_get_config(endpoint, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(config.dma_max_fragment_size_bytes == requested);
}
#endif

#if CSR__HAS_PEER_DMA || CSR__HAS_RMEM
static void clear_peer_error_and_wait(uint16_t peer_index) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_peer_status_t status;

    result = openenoc_endpoint_peer_request_clear_error(endpoint, peer_index);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    for (uint32_t poll = 0; poll < TEST_POLL_LIMIT; ++poll) {
        result = openenoc_endpoint_peer_get_status(endpoint, peer_index, &status);
        assert(result == OPENENOC_ENDPOINT_STATUS_OK);
        if (!status.clear_error_pending) {
            assert(!status.error && status.error_code == OPENENOC_ENDPOINT_ERROR_NONE);
            return;
        }
    }
    assert(false);
}

static void disable_peer(uint16_t peer_index) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_peer_config_t config = {0};

    result = openenoc_endpoint_peer_set_config(endpoint, peer_index, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
}

static void test_peer_configuration_readback(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_peer_config_t config = {0};
    openenoc_endpoint_peer_config_t readback;
    openenoc_endpoint_peer_status_t status;

    for (uint16_t peer = 0; peer < endpoint_info.peer_count; ++peer) {
        disable_peer(peer);
    }
    config.mac_address = local_mac;
    config.local_address = DMEM_BASE_ADDR;
    config.remote_address = DMEM_BASE_ADDR;
    result = openenoc_endpoint_peer_set_config(endpoint, 0, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_peer_get_config(endpoint, 0, &readback);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(readback.local_address == config.local_address && readback.mode == config.mode);
    result = openenoc_endpoint_peer_get_status(endpoint, 0, &status);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(status.idle && !status.request_pending && !status.done);
}

static void test_peer_index_out_of_range(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_peer_status_t status;

    result = openenoc_endpoint_peer_get_status(endpoint, endpoint_info.peer_count, &status);
    assert(result == OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE);
}

static void test_peer_error_clear_acknowledgement(void) {
    clear_peer_error_and_wait(0);
}
#endif

#if CSR__HAS_RMEM
static volatile uint32_t remote_words[2];

static void test_rmem_pointer_loopback(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_rmem_region_t region;
    openenoc_endpoint_peer_config_t config = {0};
    uint32_t count;

    result = openenoc_endpoint_rmem_get_region(endpoint, &region);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(region.word_count == endpoint_info.rmem_word_count);
    assert(region.words != NULL && region.word_count > 0U);
    count = region.word_count < 2U ? 1U : 2U;
    config.mac_address = local_mac;
    config.local_address = (uint32_t)(uintptr_t)remote_words;
    config.remote_address = config.local_address;
    config.size_bytes = count * sizeof(uint32_t);
    config.mode = OPENENOC_ENDPOINT_PEER_TRANSPARENT_RMEM;
    result = openenoc_endpoint_peer_set_config(endpoint, 0, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    for (uint32_t index = 0; index < count; ++index) {
        uint32_t pattern = UINT32_C(0xa5a50000) + index;
        uint32_t value __attribute__((unused));

        region.words[index] = pattern;
        assert(remote_words[index] == pattern);
        value = region.words[index];
        assert(value == pattern);
    }
    disable_peer(0);
}

static void test_rmem_timeout_records_peer_error(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_rmem_region_t region;
    openenoc_endpoint_peer_config_t config = {0};
    openenoc_endpoint_peer_status_t status;
    uint32_t value __attribute__((unused));
#if CSR__HAS_IRQ
    uint32_t events_before = event_count[OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR];
#endif

    result = openenoc_endpoint_rmem_get_region(endpoint, &region);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    config.mac_address = missing_mac;
    config.local_address = (uint32_t)(uintptr_t)remote_words;
    config.remote_address = config.local_address;
    config.size_bytes = sizeof(uint32_t);
    config.mode = OPENENOC_ENDPOINT_PEER_TRANSPARENT_RMEM;
    result = openenoc_endpoint_peer_set_config(endpoint, 0, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    value = region.words[0];
    assert(value == UINT32_MAX);
    result = openenoc_endpoint_peer_get_status(endpoint, 0, &status);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    assert(status.error && status.error_code == OPENENOC_ENDPOINT_ERROR_TIMEOUT);
#if CSR__HAS_IRQ
    wait_for_irq_events(OPENENOC_ENDPOINT_IRQ_SOURCE_RMEM_ERROR, events_before + 1U);
#endif
    clear_peer_error_and_wait(0);
    disable_peer(0);
}
#endif

#if CSR__HAS_DIRECT_AXIS
static void send_receive_axis_frame(uint32_t buffer_offset, uint32_t receive_capacity) {
    openenoc_endpoint_status_t result __attribute__((unused));
#if CSR__HAS_IRQ
    uint32_t tx_before = event_count[OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_TX_COMPLETE];
#endif

    openenoc_endpoint_irq_mask();
    for (uint32_t index = 0U; index < sizeof(axis_rx_bytes); ++index) {
        axis_rx_bytes[index] = 0xa5U;
    }
    for (uint32_t index = 0U; index < FRAME_BYTES; ++index) {
        axis_tx_bytes[buffer_offset + index] =
            (uint8_t)(frame_words[index / 4U] >> ((index % 4U) * 8U));
    }
    axis_frame_received = false;
    axis_receive_buffer = axis_rx_bytes + buffer_offset;
    axis_receive_capacity = receive_capacity;
    result = openenoc_endpoint_axis_send_stream(endpoint,
        axis_tx_bytes + buffer_offset, FRAME_BYTES);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
#if CSR__HAS_IRQ
    openenoc_endpoint_irq_unmask();
    wait_for_irq_events(OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DIRECT_TX_COMPLETE,
        tx_before + 1U);
    for (uint32_t poll = 0; poll < TEST_POLL_LIMIT && !axis_frame_received && !irq_error; ++poll) {
    }
    assert(!irq_error && axis_frame_received);
#else
    receive_axis_frame();
#endif
}

static void verify_axis_frame_payload(uint32_t buffer_offset, uint32_t stored_bytes) {
    (void)buffer_offset;
    assert(axis_received_bytes == FRAME_BYTES);
    assert(axis_rx_bytes[buffer_offset - 1U] == 0xa5U);
    assert(axis_rx_bytes[buffer_offset + stored_bytes] == 0xa5U);
    for (uint32_t index = 0U; index < stored_bytes; ++index) {
        assert(axis_rx_bytes[buffer_offset + index] == axis_tx_bytes[buffer_offset + index]);
    }
}

static void test_axis_stream_loopback(void) {
    if (CSR__MAX_RAW_FRAME_SIZE < FRAME_BYTES) {
        return;
    }
    send_receive_axis_frame(4U, FRAME_BYTES);
    assert(axis_receive_status == OPENENOC_ENDPOINT_STATUS_OK);
    verify_axis_frame_payload(4U, FRAME_BYTES);
}

static void test_axis_stream_unaligned_buffers(void) {
    if (CSR__MAX_RAW_FRAME_SIZE < FRAME_BYTES) {
        return;
    }
    send_receive_axis_frame(5U, FRAME_BYTES);
    assert(axis_receive_status == OPENENOC_ENDPOINT_STATUS_OK);
    verify_axis_frame_payload(5U, FRAME_BYTES);
}

static void test_axis_stream_receive_overflow(void) {
    if (CSR__MAX_RAW_FRAME_SIZE < FRAME_BYTES) {
        return;
    }
    send_receive_axis_frame(5U, FRAME_BYTES - 1U);
    assert(axis_receive_status == OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE);
    verify_axis_frame_payload(5U, FRAME_BYTES - 1U);
}
#endif

#if CSR__HAS_NON_OETP_DMA
static volatile uint32_t dma_tx_words[FRAME_WORDS];
static volatile uint32_t dma_rx_words[FRAME_WORDS];

static void wait_for_non_oetp_dma_completion(openenoc_endpoint_dma_channel_t channel) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_non_oetp_dma_status_t status;

    for (uint32_t poll = 0; poll < TEST_POLL_LIMIT; ++poll) {
        result = openenoc_endpoint_non_oetp_dma_get_status(endpoint, channel, &status);
        assert(result == OPENENOC_ENDPOINT_STATUS_OK);
        if (!status.request_pending && status.idle) {
            assert(status.done && !status.error && status.transferred_bytes == FRAME_BYTES);
            return;
        }
    }
    assert(false);
}

static void test_non_oetp_dma_zero_length_rejected(void) {
    openenoc_endpoint_status_t result __attribute__((unused));

    result = openenoc_endpoint_non_oetp_dma_tx_request(endpoint,
        (uint32_t)(uintptr_t)dma_tx_words, 0U);
    assert(result == OPENENOC_ENDPOINT_STATUS_OUT_OF_RANGE);
}

static void test_non_oetp_dma_loopback_and_busy_rx(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_non_oetp_dma_status_t status;
#if CSR__HAS_IRQ
    uint32_t tx_before = event_count[OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_TX_COMPLETE];
    uint32_t rx_before = event_count[OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_RX_COMPLETE];
#endif

    if (endpoint_info.max_raw_frame_size_bytes < FRAME_BYTES) {
        return;
    }
    for (uint32_t index = 0; index < FRAME_WORDS; ++index) {
        dma_tx_words[index] = frame_words[index];
        dma_rx_words[index] = 0U;
    }
    result = openenoc_endpoint_non_oetp_dma_rx_arm(endpoint,
        (uint32_t)(uintptr_t)dma_rx_words, FRAME_BYTES);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    for (uint32_t poll = 0; poll < TEST_POLL_LIMIT; ++poll) {
        result = openenoc_endpoint_non_oetp_dma_get_status(endpoint, OPENENOC_ENDPOINT_DMA_RX,
            &status);
        assert(result == OPENENOC_ENDPOINT_STATUS_OK);
        if (status.armed) {
            break;
        }
    }
    assert(status.armed);
    result = openenoc_endpoint_non_oetp_dma_rx_arm(endpoint,
        (uint32_t)(uintptr_t)dma_rx_words, FRAME_BYTES);
    assert(result == OPENENOC_ENDPOINT_STATUS_NOT_READY);
    result = openenoc_endpoint_non_oetp_dma_tx_request(endpoint,
        (uint32_t)(uintptr_t)dma_tx_words, FRAME_BYTES);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    wait_for_non_oetp_dma_completion(OPENENOC_ENDPOINT_DMA_TX);
    wait_for_non_oetp_dma_completion(OPENENOC_ENDPOINT_DMA_RX);
    for (uint32_t index = 0; index < FRAME_WORDS; ++index) {
        uint32_t mask __attribute__((unused)) =
            index == FRAME_WORDS - 1U ? UINT32_C(0xffff) : UINT32_MAX;

        assert((dma_rx_words[index] & mask) == (frame_words[index] & mask));
    }
#if CSR__HAS_IRQ
    wait_for_irq_events(OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_TX_COMPLETE,
        tx_before + 1U);
    wait_for_irq_events(OPENENOC_ENDPOINT_IRQ_SOURCE_NON_OETP_DMA_RX_COMPLETE,
        rx_before + 1U);
#endif
}

static void test_non_oetp_dma_error_clear_requests(void) {
    openenoc_endpoint_status_t result __attribute__((unused));

    result = openenoc_endpoint_non_oetp_dma_request_clear_errors(endpoint,
        OPENENOC_ENDPOINT_DMA_TX);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_non_oetp_dma_request_clear_errors(endpoint,
        OPENENOC_ENDPOINT_DMA_RX);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
}
#endif

#if CSR__HAS_PEER_DMA
static volatile uint32_t peer_source[3];
static volatile uint32_t peer_destination[3];

static void wait_for_peer_dma_completion(uint16_t peer_index, bool success) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_peer_status_t status;

    (void)success;
    for (uint32_t poll = 0; poll < TEST_POLL_LIMIT; ++poll) {
        result = openenoc_endpoint_peer_get_status(endpoint, peer_index, &status);
        assert(result == OPENENOC_ENDPOINT_STATUS_OK);
        if (!status.request_pending && status.idle) {
            assert(status.done == success);
            assert(success ? !status.error : status.error &&
                status.error_code == OPENENOC_ENDPOINT_ERROR_TIMEOUT);
            return;
        }
    }
    assert(false);
}

static void test_peer_dma_timeout(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_peer_config_t config = {0};
#if CSR__HAS_IRQ
    uint32_t before = event_count[OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE];
#endif

    result = openenoc_endpoint_set_dma_max_fragment_size(endpoint, 4U, NULL);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    config.mac_address = missing_mac;
    config.local_address = (uint32_t)(uintptr_t)peer_source;
    config.remote_address = (uint32_t)(uintptr_t)peer_destination;
    config.size_bytes = sizeof(peer_source);
    config.mode = OPENENOC_ENDPOINT_PEER_MIRROR_TO_REMOTE;
    config.irq_enable = endpoint_info.irq_supported;
    result = openenoc_endpoint_peer_set_config(endpoint, 0, &config);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_peer_dma_request(endpoint, 0);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    wait_for_peer_dma_completion(0, false);
#if CSR__HAS_IRQ
    wait_for_irq_events(OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE, before + 1U);
#endif
    clear_peer_error_and_wait(0);
    disable_peer(0);
}

static void test_peer_dma_push_loopback(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_peer_config_t initiator = {0};
    openenoc_endpoint_peer_config_t responder;
#if CSR__HAS_IRQ
    uint32_t before = event_count[OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE];
#endif

    if (endpoint_info.peer_count < 2U) {
        return;
    }
    result = openenoc_endpoint_set_dma_max_fragment_size(endpoint, 4U, NULL);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    initiator.mac_address = local_mac;
    initiator.local_address = (uint32_t)(uintptr_t)peer_source;
    initiator.remote_address = (uint32_t)(uintptr_t)peer_destination;
    initiator.size_bytes = sizeof(peer_source);
    initiator.mode = OPENENOC_ENDPOINT_PEER_MIRROR_TO_REMOTE;
    initiator.irq_enable = endpoint_info.irq_supported;
    responder = initiator;
    responder.local_address = initiator.remote_address;
    responder.mode = OPENENOC_ENDPOINT_PEER_MIRROR_TO_LOCAL;
    result = openenoc_endpoint_peer_set_config(endpoint, 0, &responder);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_peer_set_config(endpoint, 1, &initiator);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    for (uint32_t index = 0; index < 3U; ++index) {
        peer_source[index] = UINT32_C(0x12340000) + index;
        peer_destination[index] = 0U;
    }
    result = openenoc_endpoint_peer_dma_request(endpoint, 1);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    wait_for_peer_dma_completion(1, true);
#if CSR__HAS_IRQ
    wait_for_irq_events(OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE, before + 1U);
#endif
    for (uint32_t index = 0; index < 3U; ++index) {
        assert(peer_destination[index] == peer_source[index]);
    }
    disable_peer(0);
    disable_peer(1);
}

static void test_peer_dma_pull_loopback(void) {
    openenoc_endpoint_status_t result __attribute__((unused));
    openenoc_endpoint_peer_config_t initiator = {0};
    openenoc_endpoint_peer_config_t responder;
#if CSR__HAS_IRQ
    uint32_t before = event_count[OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE];
#endif

    if (endpoint_info.peer_count < 2U) {
        return;
    }
    result = openenoc_endpoint_set_dma_max_fragment_size(endpoint, 4U, NULL);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    initiator.mac_address = local_mac;
    initiator.local_address = (uint32_t)(uintptr_t)peer_source;
    initiator.remote_address = (uint32_t)(uintptr_t)peer_destination;
    initiator.size_bytes = sizeof(peer_source);
    initiator.mode = OPENENOC_ENDPOINT_PEER_MIRROR_TO_LOCAL;
    initiator.irq_enable = endpoint_info.irq_supported;
    responder = initiator;
    responder.local_address = initiator.remote_address;
    responder.mode = OPENENOC_ENDPOINT_PEER_MIRROR_TO_REMOTE;
    result = openenoc_endpoint_peer_set_config(endpoint, 0, &responder);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    result = openenoc_endpoint_peer_set_config(endpoint, 1, &initiator);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    for (uint32_t index = 0; index < 3U; ++index) {
        peer_source[index] = 0U;
        peer_destination[index] = UINT32_C(0x12340000) + index;
    }
    result = openenoc_endpoint_peer_dma_request(endpoint, 1);
    assert(result == OPENENOC_ENDPOINT_STATUS_OK);
    wait_for_peer_dma_completion(1, true);
#if CSR__HAS_IRQ
    wait_for_irq_events(OPENENOC_ENDPOINT_IRQ_SOURCE_PEER_DMA_COMPLETE, before + 1U);
#endif
    for (uint32_t index = 0; index < 3U; ++index) {
        assert(peer_source[index] == peer_destination[index]);
    }
    disable_peer(0);
    disable_peer(1);
}
#endif

static void run_tests(void) {
    volatile csr_t *csr = (volatile csr_t *)(uintptr_t)CSR_BASE_ADDR;

    openenoc_endpoint_irq_mask();
    endpoint = &csr->endpoint_interface;
    test_endpoint_initialization();
    test_endpoint_information();
    test_endpoint_configuration_readback();
    test_unicast_mac_address_validation();
    test_multicast_mac_address_validation_and_disable();
    test_receive_mode_configuration();
#if CSR__HAS_RMEM
    test_rmem_timeout_configuration();
#endif
#if CSR__HAS_PEER_DMA
    test_peer_dma_timeout_configuration();
    test_peer_dma_fragment_size_rounding_and_bounds();
#endif
    _openenoc_assert_status.completed_checks |= TEST_CONFIG;
#if CSR__HAS_IRQ
    test_irq_configuration_and_empty_claim();
    test_irq_error_clear_preserves_global_enable();
    openenoc_endpoint_irq_unmask();
#endif
#if CSR__HAS_PEER_DMA || CSR__HAS_RMEM
    test_peer_configuration_readback();
    test_peer_index_out_of_range();
    test_peer_error_clear_acknowledgement();
    _openenoc_assert_status.completed_checks |= TEST_PEER;
#endif
#if CSR__HAS_RMEM
    test_rmem_pointer_loopback();
    test_rmem_timeout_records_peer_error();
    _openenoc_assert_status.completed_checks |= TEST_RMEM;
#endif
#if CSR__HAS_DIRECT_AXIS
    test_axis_stream_loopback();
    test_axis_stream_unaligned_buffers();
    test_axis_stream_receive_overflow();
    if (CSR__MAX_RAW_FRAME_SIZE >= FRAME_BYTES) {
        _openenoc_assert_status.completed_checks |= TEST_AXIS;
    }
#endif
#if CSR__HAS_NON_OETP_DMA
    test_non_oetp_dma_zero_length_rejected();
    test_non_oetp_dma_loopback_and_busy_rx();
    test_non_oetp_dma_error_clear_requests();
    if (CSR__MAX_RAW_FRAME_SIZE >= FRAME_BYTES) {
        _openenoc_assert_status.completed_checks |= TEST_RAW_DMA;
    }
#endif
#if CSR__HAS_PEER_DMA
    test_peer_dma_timeout();
    test_peer_dma_push_loopback();
    test_peer_dma_pull_loopback();
    _openenoc_assert_status.completed_checks |= TEST_PEER_DMA;
#endif
    openenoc_endpoint_irq_mask();
#if CSR__HAS_IRQ
    test_irq_controller_idle_after_transfers();
    _openenoc_assert_status.completed_checks |= TEST_IRQ;
#endif
}

int main(void) {
    run_tests();
    _openenoc_assert_status.status = OPENENOC_ASSERT_STATUS_PASSED;
    return 0;
}
