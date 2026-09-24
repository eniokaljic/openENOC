// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

#include "riscv/processor.h"
#include "riscv/simif.h"

namespace {

constexpr char kIsa[] = "RV32I";
constexpr char kPrivilege[] = "M";
constexpr reg_t kExternalAddress = 0x10000000;
constexpr size_t kImemSize = 32 * 1024;

class TestSimIf final : public simif_t
{
public:
    TestSimIf() : memory_(kImemSize, 0)
    {
        debug_mmu = nullptr;
        config_.isa = kIsa;
        config_.priv = kPrivilege;
        config_.endianness = endianness_little;
        config_.mem_layout = {mem_cfg_t(0, kImemSize)};
        config_.hartids = {0};
        config_.explicit_hartids = true;
        config_.start_pc.set_global(0);
    }

    const cfg_t *config() const
    {
        return &config_;
    }

    void attach(processor_t *processor)
    {
        harts_.emplace(0, processor);
        processor->get_state()->pc = 0;
    }

    void load_program(const std::array<uint32_t, 5> &program)
    {
        for (size_t word = 0; word < program.size(); ++word) {
            for (size_t byte = 0; byte < sizeof(program[word]); ++byte) {
                memory_[word * sizeof(program[word]) + byte] =
                    static_cast<uint8_t>(program[word] >> (byte * 8));
            }
        }
    }

    char *addr_to_mem(reg_t address) override
    {
        if (address >= memory_.size()) {
            return nullptr;
        }

        return reinterpret_cast<char *>(memory_.data() + address);
    }

    bool mmio_fetch(reg_t, size_t, uint8_t *) override
    {
        ++fetch_count;
        return false;
    }

    bool mmio_load(reg_t address, size_t length, uint8_t *bytes) override
    {
        if (address != kExternalAddress || length != sizeof(external_value)) {
            return false;
        }

        ++load_count;
        for (size_t byte = 0; byte < length; ++byte) {
            bytes[byte] = static_cast<uint8_t>(external_value >> (byte * 8));
        }
        return true;
    }

    bool mmio_store(reg_t address, size_t length, const uint8_t *bytes) override
    {
        if (address != kExternalAddress || length != sizeof(external_value)) {
            return false;
        }

        ++store_count;
        external_value = 0;
        for (size_t byte = 0; byte < length; ++byte) {
            external_value |= static_cast<uint32_t>(bytes[byte]) << (byte * 8);
        }
        return true;
    }

    void proc_reset(unsigned id) override
    {
        ++reset_count;
        auto hart = harts_.find(id);
        if (hart != harts_.end()) {
            hart->second->get_state()->pc = config_.start_pc.get(id).value_or(0);
        }
    }

    const cfg_t &get_cfg() const override
    {
        return config_;
    }

    const std::map<size_t, processor_t *> &get_harts() const override
    {
        return harts_;
    }

    const char *get_symbol(uint64_t) override
    {
        return nullptr;
    }

    uint32_t external_value = 0;
    size_t fetch_count = 0;
    size_t load_count = 0;
    size_t store_count = 0;
    size_t reset_count = 0;

private:
    cfg_t config_;
    std::vector<uint8_t> memory_;
    std::map<size_t, processor_t *> harts_;
};

} // namespace

int main()
{
    constexpr std::array<uint32_t, 5> program = {
        0x100000b7, // lui  x1, 0x10000
        0x02a00113, // addi x2, x0, 42
        0x0020a023, // sw   x2, 0(x1)
        0x0000a183, // lw   x3, 0(x1)
        0x00118213, // addi x4, x3, 1
    };

    TestSimIf sim;
    sim.load_program(program);

    processor_t processor(
        kIsa, kPrivilege, sim.config(), &sim, 0, false, nullptr, std::cerr);
    sim.attach(&processor);
    processor.step(program.size());

    const state_t *state = processor.get_state();
    if (state->pc != program.size() * sizeof(program[0]) ||
            state->XPR[3] != 42 || state->XPR[4] != 43 ||
            sim.external_value != 42 || sim.store_count != 1 ||
            sim.load_count != 1 || sim.fetch_count != 0 ||
            sim.reset_count != 1) {
        std::cerr << "Unexpected processor result: pc=0x" << std::hex
                  << state->pc << std::dec << ", x3=" << state->XPR[3]
                  << ", x4=" << state->XPR[4]
                  << ", external=" << sim.external_value
                  << ", stores=" << sim.store_count
                  << ", loads=" << sim.load_count
                  << ", external_fetches=" << sim.fetch_count
                  << ", resets=" << sim.reset_count << '\n';
        return 1;
    }

    std::cout << "Spike processor smoke passed: x3=42, x4=43, "
                 "MMIO writes=1, MMIO reads=1\n";
    return 0;
}