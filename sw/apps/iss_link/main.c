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
        while (openenoc_endpoint_axis_send(
            &csr->endpoint_interface.axis_if, outgoing, 0xf, false) ==
            OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
        }
        while (iss_link_release == 0) {
        }
        while (openenoc_endpoint_axis_send(
            &csr->endpoint_interface.axis_if, REQUEST_LAST_WORD, 0xf, true) ==
            OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
        }
    }

    while (openenoc_endpoint_axis_receive(
        &csr->endpoint_interface.axis_if, &received, &keep, &last) ==
        OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
    }
    iss_link_received = received;
    if (received != expected || keep != 0xf ||
        last == (role == RESPONDER_ROLE)) {
        iss_link_status = STATUS_FAILED;
        return 1;
    }

    if (role == RESPONDER_ROLE) {
        while (openenoc_endpoint_axis_receive(
            &csr->endpoint_interface.axis_if, &received, &keep, &last) ==
            OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
        }
        if (received != REQUEST_LAST_WORD || keep != 0xf || !last) {
            iss_link_status = STATUS_FAILED;
            return 1;
        }
        while (openenoc_endpoint_axis_send(
            &csr->endpoint_interface.axis_if, outgoing, 0xf, true) ==
            OPENENOC_ENDPOINT_AXIS_STATUS_NOT_READY) {
        }
    }

    iss_link_status = role == INITIATOR_ROLE ?
        STATUS_INITIATOR_PASSED : STATUS_RESPONDER_PASSED;
    return 0;
}