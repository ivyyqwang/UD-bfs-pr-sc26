# Check generate_event_word_update_test.sh about how to generate event word update test cases

import sys
import random
from pathlib import Path, PosixPath
import subprocess
import argparse
import os
from ctypes import c_int16


str_tab     = "    "
max_uint64  = int('0xFFFFFFFFFFFFFFFF', 16)
mask_uint64 = int('0xFFFFFFFFFFFF0000', 16)
max_uint32  = int('0xFFFFFFFF', 16)
max_uint21  = int('0x1FFFFF', 16)
max_uint20  = int('0xFFFFF', 16)
max_uint16  = int('0xFFFF', 16)
max_uint12  = int('0xFFF', 16)
max_uint6   = int('0x3F', 16)
max_uint5   = int('0x1F', 16)
max_uint4   = int('0xF', 16)

def num_split_p0(num):
    return c_int16(num >> 48).value
def num_split_p1(num):
    return (num >> 36) & 0x0000000000000FFF
def num_split_p2(num):
    return (num >> 24) & 0x0000000000000FFF
def num_split_p3(num):
    return (num >> 12) & 0x0000000000000FFF
def num_split_p4(num):
    return num & 0x0000000000000FFF

parser = argparse.ArgumentParser(description="input generated instruction and the number")
parser.add_argument("inst_type", type=str, help="the instruction to generated")
parser.add_argument("inst_num", type=int, help="the number of the instructions to generated")
args = parser.parse_args()

inst_type = args.inst_type
inst_num = args.inst_num

# Change path to your testing programs
test_path = Path(f'../tests/inst_unit_tests/{inst_type}_test.cpp') # The c++ google test script
prog_path = Path('./efas/') # The directory to hold the efa programs
top_exe_path = Path('./fastsim_exe') # The top program to generate expected results


def generate_bin(efa_fname):
    os.chdir("../assembler/")
    os.system("python3 ./efa2bin.py --efa ../testprogs/efas/" + efa_fname + " --outpath ../testprogs/binaries/" )
    os.chdir("../testprogs/")
    print("Binary file generated at ./efas/" + efa_fname)
    print("=====================================================")
    return

def generate_efa_unit_test(test_path: PosixPath, fpath: PosixPath, instruction: str, args: list, iter: int):
    match instruction:
        case "evii":
            prog_lines = ["from EFA_v2 import *",
                f"def {fpath.stem}():",
                str_tab + "efa = EFA([])",
                str_tab + "efa.code_level = \"machine\"",
                str_tab + "state = State()",
                str_tab + "efa.add_initId(state.state_id)",
                str_tab + "efa.add_state(state)",
                str_tab + "event_map = {",
                str_tab + str_tab + "\"launch_events\": 0,",
                str_tab + str_tab + f"\"finish_events\": {max(1, args[2] & 0xFFFFF)}",
                str_tab + "}",
                str_tab + "tran0 = state.writeTransition(\"eventCarry\", state, state, event_map['launch_events'])"]
        case _:
            prog_lines = ["from EFA_v2 import *",
                f"def {fpath.stem}():",
                str_tab + "efa = EFA([])",
                str_tab + "efa.code_level = \"machine\"",
                str_tab + "state = State()",
                str_tab + "efa.add_initId(state.state_id)",
                str_tab + "efa.add_state(state)",
                str_tab + "event_map = {",
                str_tab + str_tab + "\"launch_events\": 0,",
                str_tab + str_tab + f"\"finish_events\": {max(1, args[2] & 0xFFFFF)}",
                str_tab + "}",
                str_tab + "tran0 = state.writeTransition(\"eventCarry\", state, state, event_map['launch_events'])"]

    test_lines = [f"TEST_F({instruction.upper()}, random_{iter}){{",
            str_tab + f"lane0.initSetup(0,\"testprogs/binaries/{fpath.stem}.bin\", 0);",
            str_tab + "uint8_t numop = 2;",
            str_tab + "eventword_t ev0(0);",
            str_tab + "ev0.setNumOperands(numop);",
            str_tab + "operands_t op0(numop);",
            str_tab + "word_t* data = new word_t[numop];",
            str_tab + "for(auto i = 0; i < numop; i++)",
            str_tab + str_tab + "data[i] = i+5;",

            str_tab + "op0.setData(data);",
            str_tab + "eventoperands_t eops(&ev0, &op0);",
            str_tab + "lane0.pushEventOperands(eops);",

            str_tab + "while(!lane0.isIdle())",
            str_tab + str_tab + "lane0.tick();"]

    generate_efa(instruction, prog_lines, args)
    prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")
    prog_lines.append(str_tab + "tran0 = state.writeTransition(\"eventCarry\", state, state, event_map['finish_events'])")
    prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")
    prog_lines.append(str_tab + "return efa")

    with open(fpath, 'w') as writer:
        writer.writelines('\n'.join(prog_lines) + '\n')

    return test_lines

def generate_output(instruction: str, args: list):
    output = []
    match instruction:
        case "evii":
            return output
        case "evi":
            return output
        case "evlb":
            return output
        case "ev":
            return output
        case _:
            print("Instruction not implemented yet or not belong to event word update, exit.")
            sys.exit()
    return output

def generate_output_efa(fname):
    # os.system(f"./{top_exe_path} {fname} > /local/tonyztc/output0.txt")
    os.chdir("./efas/")
    p = subprocess.Popen([f"./{top_exe_path}", fname], stdout=subprocess.PIPE)
    out, _ = p.communicate()
    s = out.decode('ascii').split('\n')
    ind = -1
    for j in range(len(s)):
        if s[-1-j] == '[yieldt,]':
            ind = -2-j
            break
    output = s[ind].split(':')[-1].split(',')
    os.chdir("..")
    return output

def generate_random_efa(instruction: str, fpath: PosixPath, count: int):
    args_list, output_list = [], []
    for i in range(count):
        args = generate_random_args(instruction)
        args_list.append(args)

        test_lines = generate_efa_unit_test(test_path, fpath.joinpath(f'{instruction}_{i}.py'), instruction, args, i)
        generate_bin(f'{instruction}_{i}.py')
        # output = generate_output(instruction, args)
        # print(output)
        match instruction:
            case "evlb":
                output_efa = []
            case _:
                output_efa = generate_output_efa(f'{instruction}_{i}')
        # print(output_efa)
        # for j in range(len(output)):
        #     if output[j] != 0xFFFFFFFFFFFFFFFF & int(output_efa[j]):
        #         print("Error: output not match")
        #         print(f"input: {args}")
        #         print(f"output: {output}")
        #         print(f"output_efa: {output_efa}")
        #         print(f"{output[j]} != {0xFFFFFFFFFFFFFFFF & int(output_efa[j])}")
        #         print(f"{bin(output[j])} != {bin(0xFFFFFFFFFFFFFFFF & int(output_efa[j]))}")
        #         sys.exit()
        output_list.append([int(o_efa) for o_efa in output_efa])

        # generate_assertion(instruction, test_lines, output, output_efa)
        generate_assertion(instruction, test_lines, args, output_efa)
        with open(test_path, 'a') as test_writer:
          test_writer.writelines('\n'.join(test_lines) + '\n')

    return args_list, output_list



##################################################
# To add unit tests with random input, implement following three functions
# Add the instruction in the match cases
# Naming as
# generage_efa
# generate_random_args
# generate_assertion
##################################################

# Add the efa program in the corresponding case
def generate_efa(instruction: str, prog_lines: list, args: list):
    prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 {12} {num_split_p1(args[0])}\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 {12} {num_split_p2(args[0])}\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 {12} {num_split_p3(args[0])}\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 {12} {num_split_p4(args[0])}\")")

    prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {num_split_p0(args[1])}\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 {12} {num_split_p1(args[1])}\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 {12} {num_split_p2(args[1])}\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 {12} {num_split_p3(args[1])}\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 {12} {num_split_p4(args[1])}\")")

    match instruction:
        case "evii":
            prog_lines.append(str_tab + f"tran0.writeAction(\""+instruction+f" X16 {args[2]} {args[3]} {args[4]}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
        case "evi":
            prog_lines.append(str_tab + f"tran0.writeAction(\""+instruction+f" X16 X17 {args[2]} {args[3]}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
        case "evlb":
            prog_lines.append(str_tab + f"tran0.writeAction(\""+instruction+f" X16 {args[2]}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
        case "ev":
            prog_lines.append(str_tab + f"tran0.writeAction(\"movir X18 {num_split_p0(args[2])}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 {12} {num_split_p1(args[2])}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 {12} {num_split_p2(args[2])}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 {12} {num_split_p3(args[2])}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 {12} {num_split_p4(args[2])}\")")

            prog_lines.append(str_tab + f"tran0.writeAction(\"movir X19 {num_split_p0(args[3])}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X19 X19 {12} {num_split_p1(args[3])}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X19 X19 {12} {num_split_p2(args[3])}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X19 X19 {12} {num_split_p3(args[3])}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X19 X19 {12} {num_split_p4(args[3])}\")")

            prog_lines.append(str_tab + f"tran0.writeAction(\""+instruction+f" X16 X17 X18 X19 {args[4]}\")")
            prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d,%d,%d' {'X16'} {'X17'} {'X18'} {'X19'}\")")
        case _:
            print("Instruction not implemented yet or not belong to event word update, exit.")
            sys.exit()
    return


# Add code to generate corresponding random arguments
def generate_random_args(instruction: str) -> list:
    args = [random.randint(0, max_uint64), 
            random.randint(0, max_uint64)]
    match instruction:
        case "evii":
            args.append(random.randint(0, max_uint12))
            args.append(random.randint(0, max_uint12))
            args.append(2**random.randint(0, 3))
            while args[-1] == 1 or args[-1] == 2 or args[-1] == 4 or args[-1] == 8:
                args[-1] = args[-1] | (2**random.randint(0, 3))
            if args[-1] & 0x1:
                args[-3] = random.randint(0, max_uint20)
        case "evi":
            args.append(random.randint(0, max_uint12))
            args.append(2**random.randint(0, 3))
        case "evlb":
            args.append(random.randint(0, max_uint20))
        case "ev":
            args.append(random.randint(0, max_uint64))
            args.append(random.randint(0, max_uint64))
            args.append(2**random.randint(0, 3))
        case _:
            print("Instruction not implemented yet or not belong to bit manipulation, exit.")
            sys.exit()
    return args


# Add google test code to assert the output
# def generate_assertion(instruction: str, test_lines: list, output: list, output_efa: list):
def generate_assertion(instruction: str, test_lines: list, args: list, output_efa: list):
    match instruction:
        case "evii":
            test_lines.append(str_tab + f"EventWord new_ev(lane0.readReg(RegId::X2));")
            test_lines.append(str_tab + f"if ({args[-1]} & 0x8) {{")
            test_lines.append(str_tab + f"    new_ev.setNWIDbits({args[3]} & NWIDBITS);}}")
            test_lines.append(str_tab + f"if ({args[-1]} & 0x4) {{")
            test_lines.append(str_tab + f"    if ({args[-1]} & 0x8)")
            test_lines.append(str_tab + f"        new_ev.setThreadID({args[2]} & THREADIDBITS);")
            test_lines.append(str_tab + f"    else")
            test_lines.append(str_tab + f"        new_ev.setThreadID({args[3]} & THREADIDBITS);}}")
            test_lines.append(str_tab + f"if ({args[-1]} & 0x2) {{")
            test_lines.append(str_tab + f"    if ({args[-1]} & 0xC)")
            test_lines.append(str_tab + f"        new_ev.setNumOperands({args[2]} & NUMOPBITS);")
            test_lines.append(str_tab + f"    else")
            test_lines.append(str_tab + f"        new_ev.setNumOperands({args[3]} & NUMOPBITS);}}")
            test_lines.append(str_tab + f"if ({args[-1]} & 0x1) {{")
            test_lines.append(str_tab + f"    new_ev.setEventLabel({args[2]} & ELABELBITS);}}")

            # test_lines.append(str_tab + f"printf(\"new_ev.eventword: %lx\", new_ev.eventword);")
            # test_lines.append(str_tab + f"printf(\"    X16: %lx\", lane0.readReg(RegId::X16));")
            # test_lines.append(str_tab + f"printf(\"     X2: %lx\", lane0.readReg(RegId::X2));")
            # test_lines.append(str_tab + f"printf(\"    Args: {args[-3]}   {args[-2]}   {args[-1]}\");")

            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X16, new_ev.eventword, 0xFFFFFFFFFFF00000));")
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X17, {int(0xFFFFFFFFFFFFFFFF & int(output_efa[1]))}u));")
        case "evi":
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X16, {int(0xFFFFFFFFFFFFFFFF & int(output_efa[0]))}u));")
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X17, {int(0xFFFFFFFFFFFFFFFF & int(output_efa[1]))}u, 0xFFFFFFFFFFF00000));")
        case "evlb":
            test_lines.append(str_tab + f"EventWord new_ev({args[0]}u);")
            test_lines.append(str_tab + f"new_ev.setEventLabel({args[2]} & ELABELBITS);")
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X16, new_ev.eventword, 0xFFFFFFFFFFF00000));")
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X17, {args[1]}u));")
        
        case "ev":
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X16, {int(0xFFFFFFFFFFFFFFFF & int(output_efa[0]))}u));")
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X17, {int(0xFFFFFFFFFFFFFFFF & int(output_efa[1]))}u));")
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X18, {int(0xFFFFFFFFFFFFFFFF & int(output_efa[2]))}u));")
            test_lines.append(str_tab + f"EXPECT_TRUE(lane0.testReg(RegId::X19, {int(0xFFFFFFFFFFFFFFFF & int(output_efa[3]))}u));")
        case _:
            print("Instruction not implemented yet or not belong to bit manipulation, exit.")
            sys.exit()

    test_lines.append("}")
    return


# A wrpper function to handle the unit test
def generate_random_unit_test(fpath: PosixPath, instruction: str, count: int=10):
    args_list, output_list = generate_random_efa(instruction, fpath, count)
    for args, out in zip(args_list, output_list):
        print(f'{args} -> {out}')


if __name__ == '__main__':
    # if not test_path.exists():
    lines = ["#include <gtest/gtest.h>",
            "#include \"udlane.hh\"",
            "#include \"types.hh\"",
            "#include \"lanetypes.hh\"",
            "",
            "using namespace basim;",
            "",
            f'class {inst_type.upper()} : public ::testing::Test {{',
            " protected:",
            str_tab + "size_t num_threads = 2;",
            str_tab + "UDLane lane0 = UDLane(0);",
            "};"]
    with open(test_path, 'w') as writer:
        writer.writelines('\n'.join(lines) + '\n')

    generate_random_unit_test(prog_path, inst_type, inst_num)

