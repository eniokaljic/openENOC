// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

#ifndef OPENENOC_ISS_H
#define OPENENOC_ISS_H

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

#define OPENENOC_ISS_ABI_VERSION UINT32_C(1)
#define OPENENOC_ISS_REQUEST_DATA_SIZE UINT32_C(4)

typedef struct openenoc_iss openenoc_iss_t;

enum {
    OPENENOC_ISS_OK = 0,
    OPENENOC_ISS_NOT_READY = 1,
    OPENENOC_ISS_INVALID_ARGUMENT = -1,
    OPENENOC_ISS_INVALID_STATE = -2,
    OPENENOC_ISS_OUT_OF_RANGE = -3,
    OPENENOC_ISS_INTERNAL_ERROR = -4,
};

enum {
    OPENENOC_ISS_STATE_READY = 0,
    OPENENOC_ISS_STATE_RUNNING = 1,
    OPENENOC_ISS_STATE_WAITING_MMIO = 2,
    OPENENOC_ISS_STATE_COMPLETED = 3,
    OPENENOC_ISS_STATE_STOPPED = 4,
    OPENENOC_ISS_STATE_ERROR = 5,
};

enum {
    OPENENOC_ISS_REQUEST_DATA_READ = 1,
    OPENENOC_ISS_REQUEST_DATA_WRITE = 2,
};

enum {
    OPENENOC_ISS_RESPONSE_OK = 0,
    OPENENOC_ISS_RESPONSE_BUS_ERROR = 1,
    OPENENOC_ISS_RESPONSE_CANCELLED = 2,
};

typedef struct {
    uint32_t abi_version;
    uint32_t struct_size;
    uint32_t endpoint_id;
    uint32_t reserved;
    uint64_t imem_base;
    uint64_t imem_size;
    uint64_t reset_pc;
} openenoc_iss_config_t;

typedef struct {
    uint32_t abi_version;
    uint32_t struct_size;
    uint32_t endpoint_id;
    uint32_t kind;
    uint64_t epoch;
    uint64_t request_id;
    uint64_t address;
    uint64_t pc;
    uint32_t size_bytes;
    uint32_t byte_enable;
    uint8_t data[OPENENOC_ISS_REQUEST_DATA_SIZE];
    uint8_t reserved[4];
} openenoc_iss_request_t;

typedef struct {
    uint32_t abi_version;
    uint32_t struct_size;
    uint32_t endpoint_id;
    uint32_t status;
    uint64_t epoch;
    uint64_t request_id;
    uint32_t axi_resp;
    uint32_t size_bytes;
    uint8_t data[OPENENOC_ISS_REQUEST_DATA_SIZE];
    uint8_t reserved[4];
    uint64_t accepted_sim_tick;
    uint64_t completed_sim_tick;
} openenoc_iss_response_t;

typedef struct {
    uint32_t abi_version;
    uint32_t struct_size;
    uint32_t endpoint_id;
    uint32_t run_state;
    uint64_t epoch;
    uint64_t step_count;
    uint64_t pc;
    uint64_t pending_request_id;
} openenoc_iss_state_t;

uint32_t openenoc_iss_abi_version(void);
const char *openenoc_iss_status_string(int32_t status);

int32_t openenoc_iss_create(
    const openenoc_iss_config_t *config,
    openenoc_iss_t **out_handle);
void openenoc_iss_destroy(openenoc_iss_t *handle);

int32_t openenoc_iss_load_image(
    openenoc_iss_t *handle,
    uint64_t address,
    const uint8_t *data,
    uint64_t size);
int32_t openenoc_iss_start(
    openenoc_iss_t *handle,
    uint64_t entry_pc,
    uint64_t max_steps);
int32_t openenoc_iss_request_stop(openenoc_iss_t *handle);

int32_t openenoc_iss_try_poll(
    openenoc_iss_t *handle,
    openenoc_iss_request_t *request);
int32_t openenoc_iss_complete(
    openenoc_iss_t *handle,
    const openenoc_iss_response_t *response);
int32_t openenoc_iss_try_state(
    openenoc_iss_t *handle,
    openenoc_iss_state_t *state);
int32_t openenoc_iss_read_register(
    openenoc_iss_t *handle,
    uint32_t index,
    uint64_t *value);

#ifdef __cplusplus
}
#endif

#endif