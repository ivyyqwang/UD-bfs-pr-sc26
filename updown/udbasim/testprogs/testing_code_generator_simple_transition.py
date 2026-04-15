import sys
import random
from pathlib import Path, PosixPath
import subprocess
import argparse
import os


transition_map1 = {
	"common_action_TX": 			"commonCarry_with_action",
	"common_noaction_TX": 			"commonCarry_with_action",
	"epsilon_action_TX":			"epsilonCarry_with_action",
	"epsilon_noaction_TX":			"epsilonCarry_with_action",
	"common_action_TX_maxSBP": 		"commonCarry_with_action",
	"common_noaction_TX_maxSBP": 	"commonCarry_with_action",
	"basic_action_TX":				"basic_with_action",
	"basic_action1_without_lastact_TX":	"basic_with_action",
	"basic_action2_without_lastact_TX":	"basic_with_action",
	"basic_action4_without_lastact_TX":	"basic_with_action",
	"basic_action8_without_lastact_TX":	"basic_with_action",
	"basic_action1_with_lastact_TX":	"basic_with_action",
	"basic_action2_with_lastact_TX":	"basic_with_action",
	"basic_action4_with_lastact_TX":	"basic_with_action",
	"basic_action8_with_lastact_TX":	"basic_with_action",
	"basic_action_TX_maxSBP":			"basic_with_action",
	"basic_action1_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action2_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action4_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action8_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_noaction1_with_lastact_TX":	"basic_with_action",
	"basic_noaction2_with_lastact_TX":	"basic_with_action",
	"basic_noaction4_with_lastact_TX":	"basic_with_action",
	"basic_noaction8_with_lastact_TX":	"basic_with_action",
	"basic_noaction1_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_noaction2_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_noaction4_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_noaction8_with_lastact_TX_maxSBP":	"basic_with_action",
	"flag_action1_with_lastact_TX":	"flagCarry_with_action",
	"flag_action2_with_lastact_TX":	"flagCarry_with_action",
	"flag_action4_with_lastact_TX":	"flagCarry_with_action",
	"flag_action8_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction1_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction2_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction4_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction8_with_lastact_TX":	"flagCarry_with_action",
	"common_event_common_TX":			"commonCarry_with_action",
	"refill_TX":			"refill_with_action",
	"refill_noaction_TX":	"refill_with_action",
	"refill_noaction_TX":	"refill_with_action",
	"SB_automatic_refill_TX": "basic_with_action",
	"common_event_common_TX_maxSBP":			"commonCarry_with_action",
}

transition_map2 = {
	"common_action_TX": 			"commonCarry_with_action",
	"common_noaction_TX": 			"commonCarry",
	"epsilon_action_TX":			"epsilonCarry_with_action",
	"epsilon_noaction_TX":			"epsilonCarry",
	"common_action_TX_maxSBP": 		"commonCarry_with_action",
	"common_noaction_TX_maxSBP": 	"commonCarry",
	"basic_action_TX":				"basic_with_action",
	"basic_action1_without_lastact_TX":	"basic_with_action",
	"basic_action2_without_lastact_TX":	"basic_with_action",
	"basic_action4_without_lastact_TX":	"basic_with_action",
	"basic_action8_without_lastact_TX":	"basic_with_action",
	"basic_action1_with_lastact_TX":	"basic_with_action",
	"basic_action2_with_lastact_TX":	"basic_with_action",
	"basic_action4_with_lastact_TX":	"basic_with_action",
	"basic_action8_with_lastact_TX":	"basic_with_action",
	"basic_action_TX_maxSBP":			"basic_with_action",
	"basic_action1_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action2_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action4_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action8_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_noaction1_with_lastact_TX":	"basic",
	"basic_noaction2_with_lastact_TX":	"basic",
	"basic_noaction4_with_lastact_TX":	"basic",
	"basic_noaction8_with_lastact_TX":	"basic",
	"basic_noaction1_with_lastact_TX_maxSBP":	"basic",
	"basic_noaction2_with_lastact_TX_maxSBP":	"basic",
	"basic_noaction4_with_lastact_TX_maxSBP":	"basic",
	"basic_noaction8_with_lastact_TX_maxSBP":	"basic",
	"flag_action1_with_lastact_TX":	"flagCarry_with_action",
	"flag_action2_with_lastact_TX":	"flagCarry_with_action",
	"flag_action4_with_lastact_TX":	"flagCarry_with_action",
	"flag_action8_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction1_with_lastact_TX":	"flagCarry",
	"flag_noaction2_with_lastact_TX":	"flagCarry",
	"flag_noaction4_with_lastact_TX":	"flagCarry",
	"flag_noaction8_with_lastact_TX":	"flagCarry",
	"common_event_common_TX":			"commonCarry_with_action",
	"refill_TX":					"refill_with_action",
	"refill_noaction_TX":	"refill",
	"SB_automatic_refill_TX": "basic_with_action",
	"common_event_common_TX_maxSBP":			"commonCarry_with_action",
	
}

transition_map3 = {
	"common_action_TX": 			"commonCarry_with_action",
	"common_noaction_TX": 			"commonCarry_with_action",
	"epsilon_action_TX":			"epsilonCarry_with_action",
	"epsilon_noaction_TX":			"epsilonCarry_with_action",
	"common_action_TX_maxSBP": 		"commonCarry_with_action",
	"common_noaction_TX_maxSBP": 	"commonCarry",
	"basic_action_TX":				"basic_with_action",
	"basic_action1_without_lastact_TX":	"basic_with_action",
	"basic_action2_without_lastact_TX":	"basic_with_action",
	"basic_action4_without_lastact_TX":	"basic_with_action",
	"basic_action8_without_lastact_TX":	"basic_with_action",
	"basic_action1_with_lastact_TX":	"basic_with_action",
	"basic_action2_with_lastact_TX":	"basic_with_action",
	"basic_action4_with_lastact_TX":	"basic_with_action",
	"basic_action8_with_lastact_TX":	"basic_with_action",
	"basic_action_TX_maxSBP":			"basic_with_action",
	"basic_action1_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action2_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action4_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_action8_with_lastact_TX_maxSBP":	"basic_with_action",
	"basic_noaction1_with_lastact_TX":	"basic_with_action",
	"basic_noaction2_with_lastact_TX":	"basic_with_action",
	"basic_noaction4_with_lastact_TX":	"basic_with_action",
	"basic_noaction8_with_lastact_TX":	"basic_with_action",
	"basic_noaction1_with_lastact_TX_maxSBP":	"basic",
	"basic_noaction2_with_lastact_TX_maxSBP":	"basic",
	"basic_noaction4_with_lastact_TX_maxSBP":	"basic",
	"basic_noaction8_with_lastact_TX_maxSBP":	"basic",
	"flag_action1_with_lastact_TX":	"flagCarry_with_action",
	"flag_action2_with_lastact_TX":	"flagCarry_with_action",
	"flag_action4_with_lastact_TX":	"flagCarry_with_action",
	"flag_action8_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction1_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction2_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction4_with_lastact_TX":	"flagCarry_with_action",
	"flag_noaction8_with_lastact_TX":	"flagCarry_with_action",
	"common_event_common_TX":			"commonCarry_with_action",
	"refill_TX":			"refill_with_action",
	"refill_noaction_TX":	"refill_with_action",
	"SB_automatic_refill_TX": "basic_with_action",
	"common_event_common_TX_maxSBP":		"commonCarry_with_action",
	
}

def get_transition_eventLabel(transition: str):
	if transition == "common_action_TX":
		return 72
	if transition == "common_action_TX_maxSBP":
		return 72
	if transition == "common_noaction_TX":
		return 60
	if transition == "common_noaction_TX_maxSBP":
		return 44
	if transition == "epsilon_action_TX":
		return 72
	if transition == "epsilon_noaction_TX":
		return 60
	if transition == "basic_action_TX":
		return 10276
	if transition == "basic_action1_without_lastact_TX":
		return 7204
	if transition == "basic_action2_without_lastact_TX":
		return 8228
	if transition == "basic_action4_without_lastact_TX":
		return 10276
	if transition == "basic_action8_without_lastact_TX":
		return 14372
	if transition == "basic_action1_with_lastact_TX":
		return 7204
	if transition == "basic_action2_with_lastact_TX":
		return 8228
	if transition == "basic_action4_with_lastact_TX":
		return 10276
	if transition == "basic_action8_with_lastact_TX":
		return 14372
	if transition == "basic_action_TX_maxSBP":
		return 8232
	if transition == "basic_action1_with_lastact_TX_maxSBP":
		return 5160
	if transition == "basic_action2_with_lastact_TX_maxSBP":
		return 6184
	if transition == "basic_action4_with_lastact_TX_maxSBP":
		return 8232
	if transition == "basic_action8_with_lastact_TX_maxSBP":
		return 12328
	if transition == "basic_noaction1_with_lastact_TX":
		return 7204
	if transition == "basic_noaction2_with_lastact_TX":
		return 8228
	if transition == "basic_noaction4_with_lastact_TX":
		return 10276
	if transition == "basic_noaction8_with_lastact_TX":
		return 14372
	if transition == "basic_noaction1_with_lastact_TX_maxSBP":
		return 7204
	if transition == "basic_noaction2_with_lastact_TX_maxSBP":
		return 8228
	if transition == "basic_noaction4_with_lastact_TX_maxSBP":
		return 10276
	if transition == "basic_noaction8_with_lastact_TX_maxSBP":
		return 14372
	if transition == "flag_action1_with_lastact_TX":
		return 5156
	if transition == "flag_action2_with_lastact_TX":
		return 8220
	if transition == "flag_action4_with_lastact_TX":
		return 14348
	if transition == "flag_action8_with_lastact_TX":
		return 26604
	if transition == "flag_noaction1_with_lastact_TX":
		return 5156
	if transition == "flag_noaction2_with_lastact_TX":
		return 8220
	if transition == "flag_noaction4_with_lastact_TX":
		return 14348
	if transition == "flag_noaction8_with_lastact_TX":
		return 26604
	if transition == "common_event_common_TX":
		return 72
	if transition == "refill_TX":
		return 8228
	if transition == "refill_noaction_TX":
		return 7204
	if transition == "SB_automatic_refill_TX":
		return 3156
	if transition == "common_event_common_TX_maxSBP":
		return 72
	return 0

def get_transition_eventLabel2(transition: str):
	if transition == "common_event_common_TX":
		return 400
	if transition == "common_event_common_TX_maxSBP":
		return 400
	return 0



str_tab = "    "
max_int_64 = int('7fffffffffffffff', 16)
min_int_64 = -max_int_64 - 1
max_int_32 = int('7fffffff', 16) 
min_int_32 = -max_int_32 - 1
max_int_16 = int('7fff', 16) 
min_int_16 = -max_int_16 - 1
max_int_12 = int('7ff', 16)
min_int_12 = -max_int_12 - 1
max_int_4 = int('7', 16)
min_int_4 = -max_int_4 - 1

max_uint_32 = int('ffffffff', 16)
max_uint_16 = int('ffff', 16) 
max_uint_12 = int('fff', 16) 
max_uint_4 = int('f', 16)

max_1_byte = int('ff', 16)
max_2_bytes = int('ffff', 16)

def num_split_p0(num):
	return ((num & int('ffffffffffffffff', 16)) >> 48) & 0x000000000000FFFF
def num_split_p1(num):
	return ((num & int('ffffffffffffffff', 16)) >> 36) & 0x0000000000000FFF
def num_split_p2(num):
	return ((num & int('ffffffffffffffff', 16)) >> 24) & 0x0000000000000FFF
def num_split_p3(num):
	return ((num & int('ffffffffffffffff', 16)) >> 12) & 0x0000000000000FFF
def num_split_p4(num):
	return num & 0x0000000000000FFF

local_memory_boundary = 4*1024*1024/64

parser = argparse.ArgumentParser(description="input generated instruction and the number")
parser.add_argument("inst_type", type=str, help="the instruction to generated")
parser.add_argument("inst_num", type=int, help="the number of the instructions to generated")
args = parser.parse_args()

inst_type = args.inst_type
inst_num = args.inst_num

# Change path to your testing programs
test_path = Path(f'../tests/trans_unit_tests/{inst_type}_test.cpp') # The c++ google test script
prog_path = Path('./efas/') # The directory to hold the efa programs
# top_exe_path = Path('fastsim_exe_jiya') # The top program to generate expected results
bin_path = Path("efa2bin.py")


def generate_efa_unit_test(test_path: PosixPath, prog_path: PosixPath, instruction: str, args: list):
	prog_lines = ["from EFA_v2 import *"]
	prog_lines.append(f"def {prog_path.stem}():")
	prog_lines.append(str_tab + "efa = EFA([])")
	prog_lines.append(str_tab + "efa.code_level = \"machine\"")
	prog_lines.append(str_tab + "state = State()")
	prog_lines.append(str_tab + "efa.add_initId(state.state_id)")
	prog_lines.append(str_tab + "efa.add_state(state)")
	prog_lines.append(str_tab + "state1 = State()")
	prog_lines.append(str_tab + "state1.alphabet = [0-255]")
	prog_lines.append(str_tab + "efa.add_state(state1)")
	if instruction != "SB_automatic_refill_TX":
		prog_lines.append(str_tab + "state2 = State()")
		prog_lines.append(str_tab + "state2.alphabet = [0-255]")
		prog_lines.append(str_tab + "efa.add_state(state2)")
	prog_lines.append(str_tab + f"tran0 = state.writeTransition(\"{transition_map1[instruction]}\", state, state1, 1)")
			
	# args = [val[8], rdMode, issueWidth, advanceWidth, ...]
	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 0\")")
	prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X17 X17\")")								# X17 = X7
	if instruction == "SB_automatic_refill_TX":
		for i in range(9):
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0][i])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0][i])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0][i])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0][i])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0][i])}\")")	# X16 = val[i]
			prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X16 0(X17) 1 8\")")	
	else:
		for i in range(8):
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0][i])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0][i])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0][i])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0][i])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0][i])}\")")	# X16 = val[i]
			prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X16 0(X17) 1 8\")")	

	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X18 1\")")									# X18 used to update threadMode
	prog_lines.append(str_tab + f"tran0.writeAction(\"sli X18 X18 23\")")								# X18 used to update threadMode
	prog_lines.append(str_tab + f"tran0.writeAction(\"or X18 X2 X2\")")									# X2 = X2 | X18 (1<<23) (current event word)

	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0][0])}\")")			
	prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0][0])}\")")	
	prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0][0])}\")")	
	prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0][0])}\")")	
	prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0][0])}\")")	# X16 = val[i]
	prog_lines.append(str_tab + f"tran0.writeAction(\"sri X16 X16 41\")")		# X16 clear SBCR left hand side
	prog_lines.append(str_tab + f"tran0.writeAction(\"sli X16 X16 41\")")		# X16 shift cleared SBCR back
	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {args[1]}\")")	# X17 = rmMode
	prog_lines.append(str_tab + f"tran0.writeAction(\"sli X17 X17 40\")")		# X17 = rmMode << 40
	prog_lines.append(str_tab + f"tran0.writeAction(\"or X17 X16 X16\")")		# Update rmMode
	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {args[2]}\")")	# X17 = SBCR.issueWidth
	prog_lines.append(str_tab + f"tran0.writeAction(\"sli X17 X17 36\")")		# X17 = issueWidth << 36
	prog_lines.append(str_tab + f"tran0.writeAction(\"or X17 X16 X16\")")		# Update SBCR.issueWidth
	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {args[3]}\")")	# X17 = SBCR.advanceWidth
	prog_lines.append(str_tab + f"tran0.writeAction(\"sli X17 X17 32\")")		# X17 = advanceWidth << 32
	prog_lines.append(str_tab + f"tran0.writeAction(\"or X17 X16 X16\")")		# Update SBCR.advanceWidth
	if args[1] == 1:	# SBMode (StreamBuffer Mode)
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X31 0\")")
		prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X31 X31\")")	# X31 = X7
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X20 0\")")
		prog_lines.append(str_tab + f"tran0.writeAction(\"sli X31 X21 3\")")	# SBP = X7 * 8
		prog_lines.append(str_tab + f"tran0.writeAction(\"add X21 X20 X5\")")	# X5 (SBP) = X7 * 8
		prog_lines.append(str_tab + f"tran0.writeAction(\"movlsb X31\")")		# copy to streambuffer
		if instruction == "SB_automatic_refill_TX":
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X20 X17 {72*args[3]}\")")
		elif instruction[-2:] == "TX":
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X20 X17 {3*args[3]}\")")
		else:
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X20 X17 {args[3]}\")")

	else: # LMMode (LocalMemory Mode)
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X20 0\")")
		prog_lines.append(str_tab + f"tran0.writeAction(\"add X20 X7 X5\")")		# X5 (SBP) = X7
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X30 0\")")
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X30 0\")")
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X30 0\")")
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X30 0\")")
		if instruction[-2:] == "TX":
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X20 X17 {3*args[3]}\")")
		else:
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X20 X17 {args[3]}\")")
	prog_lines.append(str_tab + f"tran0.writeAction(\"or X17 X16 X4\")")		# Update maxSBP to SBP
	prog_lines.append(str_tab + f"tran0.writeAction(\"addi X4 X18 0\")")
	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X30 0\")")
	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X31 0\")")
	
	if instruction[0:4] == "flag":
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {args[4]}\")")

	prog_lines.append(str_tab + f"tran0.writeAction(\"lastact\")")

	if instruction == "refill_TX" or instruction == "refill_noaction_TX":
		prog_lines.append(str_tab + f"tran1 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, {args[4]}, {args[6]})")
	elif instruction == "SB_automatic_refill_TX":
		prog_lines.append(str_tab + f"tran1 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state1, {args[4]})")
	else:
		prog_lines.append(str_tab + f"tran1 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, {args[4]})")


	test_lines = [f"TEST_F({inst_type}, Basic_{prog_path.stem}){{",
			str_tab + f"acc0.initSetup(0, \"testprogs/binaries/{prog_path.stem}.bin\", 0);",
			str_tab + f"int numop = 8;",
			str_tab + f"eventword_t ev0(0);",
			str_tab + f"ev0.setEventLabel({get_transition_eventLabel(instruction)});",
			str_tab + f"ev0.setNumOperands(numop);",
			str_tab + f"operands_t op0(numop);",
			str_tab + f"word_t *data = new word_t[numop];",
			str_tab + f"data[0] = reinterpret_cast<word_t>((uint64_t)8);",
			str_tab + f"data[1] = reinterpret_cast<word_t>((uint64_t)9);",
			str_tab + f"data[2] = reinterpret_cast<word_t>((uint64_t)10);",
			str_tab + f"data[3] = reinterpret_cast<word_t>((uint64_t)11);",
			str_tab + f"data[4] = reinterpret_cast<word_t>((uint64_t)12);",
			str_tab + f"data[5] = reinterpret_cast<word_t>((uint64_t)13);",
			str_tab + f"data[6] = reinterpret_cast<word_t>((uint64_t)14);",
			str_tab + f"data[7] = reinterpret_cast<word_t>((uint64_t)15);",
			str_tab + f"",
			str_tab + f"op0.setData(data);",
			str_tab + f"eventoperands_t eops(&ev0, &op0);"]

	if instruction == "common_event_common_TX" or instruction == "common_event_common_TX_maxSBP":
		test_lines.append(str_tab + f"eventword_t ev1(0);")
		test_lines.append(str_tab + f"ev1.setEventLabel({get_transition_eventLabel2(instruction)});")
		test_lines.append(str_tab + f"ev1.setNumOperands(numop);")
		test_lines.append(str_tab + f"eventoperands_t eops1(&ev1, &op0);")

	test_lines.append(str_tab + f"for(auto i = 0; i < numLanes; i++){{")
	test_lines.append(str_tab + str_tab + f"acc0.pushEventOperands(eops, i);")
	if instruction == "common_event_common_TX" or instruction == "common_event_common_TX_maxSBP":
		test_lines.append(str_tab + str_tab + f"acc0.pushEventOperands(eops1, i);")
	test_lines.append(str_tab + f"}}")
	test_lines.append(str_tab + f"while(!acc0.isIdle()){{")
	test_lines.append(str_tab + str_tab + f"acc0.simulate(2); // 2 is num stick")
	test_lines.append(str_tab + f"}}")

	test_lines.append(str_tab + f"// Checks specific for tests being written")
	test_lines.append(str_tab + f"for(auto i = 0; i < numLanes; i++){{")
		
	generate_assertion(instruction, test_lines, args)
	generate_efa1(instruction, prog_lines, args)
	if instruction[0:13] == "flag_noaction":
		prog_lines.append(str_tab + f"tran2 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state2, {args[4]})")
	elif instruction == "refill_TX" or instruction == "refill_noaction_TX":
		prog_lines.append(str_tab + f"tran2 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state2, {args[5]}, {args[7]})")
	elif instruction == "SB_automatic_refill_TX":
		prog_lines.append(str_tab + f"tran2 = state1.writeTransition(\"{transition_map3[instruction]}\", state1, state1, {args[5]})")
	else:
		prog_lines.append(str_tab + f"tran2 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state2, {args[5]})")
	generate_efa2(instruction, prog_lines, args)

	
	prog_lines.append(str_tab + f"efa.appendBlockAction(\"end_of_input_terminate_efa1\",\"movir X29 10\")")
	if instruction == "common_event_common_TX_maxSBP":
		prog_lines.append(str_tab + f"efa.appendBlockAction(\"end_of_input_terminate_efa1\",\"yield\")")
	else:
		prog_lines.append(str_tab + f"efa.appendBlockAction(\"end_of_input_terminate_efa1\",\"yieldt\")")
	if instruction == "SB_automatic_refill_TX":
		prog_lines.append(str_tab + f"efa.linkBlocktoState(\"end_of_input_terminate_efa1\", state1)")
		prog_lines.append(str_tab + f"efa.appendBlockAction(\"sb_refill\",\"sri X5 X28 3\")")
		prog_lines.append(str_tab + f"efa.appendBlockAction(\"sb_refill\",\"movlsb X28\")")
		prog_lines.append(str_tab + f"efa.appendBlockAction(\"sb_refill\",\"lastact\")")
		prog_lines.append(str_tab + f"efa.linkBlocktoState(\"sb_refill\", state1)")
	else:
		prog_lines.append(str_tab + f"efa.linkBlocktoState(\"end_of_input_terminate_efa1\", state2)")

	prog_lines.append(str_tab + "return efa")

	with open(prog_path, 'w') as writer:
		writer.writelines('\n'.join(prog_lines) + '\n')

	return test_lines

def generate_bin(efa_fname):
	os.chdir("../assembler/")
	os.system("python3 " + str(bin_path) + " --efa ../testprogs/efas/" + efa_fname + " --outpath ../testprogs/binaries/ --debug-messages --toplinker")
	os.chdir("../testprogs/")
	# subprocess.Popen([f"python3", bin_path, "--efa", "efas/"+efa_fname, "--outpath", "binaries/"])
	return


def generate_random_efa(instruction: str, test_path: PosixPath, prog_path: PosixPath, count: int):
	args_list, output_list = [], []
	for i in range(count):
		args = generate_random_args(instruction)
		args_list.append(args)
		test_lines = generate_efa_unit_test(test_path, prog_path.joinpath(f'{instruction}_{i}.py'), instruction, args)
		generate_bin(f'{instruction}_{i}.py')
		print(f'{instruction}_{i}.py')
		with open(test_path, 'a') as test_writer:
			test_writer.writelines('\n'.join(test_lines) + '\n')

	return args_list



##################################################
# To add unit tests with random input, implement following three functions
# Add the instruction in the match cases
# Naming as
# generage_efa
# generate_random_args
# generate_assertion
##################################################

# Add the efa program in the corresponding case
def generate_efa1(instruction: str, prog_lines: list, args: list):
	if instruction == "common_action_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 1\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")
	elif instruction == "common_noaction_TX":
		print("common_noaction_TX_maxSBP has no action.")

	elif instruction == "common_action_TX_maxSBP":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 1\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")
	elif instruction == "common_noaction_TX_maxSBP":
		print("common_noaction_TX_maxSBP has no action.")

	elif instruction == "epsilon_action_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 3\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")
	elif instruction  == "epsilon_noaction_TX":
		print("epsilon_noaction_TX has no action.")

	elif instruction == "basic_action_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 5\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 5\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 6\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 6\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")
	
	elif instruction == "basic_action2_without_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 5\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 6\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_action1_without_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
	
	elif instruction == "basic_action4_without_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")

	elif instruction == "basic_action8_without_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X27 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X26 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X25 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X24 7\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X27 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X26 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X25 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X24 8\")")


	elif instruction == "basic_action2_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_action1_with_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")
		
	
	elif instruction == "basic_action4_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_action8_with_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X27 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X26 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X25 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X24 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X27 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X26 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X25 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X24 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_action_TX_maxSBP":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 5\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 5\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 6\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 6\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_action2_with_lastact_TX_maxSBP":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_action1_with_lastact_TX_maxSBP":
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")
		
	
	elif instruction == "basic_action4_with_lastact_TX_maxSBP":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_action8_with_lastact_TX_maxSBP":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X27 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X26 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X25 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X24 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X27 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X26 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X25 8\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X24 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_noaction2_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_noaction1_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")
		
	
	elif instruction == "basic_noaction4_with_lastact_TX":
		# # prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# # prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		# # prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_noaction8_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X27 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X26 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X25 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X24 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X27 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X26 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X25 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X24 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_noaction2_with_lastact_TX_maxSBP":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_noaction1_with_lastact_TX_maxSBP":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")
		
	
	elif instruction == "basic_noaction4_with_lastact_TX_maxSBP":
		# # prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# # prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		# # prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "basic_noaction8_with_lastact_TX_maxSBP":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X16 0\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X27 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X26 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X25 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X24 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X16 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X29 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X28 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X27 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X26 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X25 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X24 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "flag_action1_with_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {args[5]}\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X16 255\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")
		
	elif instruction == "flag_action2_with_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {args[5]}\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X16 255\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "flag_action4_with_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {args[5]}\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X16 255\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "flag_action8_with_lastact_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {args[5]}\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X27 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X26 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X25 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X24 7\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X16 255\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "flag_noaction1_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {args[5]}\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X16 255\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")
		
	elif instruction == "flag_noaction2_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {args[5]}\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X16 255\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "flag_noaction4_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {args[5]}\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X16 255\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 9\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 10\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "flag_noaction8_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {args[5]}\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X29 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X28 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X27 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X26 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X25 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X24 7\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map1[instruction]}\", state1, state2, 255)")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X16 255\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 8\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 9\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 10\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 11\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 12\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 13\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 14\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "common_event_common_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X30 X30 1\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"yield\")")

	elif instruction == "refill_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 1\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map2[instruction]}\", state1, state2, 255, {args[6]})")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 2\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "refill_noaction_TX":
		# prog_lines.append(str_tab + f"tran1.writeAction(\"movir X30 1\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

		prog_lines.append(str_tab + f"tran3 = state1.writeTransition(\"{transition_map3[instruction]}\", state1, state2, 255, {args[6]})")
		prog_lines.append(str_tab + f"tran3.writeAction(\"movir X30 2\")")
		# prog_lines.append(str_tab + f"tran3.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran3.writeAction(\"lastact\")")

	elif instruction == "SB_automatic_refill_TX":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X30 X30 1\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

	elif instruction == "common_event_common_TX_maxSBP":
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X30 X30 1\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X5 X20 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"lastact\")")

	else:
		print("Instruction not implemented yet, exit. 0")
		sys.exit()

	return

# Add the efa program in the corresponding case
def generate_efa2(instruction: str, prog_lines: list, args: list):
	if instruction == "common_action_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 2\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
	elif instruction == "common_noaction_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 2\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
	
	elif instruction == "common_action_TX_maxSBP":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 2\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
	elif instruction == "common_noaction_TX_maxSBP":
		print("common_noaction_TX_maxSBP has no action.")

	elif instruction == "epsilon_action_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 4\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
	elif instruction  == "epsilon_noaction_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 4\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")

	elif instruction == "basic_action_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 5\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 6\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "basic_action2_without_lastact_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 5\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 6\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "basic_action1_without_lastact_TX" or instruction == "basic_action4_without_lastact_TX" or instruction == "basic_action8_without_lastact_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "basic_action1_with_lastact_TX" or instruction == "basic_action2_with_lastact_TX" or instruction == "basic_action4_with_lastact_TX" or instruction == "basic_action8_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "basic_action_TX_maxSBP":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 5\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 6\")")
		
	elif instruction == "basic_action1_with_lastact_TX_maxSBP" or instruction == "basic_action2_with_lastact_TX_maxSBP" or instruction == "basic_action4_with_lastact_TX_maxSBP" or instruction == "basic_action8_with_lastact_TX_maxSBP":
		# prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X30 7\")")
		# prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X30 8\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "basic_noaction1_with_lastact_TX" or instruction == "basic_noaction2_with_lastact_TX" or instruction == "basic_noaction4_with_lastact_TX" or instruction == "basic_noaction8_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "basic_noaction1_with_lastact_TX_maxSBP" or instruction == "basic_noaction2_with_lastact_TX_maxSBP" or instruction == "basic_noaction4_with_lastact_TX_maxSBP" or instruction == "basic_noaction8_with_lastact_TX_maxSBP":
		# prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		# prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map1[instruction]}\", state2, state1, 255)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "flag_action1_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "flag_action2_with_lastact_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "flag_action4_with_lastact_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 9\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "flag_action8_with_lastact_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 9\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 10\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 11\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 12\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 13\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "flag_noaction1_with_lastact_TX":
		# prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "flag_noaction2_with_lastact_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "flag_noaction4_with_lastact_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 9\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "flag_noaction8_with_lastact_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X17 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 7\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 9\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 10\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 11\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 12\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 13\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")
		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255)")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X17 0\")")
		# prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 8\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")


	elif instruction == "common_event_common_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X31 X31 1\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X19 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")

		prog_lines.append(str_tab + f"tran4 = state.writeTransition(\"event\", state, state2, 0)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X30 X30 1\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X18 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"lastact\")")

	elif instruction == "refill_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 1\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X18 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")

		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255, {args[7]})")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 2\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X18 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")
		
	elif instruction == "refill_noaction_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"movir X31 1\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X18 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")

		prog_lines.append(str_tab + f"tran4 = state2.writeTransition(\"{transition_map3[instruction]}\", state2, state1, 255, {args[7]})")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X31 2\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X18 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"yieldt\")")

	elif instruction == "SB_automatic_refill_TX":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X31 X31 1\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")		

	elif instruction == "common_event_common_TX_maxSBP":
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X31 X31 1\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"addi X5 X19 0\")")
		prog_lines.append(str_tab + f"tran2.writeAction(\"yieldt\")")

		prog_lines.append(str_tab + f"tran4 = state.writeTransition(\"event\", state, state2, 0)")
		prog_lines.append(str_tab + f"tran4.writeAction(\"movir X16 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"add X4 X16 X17\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"sri X17 X17 32\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"sli X17 X17 32\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X17 X17 {3*args[3]}\")") # change maxSBP
		prog_lines.append(str_tab + f"tran4.writeAction(\"add X17 X16 X4\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X30 X30 1\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"addi X5 X18 0\")")
		prog_lines.append(str_tab + f"tran4.writeAction(\"lastact\")")

	else:
		print("Instruction not implemented yet, exit. 1")
		sys.exit()

	return

# Add code to generate corresponding random arguments
def generate_random_args(instruction: str) -> list:
	args = []
	# args = [val, rdMode, issueWidth, advanceWidth,]
	if instruction == "common_action_TX" or instruction == "common_noaction_TX_maxSBP" or instruction == "common_noaction_TX" or instruction == "common_action_TX_maxSBP" or instruction == "epsilon_action_TX" or instruction == "epsilon_noaction_TX" or instruction == "common_event_common_TX" or instruction == "common_event_common_TX_maxSBP":
		val = []
		for i in range(8):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = random.randint(0,1)
		issueWidth = 1
		if(rdMode == 1): # SBMode
			issueWidth = random.randint(1,8)
		else:
			issueWidth = 1 << random.randint(0,3)

		advanceWidth = random.randint(issueWidth,8)
		args = [val, rdMode, issueWidth, advanceWidth, 0, 0]
	
	elif instruction == "refill_TX" or instruction == "refill_noaction_TX":
		val = []
		for i in range(8):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = random.randint(0,1)

		issueWidth = 1
		max_limit = 254
		if(rdMode == 1): # SBMode
			issueWidth = random.randint(1,8)
			max_limit = (1 << issueWidth) - 1
		else:
			issueWidth = 1 << random.randint(0,3)
		advanceWidth = random.randint(issueWidth,8)

		val1 = random.randint(0,max_limit)
		val2 = random.randint(0,max_limit)

		refill_width1 = 7
		refill_width2 = 7
		if((advanceWidth - issueWidth)< refill_width1):
			refill_width1 = advanceWidth - issueWidth
		if advanceWidth < refill_width2:
			refill_width2 = advanceWidth

		refill_width1 = random.randint(0,refill_width1) 
		refill_width2 = random.randint(0,refill_width2)

		addr = 0
		width = issueWidth
		next_addr = advanceWidth - refill_width1
		if (rdMode == 0):
			width = width << 3
			next_addr = next_addr << 3
		
		tmp_addr = addr
		tmp = 1
		for i in range(0,width):
			idx = int(tmp_addr / 64)
			low_offset = tmp_addr - (idx * 64)
			bit_val1 = (val1 >> i) & 0b1
			bit_val = (val[idx] >> low_offset) & 0b1
			if bit_val1 != bit_val:
				if bit_val == 0:
					val[idx] += (tmp << low_offset)
				else:
					val[idx] -= (tmp << low_offset)
			tmp_addr += 1

		tmp_addr = next_addr
		tmp = 1
		for i in range(0,width):
			idx = int(tmp_addr / 64)
			low_offset = tmp_addr - (idx * 64)
			bit_val1 = (val2 >> i) & 0b1
			bit_val = (val[idx] >> low_offset) & 0b1
			if bit_val1 != bit_val:
				if bit_val == 0:
					val[idx] += (tmp << low_offset)
				else:
					val[idx] -= (tmp << low_offset)
			tmp_addr += 1

		args = [val, rdMode, issueWidth, advanceWidth, val1, val2, refill_width1, refill_width2]
		

	elif instruction == "basic_action_TX" or instruction == "basic_action_TX_maxSBP" or instruction == "basic_action2_without_lastact_TX" or instruction == "basic_action1_without_lastact_TX" or instruction == "basic_action4_without_lastact_TX" or instruction == "basic_action8_without_lastact_TX" or instruction == "basic_action2_with_lastact_TX" or instruction == "basic_action1_with_lastact_TX" or instruction == "basic_action4_with_lastact_TX" or instruction == "basic_action8_with_lastact_TX" or instruction == "basic_action2_with_lastact_TX_maxSBP" or instruction == "basic_action1_with_lastact_TX_maxSBP" or instruction == "basic_action4_with_lastact_TX_maxSBP" or instruction == "basic_action8_with_lastact_TX_maxSBP" or instruction == "basic_noaction1_with_lastact_TX" or instruction == "basic_noaction2_with_lastact_TX" or instruction == "basic_noaction4_with_lastact_TX" or instruction == "basic_noaction8_with_lastact_TX" or instruction == "basic_noaction1_with_lastact_TX_maxSBP" or instruction == "basic_noaction2_with_lastact_TX_maxSBP" or instruction == "basic_noaction4_with_lastact_TX_maxSBP" or instruction == "basic_noaction8_with_lastact_TX_maxSBP":
		val = []
		for i in range(8):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = random.randint(0,1)
		issueWidth = 1
		max_limit = 254
		if(rdMode == 1): # SBMode
			issueWidth = random.randint(1,8)
			max_limit = (1 << issueWidth) - 1
		else:
			issueWidth = 1 << random.randint(0,3)
		advanceWidth = random.randint(issueWidth,8)

		val1 = random.randint(0,max_limit)
		val2 = random.randint(0,max_limit)

		addr = 0
		width = issueWidth
		next_addr = advanceWidth
		if (rdMode == 0):
			width = width << 3
			next_addr = next_addr << 3
		
		tmp_addr = addr
		tmp = 1
		for i in range(0,width):
			idx = int(tmp_addr / 64)
			low_offset = tmp_addr - (idx * 64)
			bit_val1 = (val1 >> i) & 0b1
			bit_val = (val[idx] >> low_offset) & 0b1
			if bit_val1 != bit_val:
				if bit_val == 0:
					val[idx] += (tmp << low_offset)
				else:
					val[idx] -= (tmp << low_offset)
			tmp_addr += 1

		tmp_addr = next_addr
		tmp = 1
		for i in range(0,width):
			idx = int(tmp_addr / 64)
			low_offset = tmp_addr - (idx * 64)
			bit_val1 = (val2 >> i) & 0b1
			bit_val = (val[idx] >> low_offset) & 0b1
			if bit_val1 != bit_val:
				if bit_val == 0:
					val[idx] += (tmp << low_offset)
				else:
					val[idx] -= (tmp << low_offset)
			tmp_addr += 1

		args = [val, rdMode, issueWidth, advanceWidth, val1, val2]

	elif instruction == "SB_automatic_refill_TX":
		val = []
		for i in range(8):
			val.append(0)
		val.append(255)
		rdMode = 1
		issueWidth = 8
		advanceWidth = 8
		args = [val, rdMode, issueWidth, advanceWidth, 0, 255]




	elif instruction == "flag_action1_with_lastact_TX" or instruction == "flag_action2_with_lastact_TX" or instruction == "flag_action4_with_lastact_TX" or instruction == "flag_action8_with_lastact_TX" or instruction == "flag_noaction1_with_lastact_TX" or instruction == "flag_noaction2_with_lastact_TX" or instruction == "flag_noaction4_with_lastact_TX" or instruction == "flag_noaction8_with_lastact_TX":
		val = []
		for i in range(8):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = random.randint(0,1)
		issueWidth = 1
		max_limit = 254
		if(rdMode == 1): # SBMode
			issueWidth = random.randint(1,8)
		else:
			issueWidth = 1 << random.randint(0,3)
		advanceWidth = random.randint(issueWidth,8)

		val1 = random.randint(0,max_limit)
		val2 = random.randint(0,max_limit)
		args = [val, rdMode, issueWidth, advanceWidth, val1, val2]
	
	else:
		print("Instruction not implemented yet, exit. 2")
		sys.exit()

	return args

# Add google test code to assert the results
def generate_assertion(instruction: str, test_lines: list, args: list):
	# args = [val, rdMode, issueWidth, advanceWidth,]
	if instruction == "common_action_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 1));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 2));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	# args = [val, rdMode, issueWidth, advanceWidth,]
	elif instruction == "common_noaction_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 2));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, (i << 19) + {advanceWidth}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5, (i << 19) + {advanceWidth}));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5, ((i << 16) + {advanceWidth})));")

	elif instruction == "common_action_TX_maxSBP":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 1));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 10));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")


	elif instruction == "common_noaction_TX_maxSBP":
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5, (i << 19) + {advanceWidth}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 10));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4,  {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 10));")

	elif instruction == "epsilon_action_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 3));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 4));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")

	elif instruction == "epsilon_noaction_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 4));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")

	elif instruction == "basic_action_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 5));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 5));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 5));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")



	elif instruction == "basic_action2_without_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 5));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 5));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "basic_action1_without_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "basic_action4_without_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X28, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "basic_action8_without_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X24, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X25, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X26, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X27, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X28, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "basic_action1_with_lastact_TX" or instruction == "basic_action2_with_lastact_TX" or instruction == "basic_action4_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "basic_action8_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X24, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X25, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X26, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X27, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X28, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")


	elif instruction == "basic_action_TX_maxSBP":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 5));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 10));")
		# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 5));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")


	elif instruction == "basic_action1_with_lastact_TX_maxSBP" or instruction == "basic_action2_with_lastact_TX_maxSBP" or instruction == "basic_action4_with_lastact_TX_maxSBP":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 10));")
		# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "basic_action8_with_lastact_TX_maxSBP":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X24, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X25, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X26, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X27, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X28, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 10));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 19)));")
			# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, (i << 16)));")
			# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "basic_noaction1_with_lastact_TX" or instruction == "basic_noaction2_with_lastact_TX" or instruction == "basic_noaction4_with_lastact_TX" or instruction == "basic_noaction8_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 0));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "basic_noaction1_with_lastact_TX_maxSBP" or instruction == "basic_noaction2_with_lastact_TX_maxSBP" or instruction == "basic_noaction4_with_lastact_TX_maxSBP" or instruction == "basic_noaction8_with_lastact_TX_maxSBP":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 0));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 0));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 10));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "flag_noaction1_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[4]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")

	elif instruction == "flag_noaction2_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[4]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 0));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 16))));")

	elif instruction == "flag_noaction8_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[4]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 13));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 0));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 16))));")

	elif instruction == "flag_noaction4_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[4]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 9));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 0));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 16))));")

	elif instruction == "flag_action1_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[5]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")

	elif instruction == "flag_action2_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[5]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 16))));")

	elif instruction == "flag_action8_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[5]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 13));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X28, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X27, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X26, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X25, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X24, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 16))));")

	elif instruction == "flag_action4_with_lastact_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[5]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 9));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 7));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X28, 7));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 19))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17,  ((i << 16))));")

	elif instruction == "common_event_common_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 2));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 1));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, (i << 19) + {advanceWidth}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X19, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, (i << 16)) + {advanceWidth});")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X19, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "common_event_common_TX_maxSBP":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X29, 10));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 2));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 1));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X20, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, (i << 19) + {advanceWidth}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X19, ((i << 19) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X20, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, (i << 16)) + {advanceWidth});")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X19, ((i << 16) + {advanceWidth})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth})));")

	elif instruction == "refill_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 1));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 1));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		refillWidth = args[6]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, (i << 19) + {advanceWidth} - {refillWidth}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth} - {refillWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, (i << 16)) + {advanceWidth} - {refillWidth});")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth} - {refillWidth})));")

	elif instruction == "refill_noaction_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 0));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 1));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		refillWidth = args[6]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		if args[1] == 1: # SB Mode
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, (i << 19)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, (i << 19) + {advanceWidth} - {refillWidth}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {advanceWidth} - {refillWidth})));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 3*advanceWidth}u));")
			# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, (i << 16)));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, (i << 16)) + {advanceWidth} - {refillWidth});")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 16) + {advanceWidth} - {refillWidth})));")

	elif instruction == "SB_automatic_refill_TX":
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X30, 64));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X31, 1));")
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4, {SBCR1 + 72*advanceWidth}u));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X5,  ((i << 19) + {64*advanceWidth})));")
		

	else:
		print("Instruction not implemented yet, exit. 3")
		sys.exit()

	test_lines.append(str_tab + "}")
	test_lines.append("}")
	return


def generate_random_unit_test(test_path: PosixPath, prog_path: PosixPath, instruction: str, count: int):
	args_list = generate_random_efa(instruction, test_path, prog_path, count)

# # A wrpper function to handle the unit test
# def generate_random_addi_unit_test(test_path: PosixPath, prog_path: PosixPath, instruction: str, count: int=10):
# 	args_list, output_list = generate_random_efa(instruction, fpath, count)
# 	for args, out in zip(args_list, output_list):
# 		print(f'{args} -> {out}')



if __name__ == '__main__':

	# print("%s %d" %(inst_type,inst_num))
	# print(test_path)

	lines = ["#include <gtest/gtest.h>",
			"#include \"udlane.hh\"",
			"#include \"types.hh\"",
			"#include \"lanetypes.hh\"",
			"#include \"udaccelerator.hh\"",
			"",
			"using namespace basim;",
			"",
			f"class {inst_type} : public ::testing::Test {{",
			" protected:",
			str_tab + "size_t num_threads = 2;",
			str_tab + "int numLanes = 64;",
			str_tab + "UDAccelerator acc0 = UDAccelerator(numLanes, 0, 1); // UDAccelerator(numLanes, UDID/networkID, lmmode (0: accelerator based addressing, 1:bank/lane based addressing))",
			str_tab + "int buffsize1 = 1024;",
			str_tab + "int buffsize2 = 1024;",
			"};"]
	with open(test_path, 'w') as writer:
		writer.writelines('\n'.join(lines) + '\n')

	generate_random_unit_test(test_path, prog_path, inst_type, inst_num)
	print("End")
	
