// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

#include <inttypes.h>
#include <sched.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#include "openenoc_iss.h"

#define EXTERNAL_ADDRESS UINT64_C(0x10000000)
#define POLL_LIMIT UINT32_C(1000000)

static int check_status(int32_t status, const char *operation)
{
    if (status == OPENENOC_ISS_OK) {
        return 0;
    }

    fprintf(stderr, "%s failed: %s (%" PRId32 ")\n", operation,
            openenoc_iss_status_string(status), status);
    return 1;
}

static void encode_program(uint8_t *image)
{
    static const uint32_t program[] = {
        UINT32_C(0x100000b7),
        UINT32_C(0x02a00113),
        UINT32_C(0x0020a023),
        UINT32_C(0x0000a183),
        UINT32_C(0x00118213),
    };

    for (size_t word = 0; word < sizeof(program) / sizeof(program[0]); ++word) {
        for (size_t byte = 0; byte < sizeof(program[word]); ++byte) {
            image[word * sizeof(program[word]) + byte] =
                (uint8_t)(program[word] >> (byte * 8));
        }
    }
}

int main(void)
{
    uint8_t image[5 * sizeof(uint32_t)] = {0};
    openenoc_iss_t *iss = NULL;
    openenoc_iss_config_t config = {
        .abi_version = OPENENOC_ISS_ABI_VERSION,
        .struct_size = sizeof(config),
        .endpoint_id = 7,
        .imem_base = 0,
        .imem_size = 32 * 1024,
        .reset_pc = 0,
    };
    unsigned write_count = 0;
    unsigned read_count = 0;
    int result = 1;

    if (openenoc_iss_abi_version() != OPENENOC_ISS_ABI_VERSION) {
        fprintf(stderr, "Unexpected ISS ABI version\n");
        return 1;
    }

    encode_program(image);
    if (check_status(openenoc_iss_create(&config, &iss), "create") ||
            check_status(openenoc_iss_load_image(
                iss, 0, image, sizeof(image)), "load image") ||
            check_status(openenoc_iss_start(iss, 0, 5), "start")) {
        goto cleanup;
    }

    for (uint32_t attempt = 0; attempt < POLL_LIMIT; ++attempt) {
        openenoc_iss_request_t request = {
            .abi_version = OPENENOC_ISS_ABI_VERSION,
            .struct_size = sizeof(request),
        };
        int32_t poll_status = openenoc_iss_try_poll(iss, &request);

        if (poll_status == OPENENOC_ISS_OK) {
            openenoc_iss_response_t response = {
                .abi_version = OPENENOC_ISS_ABI_VERSION,
                .struct_size = sizeof(response),
                .endpoint_id = request.endpoint_id,
                .status = OPENENOC_ISS_RESPONSE_OK,
                .epoch = request.epoch,
                .request_id = request.request_id,
                .axi_resp = 0,
                .size_bytes = request.size_bytes,
            };

            if (request.endpoint_id != config.endpoint_id ||
                    request.address != EXTERNAL_ADDRESS ||
                    request.size_bytes != sizeof(uint32_t) ||
                    request.byte_enable != UINT32_C(0xf)) {
                fprintf(stderr, "Unexpected MMIO request metadata\n");
                goto cleanup;
            }

            if (request.kind == OPENENOC_ISS_REQUEST_DATA_WRITE) {
                if (memcmp(request.data, "\x2a\x00\x00\x00", 4) != 0 ||
                        request.pc != 8 || write_count != 0) {
                    fprintf(stderr, "Unexpected MMIO write request\n");
                    goto cleanup;
                }
                ++write_count;
            } else if (request.kind == OPENENOC_ISS_REQUEST_DATA_READ) {
                if (request.pc != 12 || read_count != 0) {
                    fprintf(stderr, "Unexpected MMIO read request\n");
                    goto cleanup;
                }
                response.data[0] = 42;
                ++read_count;
            } else {
                fprintf(stderr, "Unexpected MMIO request kind\n");
                goto cleanup;
            }

            if (check_status(openenoc_iss_complete(iss, &response),
                             "complete request")) {
                goto cleanup;
            }
        } else if (poll_status != OPENENOC_ISS_NOT_READY) {
            check_status(poll_status, "poll request");
            goto cleanup;
        }

        openenoc_iss_state_t state = {
            .abi_version = OPENENOC_ISS_ABI_VERSION,
            .struct_size = sizeof(state),
        };
        if (check_status(openenoc_iss_try_state(iss, &state), "read state")) {
            goto cleanup;
        }
        if (state.run_state == OPENENOC_ISS_STATE_ERROR) {
            fprintf(stderr, "ISS worker entered error state\n");
            goto cleanup;
        }
        if (state.run_state == OPENENOC_ISS_STATE_COMPLETED) {
            uint64_t x3 = 0;
            uint64_t x4 = 0;
            if (state.pc != sizeof(image) || state.step_count != 5 ||
                    write_count != 1 || read_count != 1 ||
                    check_status(openenoc_iss_read_register(iss, 3, &x3),
                                 "read x3") ||
                    check_status(openenoc_iss_read_register(iss, 4, &x4),
                                 "read x4") ||
                    x3 != 42 || x4 != 43) {
                fprintf(stderr,
                        "Unexpected final state: pc=0x%" PRIx64
                        ", steps=%" PRIu64 ", x3=%" PRIu64
                        ", x4=%" PRIu64 "\n",
                        state.pc, state.step_count, x3, x4);
                goto cleanup;
            }
            result = 0;
            break;
        }

        sched_yield();
    }

    if (result != 0) {
        fprintf(stderr, "Timed out waiting for the ISS worker\n");
        goto cleanup;
    }

    printf("Spike C API smoke passed: endpoint=7, writes=1, reads=1, "
           "x3=42, x4=43\n");

cleanup:
    openenoc_iss_destroy(iss);
    return result;
}