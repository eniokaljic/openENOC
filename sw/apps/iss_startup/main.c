/* SPDX-FileCopyrightText: 2026 Kerim Bavcic
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */

#include <stdint.h>

#define ISS_STARTUP_PASSED UINT32_C(0x51a7c0de)
#define ISS_STARTUP_FAILED UINT32_C(0xfa11ed00)
#define INITIALIZED_WORD_0 UINT32_C(0x12345678)
#define INITIALIZED_WORD_1 UINT32_C(0x89abcdef)
#define RODATA_WORD_0 UINT32_C(0x0badcafe)
#define RODATA_WORD_1 UINT32_C(0xc001d00d)
#define STACK_SEED UINT32_C(0x2468ace0)

volatile uint32_t iss_startup_status;
volatile uint32_t startup_initialized[2] = {
    INITIALIZED_WORD_0,
    INITIALIZED_WORD_1,
};
volatile uint32_t startup_bss;
const uint32_t startup_rodata[2] = {
    RODATA_WORD_0,
    RODATA_WORD_1,
};

__attribute__((noinline))
static uint32_t stack_probe(uint32_t seed) {
    volatile uint32_t frame[4];

    frame[0] = seed ^ RODATA_WORD_0;
    frame[1] = INITIALIZED_WORD_0 + RODATA_WORD_1;
    frame[2] = frame[0] ^ frame[1];
    frame[3] = frame[2] + INITIALIZED_WORD_1;

    return frame[0] + frame[1] + frame[2] + frame[3];
}

int main(void) {
    const volatile uint32_t *const rodata = startup_rodata;
    const uint32_t expected_stack =
        (STACK_SEED ^ RODATA_WORD_0) +
        (INITIALIZED_WORD_0 + RODATA_WORD_1) +
        ((STACK_SEED ^ RODATA_WORD_0) ^
         (INITIALIZED_WORD_0 + RODATA_WORD_1)) +
        (((STACK_SEED ^ RODATA_WORD_0) ^
          (INITIALIZED_WORD_0 + RODATA_WORD_1)) + INITIALIZED_WORD_1);

    if (startup_initialized[0] != INITIALIZED_WORD_0 ||
        startup_initialized[1] != INITIALIZED_WORD_1 ||
        startup_bss != 0 ||
        rodata[0] != RODATA_WORD_0 ||
        rodata[1] != RODATA_WORD_1 ||
        stack_probe(STACK_SEED) != expected_stack) {
        iss_startup_status = ISS_STARTUP_FAILED;
        return 1;
    }

    iss_startup_status = ISS_STARTUP_PASSED;
    return 0;
}