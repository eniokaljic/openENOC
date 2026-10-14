# SPDX-FileCopyrightText: 2026 Kerim Bavcic
# SPDX-License-Identifier: AGPL-3.0-or-later

TOPLEVEL_LANG = verilog

override SIM := verilator
WAVES ?= 0

COCOTB_HDL_TIMEUNIT = 1ns
COCOTB_HDL_TIMEPRECISION = 1ps

include ../../../common/sim_paths.mk

REPO_DIR = ../../../..
ISS_DIR = ../..
HW_DIR = $(REPO_DIR)/hw
LIBS_DIR = $(REPO_DIR)/libs
CORE_DIR = $(HW_DIR)/rtl/core
ENDPOINT_DIR = $(HW_DIR)/rtl/endpoints
TAXI_AXI_DIR = $(LIBS_DIR)/taxi/src/axi/rtl
TAXI_AXIS_DIR = $(LIBS_DIR)/taxi/src/axis/rtl
TAXI_SYNC_DIR = $(LIBS_DIR)/taxi/src/sync/rtl
HAL_RTL_DIR = $(REPO_DIR)/build/hal/openenoc_endpoint_full/rtl
HAL_IF_DIR = $(REPO_DIR)/build/hal/rtl

COCOTB_TEST_MODULES = test_openenoc_iss
COCOTB_TOPLEVEL = test_openenoc_iss
MODULE = $(COCOTB_TEST_MODULES)
TOPLEVEL = $(COCOTB_TOPLEVEL)

VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_pkg.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr_pkg.sv
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_endpoint_if.sv
VERILOG_SOURCES += $(HAL_IF_DIR)/openenoc_switch_if.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_if.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_register.sv
VERILOG_SOURCES += $(TAXI_SYNC_DIR)/taxi_sync_reset.sv
VERILOG_SOURCES += $(TAXI_SYNC_DIR)/taxi_sync_signal.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_adapter.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_async_fifo.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_async_fifo_adapter.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axil_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_skid_buffer.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_rr_arbiter.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_addr.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_wr.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar_rd.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_crossbar.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_eth_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_cpuif_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_cpuif_axil_adapter.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_peer_lookup_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_dma_transfer_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_irq_event_if.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_endpoint_dma_engine.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_endpoint_peer_lookup.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_endpoint_irq_controller.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_endpoint_direct_axis.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_endpoint_oetp_engine.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_fifo.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_fifo_adapter.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_arb_mux.sv
VERILOG_SOURCES += $(TAXI_AXIS_DIR)/taxi_axis_demux.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axi_if.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axi_register_rd.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axi_register_wr.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axi_axil_adapter.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axi_axil_adapter_wr.sv
VERILOG_SOURCES += $(TAXI_AXI_DIR)/taxi_axi_axil_adapter_rd.sv
VERILOG_SOURCES += $(LIBS_DIR)/taxi/src/dma/rtl/taxi_dma_desc_if.sv
VERILOG_SOURCES += $(LIBS_DIR)/taxi/src/dma/rtl/taxi_axi_dma.sv
VERILOG_SOURCES += $(LIBS_DIR)/taxi/src/dma/rtl/taxi_axi_dma_rd.sv
VERILOG_SOURCES += $(LIBS_DIR)/taxi/src/dma/rtl/taxi_axi_dma_wr.sv
VERILOG_SOURCES += $(LIBS_DIR)/taxi/src/prim/rtl/taxi_arbiter.sv
VERILOG_SOURCES += $(LIBS_DIR)/taxi/src/prim/rtl/taxi_penc.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_endpoint_interface.sv
VERILOG_SOURCES += $(CORE_DIR)/openenoc_axil_ram.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr.sv
VERILOG_SOURCES += $(HAL_RTL_DIR)/openenoc_endpoint_full_csr_bridge.sv
VERILOG_SOURCES += $(ISS_DIR)/rtl/openenoc_iss_cpu_proxy.sv
VERILOG_SOURCES += $(ENDPOINT_DIR)/openenoc_endpoint_full.sv
VERILOG_SOURCES += test_openenoc_iss.sv

export PYTHONPATH := $(abspath $(ISS_DIR)/python):$(PYTHONPATH)
export OPENENOC_ISS_LIBRARY := $(abspath $(REPO_DIR)/build/dv/iss/lib/libopenenoc_iss.so)
export OPENENOC_FIRMWARE_ELF := \
	$(abspath $(REPO_DIR)/build/sw/openenoc_endpoint_full/csr_smoke.elf)
export OPENENOC_IRQ_FIRMWARE_ELF := \
	$(abspath $(REPO_DIR)/build/dv/iss/irq-firmware/openenoc_endpoint_full/csr_smoke.elf)
export OPENENOC_LINK_FIRMWARE_ELF := \
	$(abspath $(REPO_DIR)/build/dv/iss/firmware/openenoc_endpoint_full/iss_link.elf)
export OPENENOC_STARTUP_FIRMWARE_ELF := \
	$(abspath $(REPO_DIR)/build/dv/iss/firmware/openenoc_endpoint_full/iss_startup.elf)

ifneq ($(TWO_ENDPOINTS),)
	COMPILE_ARGS += -GTWO_ENDPOINTS=$(TWO_ENDPOINTS)
endif
ifneq ($(DUAL_LOOPBACK),)
	COMPILE_ARGS += -GDUAL_LOOPBACK=$(DUAL_LOOPBACK)
endif
EXTRA_ARGS += -Wall ../../../common/config.vlt
ifeq ($(WAVES), 1)
	EXTRA_ARGS += --trace
	EXTRA_ARGS += --trace-fst
	EXTRA_ARGS += --trace-structs
endif

include $(shell cocotb-config --makefiles)/Makefile.sim

# Extended clean
clean::
	@$(RM) -rf "$(SIM_OUTPUT)/sim_build" "$(SIM_OUTPUT)/__pycache__" "$(TMPDIR)"
