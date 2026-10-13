// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

#include <iostream>

#include "riscv/isa_parser.h"

int main()
{
    isa_parser_t isa("RV32I", "M");

    if (isa.get_max_xlen() != 32 || !isa.extension_enabled('I') ||
            isa.extension_enabled('M')) {
        std::cerr << "Unexpected Spike ISA profile: " << isa.get_isa_string()
                  << '\n';
        return 1;
    }

    std::cout << "Spike API link smoke passed: " << isa.get_isa_string()
              << ", privilege=M\n";
    return 0;
}