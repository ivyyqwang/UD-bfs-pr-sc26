#!/bin/bash

# How to generate bit manipulation test cases:
# 1. Run this script
# Check lines below. It should be `python3 testing_code_generator_bit_manipulation.py {BIT_MANI_INSTRUCTION} {NUM_TESTCASE}`
# It's using both fastsim and python to generate test cases.


UD_PATH=`pwd`/../..
export PYTHONPATH=$UD_PATH/linker:$PYTHONPATH
export LD_LIBRARY_PATH=$UD_PATH/install/updown/lib:$LD_LIBRARY_PATH

g++ test_top_bit_manipulation.cpp -I$UPDOWN_INSTALL_DIR/updown/include -L$UPDOWN_INSTALL_DIR/updown/lib -lUpDownSimRuntime -lUpDownRuntime /usr/lib/x86_64-linux-gnu/libpython3.10.so -o fastsim_exe
cp fastsim_exe ./efas/fastsim_exe


python3 testing_code_generator_bit_manipulation.py sli 5
python3 testing_code_generator_bit_manipulation.py sri 5
python3 testing_code_generator_bit_manipulation.py slori 5
python3 testing_code_generator_bit_manipulation.py srori 5
python3 testing_code_generator_bit_manipulation.py slandi 5
python3 testing_code_generator_bit_manipulation.py srandi 5
python3 testing_code_generator_bit_manipulation.py slorii 5
python3 testing_code_generator_bit_manipulation.py srorii 5
python3 testing_code_generator_bit_manipulation.py slandii 5
python3 testing_code_generator_bit_manipulation.py srandii 5
python3 testing_code_generator_bit_manipulation.py sari 5
python3 testing_code_generator_bit_manipulation.py sr 5
python3 testing_code_generator_bit_manipulation.py sl 5
python3 testing_code_generator_bit_manipulation.py sar 5
python3 testing_code_generator_bit_manipulation.py andi 5
python3 testing_code_generator_bit_manipulation.py and 5
python3 testing_code_generator_bit_manipulation.py ori 5
python3 testing_code_generator_bit_manipulation.py or 5
python3 testing_code_generator_bit_manipulation.py xori 5
python3 testing_code_generator_bit_manipulation.py xor 5


rm -rf fastsim_exe
rm -rf ./efas/fastsim_exe
