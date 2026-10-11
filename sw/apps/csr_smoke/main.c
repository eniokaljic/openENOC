/* SPDX-FileCopyrightText: 2026 Enio Kaljic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <stdint.h>

#include "csr.h"
#include "memory_map.h"
#include "openenoc_endpoint_axis.h"
#include "openenoc_endpoint_irq.h"

#define CSR_SMOKE_PATTERN UINT32_C(0xa5a55a5a)
#define CSR_SMOKE_RUNNING UINT32_C(0x00000000)
#define CSR_SMOKE_PASSED  UINT32_C(0x600d600d)
#define CSR_SMOKE_FAILED  UINT32_C(0xbad0bad0)
#define SWITCH_FORWARDING_PATTERN UINT32_C(0xa)
#define AXIS_LOOPBACK_WORD_COUNT 17U
#define AXIS_LOOPBACK_FULL_KEEP UINT8_C(0xf)
#define AXIS_LOOPBACK_LAST_KEEP UINT8_C(0x3)
#define AXIS_LOOPBACK_BYTE_COUNT 66U

static const uint32_t axis_loopback_words[AXIS_LOOPBACK_WORD_COUNT] = {
    UINT32_C(0xffffffff), UINT32_C(0x0122ffff),
    UINT32_C(0x89abcdef), UINT32_C(0xffffffff),
    UINT32_C(0xa5a55a5a), UINT32_C(0x5a5aa5a5),
    UINT32_C(0x00000001), UINT32_C(0x80000000),
    UINT32_C(0x11111111), UINT32_C(0x22222222),
    UINT32_C(0x33333333), UINT32_C(0x44444444),
    UINT32_C(0xdeadbeef), UINT32_C(0xc001d00d),
    UINT32_C(0x13579bdf), UINT32_C(0x2468ace0),
    UINT32_C(0x0000beef),
};

/* Keep the simulator's result at the first DMEM word. */
volatile uint32_t csr_smoke_status
    __attribute__((section(".data.csr_smoke_status"))) = CSR_SMOKE_RUNNING;

/* The ISR owns these DMEM buffers until it publishes the TLAST notification. */
static volatile uint32_t received_words[AXIS_LOOPBACK_WORD_COUNT];
static volatile uint8_t received_keep[AXIS_LOOPBACK_WORD_COUNT];
static volatile bool received_last[AXIS_LOOPBACK_WORD_COUNT];
static volatile uint32_t received_word_count;
static volatile uint32_t received_byte_count;
static volatile bool rx_frame_complete;
static volatile bool tx_frame_complete;
static volatile bool irq_error;

struct receiver_context {
    volatile csr__endpoint_interface__axis_if_t *axis_if;
};

static struct receiver_context receiver_context;

static void receive_axis_frame(
    volatile csr__endpoint_interface__irq_t *irq,
    void *context) {
    struct receiver_context *receiver = context;
    volatile csr__endpoint_interface__axis_if_t *axis_if = receiver->axis_if;
    bool last = false;

    (void)irq;

    if (rx_frame_complete) {
        irq_error = true;
    }

    while (!last) {
        uint32_t data;
        uint8_t keep;

        if (openenoc_endpoint_axis_receive(axis_if, &data, &keep, &last) ==
            OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
            continue;
        }

        uint32_t index = received_word_count;
        if (index < AXIS_LOOPBACK_WORD_COUNT) {
            received_words[index] = data;
            received_keep[index] = keep;
            received_last[index] = last;
        } else {
            // Drain an oversized frame through TLAST without overrunning DMEM.
            irq_error = true;
        }
        received_word_count = index + 1U;
        for (uint32_t lane = 0; lane < 4U; ++lane) {
            if ((keep & (UINT8_C(1) << lane)) != 0U) {
                received_byte_count++;
            }
        }
    }

    // All volatile buffer stores precede this notification to main.
    rx_frame_complete = true;
}

static void notify_tx_complete(
    volatile csr__endpoint_interface__irq_t *irq,
    void *context) {
    (void)irq;
    (void)context;

    if (tx_frame_complete) {
        irq_error = true;
    }
    tx_frame_complete = true;
}

static void notify_irq_error(
    openenoc_endpoint_irq_result_t result,
    void *context) {
    (void)result;
    (void)context;
    irq_error = true;
}

static const openenoc_endpoint_irq_callbacks_t endpoint_irq_callbacks = {
    .non_oetp_direct_tx_complete = notify_tx_complete,
    .non_oetp_direct_rx_available = receive_axis_frame,
    .error = notify_irq_error,
    .context = &receiver_context,
};

int main(void) {
    volatile csr_t *const csr =
        (volatile csr_t *)(uintptr_t)CSR_BASE_ADDR;

    openenoc_endpoint_irq_mask();

    // Verify basic software-writable CSR access.
    csr->test_reg.f.test_field = CSR_SMOKE_PATTERN;

    if (csr->test_reg.f.test_field != CSR_SMOKE_PATTERN) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    // Configure the switch and verify software and hardware-driven fields.
    csr->switch_interface.forwarding_control.f.operation_mode = 1U;
    csr->switch_interface.default_forwarding.f.bitmap =
        SWITCH_FORWARDING_PATTERN;
    csr->switch_interface.forwarding_control.f.pause_request = 1U;

    if (csr->switch_interface.forwarding_control.f.operation_mode != 1U ||
        csr->switch_interface.forwarding_control.f.pause_request != 1U ||
        csr->switch_interface.forwarding_control.f.pause_done != 1U ||
        csr->switch_interface.default_forwarding.f.bitmap !=
            SWITCH_FORWARDING_PATTERN) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    if (!csr->endpoint_interface.info.f.irq_supported) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    receiver_context.axis_if = &csr->endpoint_interface.axis_if;
    openenoc_endpoint_irq_bind(&csr->endpoint_interface.irq, &endpoint_irq_callbacks);
    const openenoc_endpoint_irq_config_t irq_config = {
        .global_enable = true,
        .non_oetp_direct_tx_complete = true,
        .non_oetp_direct_rx_available = true,
    };
    openenoc_endpoint_irq_configure(&csr->endpoint_interface.irq, &irq_config);

    // Capture IRQ events while sending, but keep the CPU masked until the final
    // beat is submitted. A blocking loopback RX ISR must not preempt its sender.
    // Send a 66-byte frame, with only two valid bytes in the final word.
    for (uint32_t i = 0; i < AXIS_LOOPBACK_WORD_COUNT; ++i) {
        bool last = i == AXIS_LOOPBACK_WORD_COUNT - 1U;

        while (openenoc_endpoint_axis_send(
            &csr->endpoint_interface.axis_if,
            axis_loopback_words[i],
            last ? AXIS_LOOPBACK_LAST_KEEP : AXIS_LOOPBACK_FULL_KEEP,
            last) == OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
        }
    }

    openenoc_endpoint_irq_unmask();
    while ((!rx_frame_complete || !tx_frame_complete) && !irq_error) {
    }
    openenoc_endpoint_irq_mask();
    openenoc_endpoint_irq_set_global_enable(&csr->endpoint_interface.irq, false);

    if (irq_error || received_word_count != AXIS_LOOPBACK_WORD_COUNT ||
        received_byte_count != AXIS_LOOPBACK_BYTE_COUNT) {
        csr_smoke_status = CSR_SMOKE_FAILED;
        return 1;
    }

    // Compare only after the IRQ receiver has published the TLAST notification.
    for (uint32_t i = 0; i < AXIS_LOOPBACK_WORD_COUNT; ++i) {
        bool expected_last = i == AXIS_LOOPBACK_WORD_COUNT - 1U;
        uint8_t expected_keep =
            expected_last ? AXIS_LOOPBACK_LAST_KEEP : AXIS_LOOPBACK_FULL_KEEP;
        if (received_words[i] != axis_loopback_words[i] ||
            received_keep[i] != expected_keep || received_last[i] != expected_last) {
            csr_smoke_status = CSR_SMOKE_FAILED;
            return 1;
        }
    }

    csr_smoke_status = CSR_SMOKE_PASSED;
    return 0;
}
