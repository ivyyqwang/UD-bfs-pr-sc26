#!/usr/bin/env python3.10
# source credit: Jiya, Jerry
# modified by: Wenyi
import sys
import random
from pathlib import Path, PosixPath
import subprocess
import argparse


str_tab = "    "
max_int_64 = int('ffffffffffffffff', 16) -1
min_int_64 = -int('ffffffffffffffff', 16)
max_int_32 = int('ffffffff', 16) -1
min_int_32 = -int('ffffffff', 16)

max_int_16 = int('ffff', 16) -1
min_int_16 = -int('ffff', 16)

max_int_12 = int('fff', 16) -1
min_int_12 = -int('fff', 16)

max_int_4 = int('f', 16) -1
min_int_4 = -int('f', 16)

max_1_byte = int('ff', 16)
max_2_bytes = int('ffff', 16)
# max_bits = int(1 << 7)

local_memory_boundary = 4*1024*1024
local_bank_boundary = 1024*64
global_memory_boundary = 4*1024*1024

# parser = argparse.ArgumentParser(description="input generated instruction and the number")
# parser.add_argument("inst_type", type=str, help="the instruction to generated")
# parser.add_argument("inst_num", type=int, help="the number of the instructions to generated")
# args = parser.parse_args()

# inst_type = args.inst_type
# inst_num = args.inst_num
test_path = Path(f'../tests/inst_unit_tests/') # The c++ google test script
prog_path = Path('./efas/') # The directory to hold the efa programs
bin_path = Path("efa2bin.py")

def gen_efa_setup(prog_path: PosixPath, mode0, mode1, cat, dlen):
    fname = ''
    match cat:
        case 'send':
            fname = 'send_mode1_{}_dlen_{}()'
            fname = fname.format('cl' if mode1 else 'cw', dlen)
         
        case 'sendb':
            fname = 'sendb_mode1_{}_dlen_{}()'
            fname = fname.format('cl' if mode1 else 'cw',dlen)
          
        
        case 'sendr':
            fname = 'sendr_mode1_{}_numop_{}()'
            fname = fname.format('cl' if mode1 else 'cw', dlen)
     
        case 'sendops':
            fname = 'sendops_mode1_{}_numop_{}()'
            fname = fname.format('cl' if mode1 else 'cw', dlen)
   
        case 'sendm':
            fname = 'sendm_mode1_{}_mode0_{}_dlen_{}()'
            fname = fname.format('cl' if mode1 else 'cw', 'store' if mode0 else 'load', dlen)
   
            
        case 'sendmb':
            fname = 'sendmb_mode1_{}_mode0_{}_dlen_{}()'
            fname = fname.format('cl' if mode1 else 'cw', 'store' if mode0 else 'load', dlen)
       
        case 'sendmr':
            fname = 'sendmr_mode1_{}_mode0_{}_numop_{}()'
            fname = fname.format('cl' if mode1 else 'cw', 'store' if mode0 else 'load', dlen)
      
        case 'sendmops':
            # print('sendops')
            fname = 'sendmops_mode1_{}_mode0_{}_numop_{}()'
            fname = fname.format('cl' if mode1 else 'cw', 'store' if mode0 else 'load', dlen)
     
            
            
                  
    prog_lines = ["from EFA_v2 import *",
            f"def {fname}:",
            str_tab + "efa = EFA([])",
            str_tab + "efa.code_level = \"machine\"",
            str_tab + "state = State()",
            str_tab + "efa.add_initId(state.state_id)",
            str_tab + "efa.add_state(state)",
            str_tab + "event_map = {",
            str_tab + str_tab + "\"start_event\": 0,",
            str_tab + str_tab + "\"send_event\": 1,",
            str_tab + str_tab + "\"cont_event\": 2,",
            str_tab + "}",
        ]
    return prog_lines


def gen_test_setup(instruction: str):
	test_lines = ["#include <gtest/gtest.h>",
			"#include \"basim.hh\"",
			"#include \"types.hh\"",
			"#include \"lanetypes.hh\"",
            "#include \"udaccelerator.hh\"",
			"",
			"using namespace basim;",
			"",
			f"class {instruction.capitalize()} : public ::testing::Test {{",
			" protected:",
            str_tab + "void SetUp() override {",
            str_tab + str_tab + "m.NumLanes = numlanes;",
            str_tab + str_tab + "m.NumNodes = 1;",
            str_tab + str_tab + "m.NumUDs = 1;",
            str_tab + str_tab + "m.NumStacks = 1;",
            str_tab + str_tab + "m.LocalMemAddrMode = 1;",
            str_tab + str_tab + "sim = BASim(m);",
            str_tab + "}",
            str_tab + "BASim sim;",
            str_tab + "machine_t m;",
            str_tab + "int numlanes = 1;",
			"};"]
	return test_lines


# this is for coverage
# inner is for randomness
def gen_send(prog_lines, test_lines, mode0, mode1, cat='send', dlen=9, udid=0, tid=0, event_label=1):
    # Xc Xptr are regs, store values before entering this function
    # test OB values of lane1
    # also test OB values of lane0 cont_event
    # mode1 = 0,1; Xptr = 0,end, 2x rand; dlen=1,9, 2x rand
    # start_event (lane0)
    # construct Xe based on mode0, mode1, udid, tid, event_label
    # construct Xc based on mode1, and Xc, Xc default is label; if mode1==0, replace CEVW with label cont
    # write random values to LM, starting from Xptr, with length lenw
    # now do the send_event
    # yield
    args=[]
    # X16 = Xe
    # X17 = Xc = X8
    # X18 = Xptr = X9
    # X19 = X1 = X10
    # X20 = X2 = X11
    # X21 = X3 = X12
    # X22 - X31 = and LM has been written with random values
    Xe = "X16"
    # starting
    Xd = "X17"
    Xptr = "X18"
    Xc = "X19"
    X1 = "X20"
    X2 = "X21"
    X3 = "X22"
    prog_lines.extend([
        str_tab + f"tran0 = state.writeTransition(\"eventCarry\", state, state, event_map['start_event'])",
        str_tab + f"tran0.writeAction(\"evi X2 {Xe} {event_label} {0b0001}\")",
        # str_tab + f"tran0.writeAction(\"evii {Xe} {0xFF} {event_label} {0b0101}\")",
        str_tab + f"tran0.writeAction(\"evi {Xe} {Xe} {udid} {0b1000}\")",
	])
    for i in range(8):
        prog_lines.append(str_tab + f"tran0.writeAction(\"addi X{i+8} X{i+17} 0\")")
    prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 {Xptr} {Xptr}\")")
    if mode1 == 0:
        # complete event word from CEVW
        prog_lines.extend([
			str_tab + f"tran0.writeAction(\"evi X2 {Xc} 2 {0b0001}\")",
		])
    else:
        prog_lines.extend([
			str_tab + f"tran0.writeAction(\"evi X2 {Xc} 2 {0b0001}\")",
		])
        
        
    fname = ''
    match cat:
        case 'send':
            fname = 'send_mode1_{}_dlen_{}.py'
            fname = fname.format('cl' if mode1 else 'cw', dlen)
            prog_lines.extend([
                # str_tab + f"tran0.writeAction(\"print 'hello word'\")",
				str_tab + f"tran0.writeAction(\"send {Xe} {Xc} {Xptr} {dlen} {mode1}\")",
			])
            
        case 'sendb':
            fname = 'sendb_mode1_{}_dlen_{}.py'
            fname = fname.format('cl' if mode1 else 'cw',dlen)
            prog_lines.extend([
                str_tab + f"tran0.writeAction(\"sendb X16 X17 X18 {dlen} {mode1}\")",
			])
        
        case 'sendr':
            fname = 'sendr_mode1_{}_numop_{}.py'
            fname = fname.format('cl' if mode1 else 'cw', dlen)
            prog_lines.extend([
                str_tab + f"tran0.writeAction(\"sendr {Xe} {Xc} {X1} {X2} {X3} {mode1}\")",
			])
            
        case 'sendops':
            fname = 'sendops_mode1_{}_numop_{}.py'
            fname = fname.format('cl' if mode1 else 'cw', dlen)
            prog_lines.extend([
                str_tab + f"tran0.writeAction(\"sendops {Xe} {Xc} X8 {dlen} {mode1}\")",
			])
            

    # send_event (lane1)
    # which is just send without Xe is the current cont
    prog_lines.extend([
        str_tab + f"tran0.writeAction(\"movir X17 1\")",
        str_tab + f"tran0.writeAction(\"addi X7 X19 0\")",
        str_tab + f"tran0.writeAction(\"movrl X17 0(X19) 0 8\")",
        str_tab + f"tran0.writeAction(\"yield\")",])
       
    # send event ()
    prog_lines.extend([
        str_tab + f"tran1 = state.writeTransition(\"eventCarry\", state, state, event_map['send_event'])",
        str_tab + f"tran1.writeAction(\"addi X7 X16 0\")",
        ])
    for i in range(dlen):
        prog_lines.append(str_tab + f"tran1.writeAction(\"movrl X{8+i} 0(X16) 1 8\")")
    prog_lines.extend([
        str_tab + f"tran1.writeAction(\"movir X17 1\")",
        str_tab + f"tran1.writeAction(\"addi X7 X19 0\")",
        str_tab + f"tran1.writeAction(\"movrl X17 0(X19) 0 8\")",
		str_tab + f"tran1.writeAction(\"yieldt\")",
  		str_tab + f"tran2= state.writeTransition(\"eventCarry\", state, state, event_map['cont_event'])",
	    str_tab + f"tran2.writeAction(\"movir X17 1\")",
        str_tab + f"tran2.writeAction(\"addi X7 X19 0\")",
        str_tab + f"tran2.writeAction(\"movrl X17 0(X19) 0 8\")",
		str_tab + f"tran2.writeAction(\"yieldt\")",
        str_tab + f"return efa",
	])
    
    # testline
    
    args = [2, random.randint(0, local_bank_boundary - 9 * 8),
            random.randint(min_int_64, max_int_64), random.randint(min_int_64, max_int_64), 
            random.randint(min_int_64, max_int_64), random.randint(min_int_64, max_int_64),
            random.randint(min_int_64, max_int_64), random.randint(min_int_64, max_int_64)]
        # for values in SP
    for arg in range(1):
        test_name = '{}_{}{}{}'.format(cat.capitalize(), mode0, mode1, dlen)
        test_lines.extend([f"TEST_F({cat.capitalize()}, {test_name}){{",
                        str_tab + f"sim.initMachine(\"testprogs/binaries/{fname.split('.')[0]}.bin\", 0);",
                        str_tab + f"sim.initMemoryArrays();",
                        #    str_tab + f"printf(\"Hello\\n\");",
                        str_tab + f"for (int i = 0; i < numlanes; i++){{",
                        str_tab*2 + f"int numops = 8;",
                        str_tab*2 + f"eventword_t ev(0);",
                        str_tab*2 + f"ev.setNumOperands(numops);",
                        str_tab*2 + f"ev.setThreadID(0xFF);",
                        str_tab*2 + f"ev.setNWIDbits(i);",
                        #    str_tab*2 + f"printf(\"Hello2\");",
                        str_tab*2 + f"operands_t ops(numops);",
                        str_tab*2 + f"word_t* data = new word_t[numops];",
                        str_tab*2 + f"word_t* sp_data = new word_t[8];",
                        str_tab*2 + f"Addr Xptr = {args[0]};",
        ])
        for i in range(8):
            test_lines.append(str_tab + f"data[{i}] = (word_t){i};")
        for i in range(8):
            test_lines.append(str_tab + f"sp_data[{i}] = {args[i]};")
        
        # test_lines.append(str_tab + f"sim.t2ud_memcpy(Xptr, {args[i+5]}, {dlen});")
        test_lines.extend([
                        str_tab + "ops.setData(data);",
                        str_tab + "eventoperands_t eops(&ev, &ops);",
                        #    str_tab + "printf(\"Hello3\");",
                        str_tab + "networkid_t nwid = NetworkID(i);",
                        #    str_tab + "printf(\"Hello4\");",
                        str_tab + "sim.pushEventOperands(nwid, eops);}",
                        str_tab + "sim.simulate();",
                        str_tab + "bool status;",
                        str_tab + "while(1){",
                        str_tab + "status = true;",
                        str_tab + "for(int i = 0; i < numlanes; i++){",
                        str_tab + str_tab + "uint64_t val;",
                        str_tab + str_tab + "sim.ud2t_memcpy(&val, 8, NetworkID(i), 0);",
                        str_tab + str_tab + "status = status && (val == 1);",
                        str_tab + "}",
                        str_tab + f"printf(\"{test_name}%d\\n\", status);",
                        str_tab + "if(status) break;",
                        str_tab + "}",
        ])
        
        # assertions
        # Assert OB values of lane1
        # Assert CCONT value of lane1
        if cat == 'sendr':
            for i in range(3):
                pass
                test_lines.append(str_tab + f"EXPECT_EQ(sim.testSPMem(0, 0, 1), true);")
        else:
            for i in range(dlen):
                pass
                # test_lines.append(str_tab + f"EXPECT_EQ(sim.readScratchPad(Xptr, {dlen}), {args[i+5]});",)
        
        test_lines.append("}")
    with open(prog_path.joinpath(fname), 'w') as writer:
        # print(f"write {fname}")
        # print(prog_lines)
        writer.writelines('\n'.join(prog_lines) + '\n')
    # save this to the file with filename = send{b,r,ops, None}_{mode1_str}_{Xptr_str}_{dlen_str}.py
    
    # append test_lines with the assertions
    return args
 
def gen_sendgtest_args():
    args = {}
    # coverage tests
    # interlane communication
    # case 0: same lane event0 create child event1, event1 write to scratchpad, num thread = 1
    # case 1: both lanes init from event0, e1 created on the other lane, write to SP, num thread = 2
    # case 3: same lane, t0 init e0, create e1, e1 write to SP, return to t0e2, e2 write to different SP
    # case 4: both lanes t0 e0, create e1 on the other lane, e1 write to SP, return to t0e2, write to different SP
    
    # Xe = {0, 1, ...}{255, (0, 1)}{}{1} x # nwid ,tid ,numops ,evlabel(created by 0)
    # Xc = {0, 1, ...}{255, (0, 1)}{}{2} x # nwid ,tid ,numops ,evlabel(created by 1)
    # Xptr = {0, end, rand*3}
    # X1, X2, X3 = {min, max, rand values * 3}
    # case0:
    # num_lanes = 1, tid=255, 
    return {}

def send_template():
    
    template = """from EFA_v2 import *
    def {fname}():
        efa = EFA([])
        efa.code_level = "machine"
        state = State()
        efa.add_initId(state.state_id)
        efa.add_state(state)
        event_map = {{
            "start_event": 0,
            "send_event": 1,
            "cont_event": 2,
        }}
        tran0 = state.writeTransition("eventCarry", state, state, event_map['start_event'])
    """
    
    for i in range(8):
        template += str_tab + f"tran0.writeAction(\"addi X{i+8} X{i+17} 0\")"
    
    return template

    pass
def gen_sendm(prog_lines, test_lines, mode0, mode1, cat='sendm', dlen=8, udid=0, tid=255, event_label=1):
    # X16 = Xe
    # X17 = Xc = X8
    # X18 = Xptr = X9
    # X19 = Xd = X10
    # X20 = X1 = X11
    # X21 = X2 = X12
    Xe = "X16"
    # starting
    Xd = "X17"
    Xptr = "X18"
    Xc = "X19"
    X1 = "X20"
    X2 = "X21"
    X3 = "X22"
    
    
    args = [random.randint(0, global_memory_boundary - 9 * 8), random.randint(0, local_memory_boundary - 9 * 8), 
            2 , random.randint(min_int_64, max_int_64), 
            random.randint(min_int_64, max_int_64), random.randint(min_int_64, max_int_64),
            random.randint(min_int_64, max_int_64), random.randint(min_int_64, max_int_64)]
          
    # for values in SP
    args.extend([random.randint(min_int_64, max_int_64) for i in range(dlen)])
    prog_lines.extend([
        str_tab + f"tran0 = state.writeTransition(\"eventCarry\", state, state, event_map['start_event'])",
	])
    for i in range(8):
        prog_lines.append(str_tab + f"tran0.writeAction(\"addi X{i+8} X{i+17} 0\")")
    
    prog_lines.extend([
        str_tab + f"tran0.writeAction(\"evi X2 {Xe} {event_label} {0b0}\")",
        str_tab + f"tran0.writeAction(\"evi {Xe} {tid} {0b0100}\")",
	])
    if mode1 == 0:
        # complete event word from CEVW
        # print()
        prog_lines.extend([
			str_tab + f"tran0.writeAction(\"evi X2 {Xc} 2 {0b0001}\")",
		])
    else:
        # TODO: generate Xc from TOP
        prog_lines.extend([
			str_tab + f"tran0.writeAction(\"evi X2 {Xc} 2 {0b0001}\")",
		])
        
    prog_lines.extend([
        str_tab + f"tran0.writeAction(\"addi X7 {Xptr} 0\")",
	])
    fname = '{}_{}_Xptr_{}_dlen_{}.py'
    match cat:
        case 'sendm':
            fname = 'sendm_mode1_{}_mode0_{}_dlen_{}.py'
            fname = fname.format('cl' if mode1 else 'cw', 'store' if mode0 else 'load', dlen)
            prog_lines.extend([
				str_tab + f"tran0.writeAction(\"sendm {Xd} {Xc} {Xptr} {dlen} {2 * mode1 + mode0}\")",
			])
            
        case 'sendmb':
            fname = 'sendmb_mode1_{}_mode0_{}_dlen_{}.py'
            fname = fname.format('cl' if mode1 else 'cw', 'store' if mode0 else 'load', dlen)
            prog_lines.extend([
                str_tab + f"tran0.writeAction(\"sendmb {Xd} {Xc} {Xptr} {dlen} {2 * mode1 + mode0}\")",
			])
        
        case 'sendmr':
            fname = 'sendmr_mode1_{}_mode0_{}_numop_{}.py'
            fname = fname.format('cl' if mode1 else 'cw', 'store' if mode0 else 'load', dlen)
            prog_lines.extend([
                str_tab + f"tran0.writeAction(\"print '%d %d %d %d' {Xd} {Xc} {X1} {X2}\")",
                str_tab + f"tran0.writeAction(\"sendmr {Xd} {Xc} {X1} {X2} {mode1}\")",
			])
            # print(2*mode1 + mode0)
        case 'sendmops':
            # print('sendops')
            fname = 'sendmops_mode1_{}_mode0_{}_numop_{}.py'
            fname = fname.format('cl' if mode1 else 'cw', 'store' if mode0 else 'load', dlen)
            prog_lines.extend([
                str_tab + f"tran0.writeAction(\"sendmops {Xd} {Xc} X8 {dlen} {2 * mode1 + mode0}\")",
			])
            

    # send_event (lane1)
    # which is just send without Xe is the current cont
    prog_lines.extend([
        str_tab + f"tran0.writeAction(\"yield\")",
        str_tab + f"tran1 = state.writeTransition(\"eventCarry\", state, state, event_map['send_event'])",
		str_tab + f"tran1.writeAction(\"addi X18 X18 1\")",
        str_tab + f"tran1.writeAction(\"yield\")",
  		str_tab + f"tran2= state.writeTransition(\"eventCarry\", state, state, event_map['cont_event'])",
        str_tab + f"tran2.writeAction(\"addi X18 X18 1\")",
        str_tab + f"tran2.writeAction(\"yieldt\")",
        str_tab + f"return efa",
	])
    
    # testline
    test_name = '{}{}{}{}'.format(cat.capitalize(), mode0, mode1, dlen)
    test_lines.extend([f"TEST_F({cat.capitalize()}, {test_name}){{",
                       str_tab + f"sim.initMachine(\"testprogs/binaries/{fname.split('.')[0]}.bin\", 0);",
                       str_tab + f"sim.initMemoryArrays();",
                    #    str_tab + f"word_t* buff = reinterpret_cast<word_t*>(sim.mm_malloc(4*1024*sizeof(word_t)));",
                       str_tab + f"word_t* buff = new word_t[numlanes];",
                       str_tab + f"printf(\"Addr of buff=%lx\\n\", buff);",
                       str_tab + f"for (int i = 0; i < numlanes; i++){{",
                       str_tab*2 + f"int numops = 8;",
                       str_tab*2 + f"eventword_t ev(0);",
                       str_tab*2 + f"ev.setNumOperands(numops);",
                       str_tab*2 + f"ev.setThreadID(0xFF);",
                       str_tab*2 + f"ev.setNWIDbits(i);",
                    #    str_tab*2 + f"printf(\"Hello2\");",
                       str_tab*2 + f"operands_t ops(numops);",
                       str_tab*2 + f"word_t* data = new word_t[numops];",
                       str_tab*2 + f"word_t* sp_data = new word_t[8];",
                    #    str_tab*2 + f"Addr Xptr = {args[0]};",
	])
    for i in range(8):
        test_lines.append(str_tab + f"data[{i}] = (word_t){i};")
    for i in range(8):
        test_lines.append(str_tab + f"sp_data[{i}] = {args[i]};")
    
    # test_lines.append(str_tab + f"sim.t2ud_memcpy(Xptr, {args[i+5]}, {dlen});")
    test_lines.extend([
                       str_tab + "ops.setData(data);",
                       str_tab + "ops.setDataWord(0, reinterpret_cast<uint64_t>(&buff[i]));",
                       str_tab + "eventoperands_t eops(&ev, &ops);",
                    #    str_tab + "printf(\"Hello3\");",
                       str_tab + "networkid_t nwid = NetworkID(i);",
                    #    str_tab + "printf(\"Hello4\");",
                       str_tab + "sim.pushEventOperands(nwid, eops);}",
                       str_tab + "sim.simulate();"
                    #    str_tab + "while(!sim.isIdle())",
                    #    str_tab + str_tab + "sim.tick();",
	])
    
    # assertions
    # Assert OB values of lane1
    # Assert CCONT value of lane1
    if cat == 'sendr':
        dlen = 2
    
    if mode0 == 0:
        # load, test the OBs
        for i in range(dlen):
            pass
            # test_lines.append(str_tab + f"EXPECT_EQ(ud0.readReg(X{8+i}, 1), {args[i+5]})",)
    elif mode0 == 1:
        # store, test the global memory
        for i in range(dlen):
            pass
            # test_lines.append(str_tab + f"EXPECT_EQ(ud0.readGlobalMem(Xd + {i}, 1), {args[i+5]})",)
    
    test_lines.append("}")
    with open(prog_path.joinpath(fname), 'w') as writer:
        # print(f"write {fname}")
        # print(prog_lines)
        writer.writelines('\n'.join(prog_lines) + '\n')
    # save this to the file with filename = send{b,r,ops, None}_{mode1_str}_{Xptr_str}_{dlen_str}.py
    
    # append test_lines with the assertions
    return args
    
    

def gen_unit_tests(prog_path: PosixPath, test_path: PosixPath):
    sends = ['send', 'sendr','sendops']
    modes=[0, 1]
    dlens = [2, 8]
    
    for send in sends:
        test_lines = gen_test_setup(instruction=send)
        for mode1 in modes:
            for dl in dlens:
                if send == "sendr" and mode1 == 0 and dl==2:
                    prog_lines = gen_efa_setup(prog_path,mode0=0, mode1=mode1, cat=send, dlen=dl)
                    gen_send(prog_lines, test_lines, mode0=0, mode1=mode1, cat=send, dlen=dl)
        with open(test_path.joinpath(send + "_test.cpp"), 'w') as writer:
            # print(test_lines)
            writer.writelines('\n'.join(test_lines) + '\n')
    sendms = ['sendm', 'sendmr', 'sendmops']
    for send in sendms:
        test_lines = gen_test_setup(instruction=send)
        for mode1 in modes:
            for mode0 in modes:
                for dl in dlens:
                    if send == 'sendmr' and mode0 == 0:
                        # sendmr is sending X1 and X2 to the global memory, only store supported
                        continue
                    prog_lines = gen_efa_setup(prog_path, mode0=mode0, mode1=mode1, cat=send, dlen=dl)
                    gen_sendm(prog_lines, test_lines, mode0=mode0, mode1=mode1, cat=send, dlen=dl)
        with open(test_path.joinpath(send + "_test.cpp"), 'w') as writer:
            # print(test_lines)
            writer.writelines('\n'.join(test_lines) + '\n')


if __name__ == '__main__':
    # Change path to your testing programs
    gen_unit_tests(prog_path=prog_path, test_path=test_path)
    send_template()








