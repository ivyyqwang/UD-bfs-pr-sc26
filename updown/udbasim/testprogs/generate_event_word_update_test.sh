#!/bin/bash

# How to generate bit manipulation test cases:
# 1. Run this script
# Check lines below. It should be `python3 testing_code_generator_event_word_update.py {BIT_MANI_INSTRUCTION} {NUM_TESTCASE}`
# It's using both fastsim and python to generate test cases.


UD_PATH=`pwd`/../..
export PYTHONPATH=$UD_PATH/linker:$PYTHONPATH
export LD_LIBRARY_PATH=$UD_PATH/install/updown/lib:$LD_LIBRARY_PATH

g++ test_top_event_word_update.cpp -I$UPDOWN_INSTALL_DIR/updown/include -L$UPDOWN_INSTALL_DIR/updown/lib -lUpDownSimRuntime -lUpDownRuntime /usr/lib/x86_64-linux-gnu/libpython3.10.so -o fastsim_exe
cp fastsim_exe ./efas/fastsim_exe


python3 testing_code_generator_event_word_update.py evi 5
python3 testing_code_generator_event_word_update.py evii 5
python3 testing_code_generator_event_word_update.py evlb 5
python3 testing_code_generator_event_word_update.py ev 5


rm -rf fastsim_exe
rm -rf ./efas/fastsim_exe
