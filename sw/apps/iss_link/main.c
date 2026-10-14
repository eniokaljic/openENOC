/* SPDX-FileCopyrightText: 2026 Kerim Bavcic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <stdint.h>

#include "csr.h"
#include "memory_map.h"
#include "openenoc_endpoint_axis.h"

#define INITIATOR_ROLE UINT32_C(1)
#define RESPONDER_ROLE UINT32_C(2)
#define REQUEST_WORD UINT32_C(0x13579bdf)
#define REQUEST_LAST_WORD UINT32_C(0x89abcdef)
#define REPLY_WORD UINT32_C(0x2468ace0)
#define STATUS_FAILED UINT32_C(0xbad0bad0)
#define STATUS_INITIATOR_PASSED UINT32_C(0x600d0001)
#define STATUS_RESPONDER_PASSED UINT32_C(0x600d0002)

volatile uint32_t iss_link_status;
volatile uint32_t iss_link_received;
volatile uint32_t iss_link_release;

/* Broadcast destination, source 22:01:ef:cd:ab:89, EtherType 0x0800. */
static const uint32_t frame_header[] = {
    UINT32_C(0xffffffff), UINT32_C(0x0122ffff),
    UINT32_C(0x89abcdef), UINT32_C(0x00000008),
};

static void send_header(volatile csr__endpoint_interface_t *endpoint) {
    for (unsigned index = 0; index < sizeof(frame_header) / sizeof(frame_header[0]); ++index) {
        while (openenoc_endpoint_axis_send(
            endpoint, frame_header[index], 0xf, false) ==
            OPENENOC_ENDPOINT_STATUS_NOT_READY) {
        }
    }
}

static bool receive_header(volatile csr__endpoint_interface_t *endpoint) {
    for (unsigned index = 0; index < sizeof(frame_header) / sizeof(frame_header[0]); ++index) {
        uint32_t data;
        uint8_t keep;
        bool last;

        while (openenoc_endpoint_axis_receive(endpoint, &data, &keep, &last) ==
            OPENENOC_ENDPOINT_STATUS_NOT_READY) {
        }
        if (data != frame_header[index] || keep != 0xf || last) {
            return false;
        }
    }
    return true;
}

int main(void) {
    volatile csr_t *const csr = (volatile csr_t *)(uintptr_t)CSR_BASE_ADDR;
    const uint32_t role = csr->test_reg.f.test_field;
    uint32_t expected;
    uint32_t outgoing;
    uint32_t received;
    uint8_t keep;
    bool last;

    if (role == INITIATOR_ROLE) {
        outgoing = REQUEST_WORD;
        expected = REPLY_WORD;
    } else if (role == RESPONDER_ROLE) {
        outgoing = REPLY_WORD;
        expected = REQUEST_WORD;
    } else {
        iss_link_status = STATUS_FAILED;
        return 1;
    }

    if (role == INITIATOR_ROLE) {
        send_header(&csr->endpoint_interface);
        while (openenoc_endpoint_axis_send(
            &csr->endpoint_interface, outgoing, 0xf, false) ==
            OPENENOC_ENDPOINT_STATUS_NOT_READY) {
        }
        while (iss_link_release == 0) {
        }
        while (openenoc_endpoint_axis_send(
            &csr->endpoint_interface, REQUEST_LAST_WORD, 0xf, true) ==
            OPENENOC_ENDPOINT_STATUS_NOT_READY) {
        }
    }

    if (!receive_header(&csr->endpoint_interface)) {
        iss_link_status = STATUS_FAILED;
        return 1;
    }
    while (openenoc_endpoint_axis_receive(
        &csr->endpoint_interface, &received, &keep, &last) ==
        OPENENOC_ENDPOINT_STATUS_NOT_READY) {
    }
    iss_link_received = received;
    if (received != expected || keep != 0xf ||
        last == (role == RESPONDER_ROLE)) {
        iss_link_status = STATUS_FAILED;
        return 1;
    }

    if (role == RESPONDER_ROLE) {
        while (openenoc_endpoint_axis_receive(
            &csr->endpoint_interface, &received, &keep, &last) ==
            OPENENOC_ENDPOINT_STATUS_NOT_READY) {
        }
        if (received != REQUEST_LAST_WORD || keep != 0xf || !last) {
            iss_link_status = STATUS_FAILED;
            return 1;
        }
        send_header(&csr->endpoint_interface);
        while (openenoc_endpoint_axis_send(
            &csr->endpoint_interface, outgoing, 0xf, true) ==
            OPENENOC_ENDPOINT_STATUS_NOT_READY) {
        }
    }

    iss_link_status = role == INITIATOR_ROLE ?
        STATUS_INITIATOR_PASSED : STATUS_RESPONDER_PASSED;
    return 0;
}
