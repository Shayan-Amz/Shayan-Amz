# Minimal Makefile for environments without CMake.  Equivalent targets:
#   make            build fp32calc and the test binary
#   make test       run the conformance tests (250 000 random pairs per family)
#   make clean

CXX      ?= g++
CXXFLAGS ?= -std=c++17 -O2 -Wall -Wextra -Wpedantic -Wshadow -Wconversion -Wsign-conversion
INCLUDES  = -Iinclude
BUILD     = build

.PHONY: all test clean

all: $(BUILD)/fp32calc $(BUILD)/test_fp32

$(BUILD):
	mkdir -p $(BUILD)

$(BUILD)/fp32calc: src/main.cpp include/fp32/fp32.hpp | $(BUILD)
	$(CXX) $(CXXFLAGS) $(INCLUDES) $< -o $@

$(BUILD)/test_fp32: tests/test_fp32.cpp include/fp32/fp32.hpp | $(BUILD)
	$(CXX) $(CXXFLAGS) -frounding-math $(INCLUDES) $< -o $@

test: $(BUILD)/test_fp32
	./$(BUILD)/test_fp32 250000

clean:
	rm -rf $(BUILD)
