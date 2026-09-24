// SPDX-FileCopyrightText: 2026 Kerim Bavcic
// SPDX-License-Identifier: AGPL-3.0-or-later

#include "openenoc_iss.h"

#include <algorithm>
#include <condition_variable>
#include <cstring>
#include <iostream>
#include <limits>
#include <map>
#include <memory>
#include <mutex>
#include <thread>
#include <vector>

#include "riscv/processor.h"
#include "riscv/simif.h"

static_assert(sizeof(openenoc_iss_config_t) == 40);
static_assert(sizeof(openenoc_iss_request_t) == 64);
static_assert(sizeof(openenoc_iss_response_t) == 64);
static_assert(sizeof(openenoc_iss_state_t) == 48);

namespace {

constexpr char kIsa[] = "RV32I";
constexpr char kPrivilege[] = "M";
constexpr reg_t kDmemBase = 0x10000000;
constexpr reg_t kDmemSize = 0x00008000;
constexpr reg_t kCsrBase = 0x20000000;
constexpr reg_t kCsrSize = 0x00002000;
constexpr size_t kRegisterCount = 32;

bool range_contains(reg_t base, reg_t region_size, reg_t address, size_t size)
{
    return address >= base && size <= region_size &&
        address - base <= region_size - size;
}

bool valid_header(uint32_t abi_version, uint32_t struct_size, size_t expected)
{
    return abi_version == OPENENOC_ISS_ABI_VERSION && struct_size >= expected;
}

class Endpoint final : public simif_t
{
public:
    explicit Endpoint(const openenoc_iss_config_t &input)
        : endpoint_id_(input.endpoint_id),
          imem_base_(input.imem_base),
          reset_pc_(input.reset_pc),
          memory_(static_cast<size_t>(input.imem_size), 0)
    {
        debug_mmu = nullptr;
        config_.isa = kIsa;
        config_.priv = kPrivilege;
        config_.endianness = endianness_little;
        config_.mem_layout = {mem_cfg_t(input.imem_base, input.imem_size)};
        config_.hartids = {0};
        config_.explicit_hartids = true;
        config_.start_pc.set_global(input.reset_pc);

        processor_ = std::make_unique<processor_t>(
            kIsa, kPrivilege, &config_, this, 0, false, nullptr, std::cerr);
        harts_.emplace(0, processor_.get());
        processor_->get_state()->pc = reset_pc_;
        snapshot_pc_ = reset_pc_;
    }

    ~Endpoint() override
    {
        request_stop();
        if (worker_.joinable()) {
            worker_.join();
        }
    }

    Endpoint(const Endpoint &) = delete;
    Endpoint &operator=(const Endpoint &) = delete;

    int32_t load_image(uint64_t address, const uint8_t *data, uint64_t size)
    {
        std::lock_guard lock(mutex_);
        if (run_state_ == OPENENOC_ISS_STATE_RUNNING ||
                run_state_ == OPENENOC_ISS_STATE_WAITING_MMIO) {
            return OPENENOC_ISS_INVALID_STATE;
        }
        if (data == nullptr || size == 0 || address < imem_base_ ||
                size > memory_.size() ||
                address - imem_base_ > memory_.size() - size) {
            return OPENENOC_ISS_OUT_OF_RANGE;
        }

        std::memcpy(memory_.data() + address - imem_base_, data,
                    static_cast<size_t>(size));
        return OPENENOC_ISS_OK;
    }

    int32_t start(uint64_t entry_pc, uint64_t max_steps)
    {
        if (max_steps == 0 || !range_contains(
                imem_base_, memory_.size(), entry_pc, sizeof(uint32_t))) {
            return OPENENOC_ISS_OUT_OF_RANGE;
        }

        {
            std::lock_guard lock(mutex_);
            if (run_state_ == OPENENOC_ISS_STATE_RUNNING ||
                    run_state_ == OPENENOC_ISS_STATE_WAITING_MMIO) {
                return OPENENOC_ISS_INVALID_STATE;
            }
        }

        if (worker_.joinable()) {
            worker_.join();
        }

        std::lock_guard lock(mutex_);
        processor_->reset();
        processor_->get_state()->pc = entry_pc;
        ++epoch_;
        next_request_id_ = 1;
        step_count_ = 0;
        snapshot_pc_ = entry_pc;
        pending_active_ = false;
        pending_claimed_ = false;
        response_ready_ = false;
        stop_requested_ = false;
        fatal_error_ = false;
        run_state_ = OPENENOC_ISS_STATE_RUNNING;

        try {
            worker_ = std::thread(&Endpoint::run, this, max_steps);
        } catch (...) {
            run_state_ = OPENENOC_ISS_STATE_ERROR;
            return OPENENOC_ISS_INTERNAL_ERROR;
        }
        return OPENENOC_ISS_OK;
    }

    int32_t request_stop()
    {
        std::lock_guard lock(mutex_);
        stop_requested_ = true;
        if (run_state_ == OPENENOC_ISS_STATE_READY) {
            run_state_ = OPENENOC_ISS_STATE_STOPPED;
        }
        response_cv_.notify_all();
        return OPENENOC_ISS_OK;
    }

    int32_t try_poll(openenoc_iss_request_t *request)
    {
        if (!valid_header(request->abi_version, request->struct_size,
                          sizeof(*request))) {
            return OPENENOC_ISS_INVALID_ARGUMENT;
        }

        std::lock_guard lock(mutex_);
        if (!pending_active_ || pending_claimed_) {
            return OPENENOC_ISS_NOT_READY;
        }

        *request = pending_request_;
        pending_claimed_ = true;
        return OPENENOC_ISS_OK;
    }

    int32_t complete(const openenoc_iss_response_t &response)
    {
        if (!valid_header(response.abi_version, response.struct_size,
                          sizeof(response))) {
            return OPENENOC_ISS_INVALID_ARGUMENT;
        }

        std::lock_guard lock(mutex_);
        if (!pending_active_ || !pending_claimed_ || response_ready_) {
            return OPENENOC_ISS_INVALID_STATE;
        }
        if (response.endpoint_id != endpoint_id_ || response.epoch != epoch_ ||
                response.request_id != pending_request_.request_id ||
                response.size_bytes != pending_request_.size_bytes) {
            return OPENENOC_ISS_INVALID_ARGUMENT;
        }

        pending_response_ = response;
        response_ready_ = true;
        response_cv_.notify_one();
        return OPENENOC_ISS_OK;
    }

    int32_t try_state(openenoc_iss_state_t *state)
    {
        if (!valid_header(state->abi_version, state->struct_size,
                          sizeof(*state))) {
            return OPENENOC_ISS_INVALID_ARGUMENT;
        }

        std::lock_guard lock(mutex_);
        *state = {
            .abi_version = OPENENOC_ISS_ABI_VERSION,
            .struct_size = sizeof(*state),
            .endpoint_id = endpoint_id_,
            .run_state = run_state_,
            .epoch = epoch_,
            .step_count = step_count_,
            .pc = snapshot_pc_,
            .pending_request_id = pending_active_
                ? pending_request_.request_id : 0,
        };
        return OPENENOC_ISS_OK;
    }

    int32_t read_register(uint32_t index, uint64_t *value)
    {
        if (value == nullptr || index >= kRegisterCount) {
            return OPENENOC_ISS_INVALID_ARGUMENT;
        }

        std::lock_guard lock(mutex_);
        if (run_state_ == OPENENOC_ISS_STATE_RUNNING ||
                run_state_ == OPENENOC_ISS_STATE_WAITING_MMIO) {
            return OPENENOC_ISS_INVALID_STATE;
        }
        *value = processor_->get_state()->XPR[index];
        return OPENENOC_ISS_OK;
    }

    char *addr_to_mem(reg_t address) override
    {
        if (!range_contains(imem_base_, memory_.size(), address, 1)) {
            return nullptr;
        }
        return reinterpret_cast<char *>(
            memory_.data() + address - imem_base_);
    }

    bool mmio_fetch(reg_t, size_t, uint8_t *) override
    {
        std::lock_guard lock(mutex_);
        fatal_error_ = true;
        return false;
    }

    bool mmio_load(reg_t address, size_t size, uint8_t *bytes) override
    {
        return transact(OPENENOC_ISS_REQUEST_DATA_READ, address, size, bytes);
    }

    bool mmio_store(reg_t address, size_t size, const uint8_t *bytes) override
    {
        return transact(OPENENOC_ISS_REQUEST_DATA_WRITE, address, size,
                        const_cast<uint8_t *>(bytes));
    }

    void proc_reset(unsigned) override
    {
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

private:
    bool external_address(reg_t address, size_t size) const
    {
        return range_contains(kDmemBase, kDmemSize, address, size) ||
            range_contains(kCsrBase, kCsrSize, address, size);
    }

    bool transact(uint32_t kind, reg_t address, size_t size, uint8_t *bytes)
    {
        if ((size != 1 && size != 2 && size != 4) ||
                !external_address(address, size)) {
            std::lock_guard lock(mutex_);
            fatal_error_ = true;
            return false;
        }

        std::unique_lock lock(mutex_);
        if (stop_requested_ || pending_active_) {
            return false;
        }

        pending_request_ = {};
        pending_request_.abi_version = OPENENOC_ISS_ABI_VERSION;
        pending_request_.struct_size = sizeof(pending_request_);
        pending_request_.endpoint_id = endpoint_id_;
        pending_request_.kind = kind;
        pending_request_.epoch = epoch_;
        pending_request_.request_id = next_request_id_++;
        pending_request_.address = address;
        pending_request_.pc = processor_->get_state()->pc;
        pending_request_.size_bytes = static_cast<uint32_t>(size);
        pending_request_.byte_enable = (UINT32_C(1) << size) - 1;
        if (kind == OPENENOC_ISS_REQUEST_DATA_WRITE) {
            std::copy_n(bytes, size, pending_request_.data);
        }

        pending_active_ = true;
        pending_claimed_ = false;
        response_ready_ = false;
        run_state_ = OPENENOC_ISS_STATE_WAITING_MMIO;

        response_cv_.wait(lock, [this] {
            return response_ready_ || stop_requested_;
        });

        if (stop_requested_ && !response_ready_) {
            pending_active_ = false;
            pending_claimed_ = false;
            return false;
        }

        const bool success =
            pending_response_.status == OPENENOC_ISS_RESPONSE_OK &&
            pending_response_.axi_resp == 0;
        if (success && kind == OPENENOC_ISS_REQUEST_DATA_READ) {
            std::copy_n(pending_response_.data, size, bytes);
        }
        if (!success && pending_response_.status !=
                OPENENOC_ISS_RESPONSE_CANCELLED) {
            fatal_error_ = true;
        }

        pending_active_ = false;
        pending_claimed_ = false;
        response_ready_ = false;
        run_state_ = OPENENOC_ISS_STATE_RUNNING;
        return success;
    }

    void run(uint64_t max_steps)
    {
        try {
            for (uint64_t step = 0; step < max_steps; ++step) {
                {
                    std::lock_guard lock(mutex_);
                    if (stop_requested_ || fatal_error_) {
                        break;
                    }
                }

                processor_->step(1);

                std::lock_guard lock(mutex_);
                ++step_count_;
                snapshot_pc_ = processor_->get_state()->pc;
                if (stop_requested_ || fatal_error_) {
                    break;
                }
            }

            std::lock_guard lock(mutex_);
            snapshot_pc_ = processor_->get_state()->pc;
            if (fatal_error_) {
                run_state_ = OPENENOC_ISS_STATE_ERROR;
            } else if (stop_requested_) {
                run_state_ = OPENENOC_ISS_STATE_STOPPED;
            } else {
                run_state_ = OPENENOC_ISS_STATE_COMPLETED;
            }
        } catch (...) {
            std::lock_guard lock(mutex_);
            run_state_ = OPENENOC_ISS_STATE_ERROR;
        }
    }

    uint32_t endpoint_id_;
    reg_t imem_base_;
    reg_t reset_pc_;
    cfg_t config_;
    std::vector<uint8_t> memory_;
    std::map<size_t, processor_t *> harts_;
    std::unique_ptr<processor_t> processor_;

    std::mutex mutex_;
    std::condition_variable response_cv_;
    std::thread worker_;
    uint32_t run_state_ = OPENENOC_ISS_STATE_READY;
    uint64_t epoch_ = 0;
    uint64_t next_request_id_ = 1;
    uint64_t step_count_ = 0;
    uint64_t snapshot_pc_ = 0;
    bool stop_requested_ = false;
    bool fatal_error_ = false;
    bool pending_active_ = false;
    bool pending_claimed_ = false;
    bool response_ready_ = false;
    openenoc_iss_request_t pending_request_ = {};
    openenoc_iss_response_t pending_response_ = {};
};

bool valid_config(const openenoc_iss_config_t *config)
{
    if (config == nullptr ||
            !valid_header(config->abi_version, config->struct_size,
                          sizeof(*config)) ||
            config->imem_size == 0 ||
            config->imem_size > std::numeric_limits<size_t>::max()) {
        return false;
    }

    return range_contains(config->imem_base, config->imem_size,
                          config->reset_pc, sizeof(uint32_t));
}

} // namespace

struct openenoc_iss
{
    std::unique_ptr<Endpoint> endpoint;
};

extern "C" uint32_t openenoc_iss_abi_version(void)
{
    return OPENENOC_ISS_ABI_VERSION;
}

extern "C" const char *openenoc_iss_status_string(int32_t status)
{
    switch (status) {
    case OPENENOC_ISS_OK:
        return "ok";
    case OPENENOC_ISS_NOT_READY:
        return "not ready";
    case OPENENOC_ISS_INVALID_ARGUMENT:
        return "invalid argument";
    case OPENENOC_ISS_INVALID_STATE:
        return "invalid state";
    case OPENENOC_ISS_OUT_OF_RANGE:
        return "out of range";
    case OPENENOC_ISS_INTERNAL_ERROR:
        return "internal error";
    default:
        return "unknown status";
    }
}

extern "C" int32_t openenoc_iss_create(
    const openenoc_iss_config_t *config,
    openenoc_iss_t **out_handle)
{
    if (!valid_config(config) || out_handle == nullptr) {
        return OPENENOC_ISS_INVALID_ARGUMENT;
    }

    try {
        auto handle = std::make_unique<openenoc_iss>();
        handle->endpoint = std::make_unique<Endpoint>(*config);
        *out_handle = handle.release();
        return OPENENOC_ISS_OK;
    } catch (...) {
        return OPENENOC_ISS_INTERNAL_ERROR;
    }
}

extern "C" void openenoc_iss_destroy(openenoc_iss_t *handle)
{
    delete handle;
}

extern "C" int32_t openenoc_iss_load_image(
    openenoc_iss_t *handle,
    uint64_t address,
    const uint8_t *data,
    uint64_t size)
{
    if (handle == nullptr) {
        return OPENENOC_ISS_INVALID_ARGUMENT;
    }
    try {
        return handle->endpoint->load_image(address, data, size);
    } catch (...) {
        return OPENENOC_ISS_INTERNAL_ERROR;
    }
}

extern "C" int32_t openenoc_iss_start(
    openenoc_iss_t *handle,
    uint64_t entry_pc,
    uint64_t max_steps)
{
    if (handle == nullptr) {
        return OPENENOC_ISS_INVALID_ARGUMENT;
    }
    try {
        return handle->endpoint->start(entry_pc, max_steps);
    } catch (...) {
        return OPENENOC_ISS_INTERNAL_ERROR;
    }
}

extern "C" int32_t openenoc_iss_request_stop(openenoc_iss_t *handle)
{
    if (handle == nullptr) {
        return OPENENOC_ISS_INVALID_ARGUMENT;
    }
    return handle->endpoint->request_stop();
}

extern "C" int32_t openenoc_iss_try_poll(
    openenoc_iss_t *handle,
    openenoc_iss_request_t *request)
{
    if (handle == nullptr || request == nullptr) {
        return OPENENOC_ISS_INVALID_ARGUMENT;
    }
    return handle->endpoint->try_poll(request);
}

extern "C" int32_t openenoc_iss_complete(
    openenoc_iss_t *handle,
    const openenoc_iss_response_t *response)
{
    if (handle == nullptr || response == nullptr) {
        return OPENENOC_ISS_INVALID_ARGUMENT;
    }
    return handle->endpoint->complete(*response);
}

extern "C" int32_t openenoc_iss_try_state(
    openenoc_iss_t *handle,
    openenoc_iss_state_t *state)
{
    if (handle == nullptr || state == nullptr) {
        return OPENENOC_ISS_INVALID_ARGUMENT;
    }
    return handle->endpoint->try_state(state);
}

extern "C" int32_t openenoc_iss_read_register(
    openenoc_iss_t *handle,
    uint32_t index,
    uint64_t *value)
{
    if (handle == nullptr) {
        return OPENENOC_ISS_INVALID_ARGUMENT;
    }
    return handle->endpoint->read_register(index, value);
}