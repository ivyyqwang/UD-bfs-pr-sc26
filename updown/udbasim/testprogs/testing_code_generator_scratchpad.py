import sys
import random
from pathlib import Path, PosixPath
import subprocess
import argparse
import os


str_tab = "    "
max_int_64 = int('7fffffffffffffff', 16)
min_int_64 = -max_int_64 - 1
max_int_32 = int('7fffffff', 16) 
min_int_32 = -max_int_32 - 1
max_int_21 = int('fffff', 16) 
min_int_21 = -max_int_21 - 1
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
test_path = Path(f'../tests/inst_unit_tests/{inst_type}_test.cpp') # The c++ google test script
prog_path = Path('./efas/') # The directory to hold the efa programs
# top_exe_path = Path('fastsim_exe_jiya') # The top program to generate expected results
bin_path = Path("efa2bin.py")


def generate_efa_unit_test(test_path: PosixPath, prog_path: PosixPath, instruction: str, args: list):
	prog_lines = ["from EFA_v2 import *",
			f"def {prog_path.stem}():",
			str_tab + "efa = EFA([])",
			str_tab + "efa.code_level = \"machine\"",
			str_tab + "state = State()",
			str_tab + "efa.add_initId(state.state_id)",
			str_tab + "efa.add_state(state)",
			str_tab + "event_map = {",
			str_tab + str_tab + "\"launch_events\": 0,",
			str_tab + "}",
			str_tab + "tran0 = state.writeTransition(\"eventCarry\", state, state, event_map['launch_events'])"]

	test_lines = [f"TEST_F({inst_type}, Basic_{prog_path.stem}){{",
			str_tab + f"acc0.initSetup(0, \"testprogs/binaries/{prog_path.stem}.bin\", 0);",
			str_tab + f"int numop = 9;",
			str_tab + f"eventword_t ev0(0);",
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
			str_tab + f"eventoperands_t eops(&ev0, &op0);",
			str_tab + f"for(auto i = 0; i < numLanes; i++)",
			str_tab + str_tab + f"acc0.pushEventOperands(eops, i);",
			str_tab + f"while(!acc0.isIdle()){{",
			str_tab + str_tab + f"acc0.simulate(2); // 2 is num stick",
			str_tab + f"}}",

			str_tab + f"// Checks specific for tests being written",
			str_tab + f"for(auto i = 0; i < numLanes; i++){{"]

	generate_efa(instruction, prog_lines, args)
	prog_lines.append(str_tab + "return efa")

	with open(prog_path, 'w') as writer:
		writer.writelines('\n'.join(prog_lines) + '\n')

	return test_lines

def generate_bin(efa_fname):
	os.chdir("../assembler/")
	os.system("python3 " + str(bin_path) + " --efa ../testprogs/efas/" + efa_fname + " --outpath ../testprogs/binaries/" )
	os.chdir("../testprogs/")
	# subprocess.Popen([f"python3", bin_path, "--efa", "efas/"+efa_fname, "--outpath", "binaries/"])
	return

# def generate_output(efa_fname):
# 	# subprocess.Popen([f"python3", bin_path, "--efa", "efas/"+efa_fname, "--outpath", "binaries/"])
# 	p = subprocess.Popen([f"./{top_exe_path}", fname], stdout=subprocess.PIPE)
# 	out, _ = p.communicate()
# 	s = out.decode('ascii').split('\n')
# 	ind = -1
# 	for j in range(len(s)):
# 		if s[-1-j] == '[yield_terminate,]':
# 			ind = -2-j
# 			break
# 	output = s[ind].split(':')[-1].split(',')
# 	return output

def generate_random_efa(instruction: str, test_path: PosixPath, prog_path: PosixPath, count: int):
	args_list, output_list = [], []
	for i in range(count):
		args = generate_random_args(instruction)
		args_list.append(args)

		test_lines = generate_efa_unit_test(test_path, prog_path.joinpath(f'{instruction}_{i}.py'), instruction, args)
		generate_bin(f'{instruction}_{i}.py')
		generate_assertion(instruction, test_lines, args)
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
def generate_efa(instruction: str, prog_lines: list, args: list):
	match instruction:
		# put_2bytes_imm Xs, $bytes
		# LM[Xs].write2Byte($bytes); Xs+=2
		# args = [addr, $bytes]
		case "put_2byte_imm":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X16 X16\")")				# X16 = X7 + X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X17\")")			# X17 = X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_2byte_imm X16 {args[1]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X18\")")			# X18 = X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_2byte_imm X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_2byte_imm X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_2byte_imm X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")				# X16 = X16 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")				# X17 = X17 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X18 X7 X18\")")				# X18 = X18 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"yield_terminate\")")	
		
		# movil2 Xs, $bytes
		# LM[Xs].write2Byte($bytes); Xs+=2
		# args = [addr, $bytes]
		case "movil2":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X16 X16\")")				# X16 = X7 + X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X17 0\")")			# X17 = X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil2 X16 {args[1]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X18 0\")")			# X18 = X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil2 X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil2 X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil2 X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")				# X16 = X16 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")				# X17 = X17 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X18 X7 X18\")")				# X18 = X18 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"yieldt\")")		

		# put_1byte_imm Xs, $bytes
		# LM[Xs] = write1Byte($bytes); Xs+=1
		# args = [addr, $bytes]
		case "put_1byte_imm":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X16 X16\")")				# X16 = X7 + X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X17\")")			# X17 = X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_1byte_imm X16 {args[1]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X18\")")			# X18 = X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_1byte_imm X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_2byte_imm X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_2byte_imm X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"put_2byte_imm X18 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")				# X16 = X16 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")				# X17 = X17 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X18 X7 X18\")")				# X18 = X18 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"yield_terminate\")")	

		# movil1 Xs, $bytes
		# LM[Xs] = write1Byte($bytes); Xs+=1
		# args = [addr, $bytes]
		case "movil1":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X16 X16\")")				# X16 = X7 + X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X17 0\")")		# X17 = X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil1 X16 {args[1]}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X18 0\")")		# X18 = X16
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil1 X18 0\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil2 X18 0\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil2 X18 0\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"movil2 X18 0\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")		# X16 = X16 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")		# X17 = X17 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X18 X7 X18\")")		# X18 = X18 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"yieldt\")")

		# move Xs, $imm(Xd), $inc_flag, $bytes
		# LM[Xd+$imm : Xd+$imm +$bytes-1] ← Xs & mask. If $inc_flag==1, Xd += $bytes
		# args = [val, imm_val, addr, inc_flag, byte_num]
		case "move_reg2lm":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X17 {num_split_p0(args[2])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p4(args[2])}\")")	# X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X17 X18\")")					# X18 = X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X17 X17\")")						# X17 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"move X16 {args[1]}(X17) {args[3]} {args[4]}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")						# X17 = X17 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"yield_terminate\")")
		

		# movrl Xs, $imm(Xd), $inc_flag, $bytes
		# LM[Xd+$imm : Xd+$imm +$bytes-1] ← Xs & mask. If $inc_flag==1, Xd += $bytes
		# args = [val, imm_val, addr, inc_flag, byte_num]
		case "movrl":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {num_split_p0(args[2])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p4(args[2])}\")")	# X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X17 X18 0\")")								# X18 = X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X17 X17\")")								# X17 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X16 {args[1]}(X17) {args[3]} {args[4]}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")								# X17 = X17 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"yieldt\")")

		# move $imm(Xs), Xd, $inc_flag, $bytes
		# Xd ← LM[Xs+$imm : Xs+$imm +$bytes-1] & mask. If $inc_flag==1, Xs += $bytes
		# args = [val, imm_val, addr, inc_flag, byte_num]
		case "move_lm2reg":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X17 {num_split_p0(args[2])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p4(args[2])}\")")	# X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X17 X18\")")					# X18 = X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X17 X17\")")						# X17 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"move X16 {args[1]}(X17) 0 8\")")			# LM[X17+$imm : X17+$imm +$bytes-1] = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"move {args[1]}(X17) X19 {args[3]} {args[4]}\")")	# X19 = LM[X17+$imm : X17+$imm +$bytes-1] = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")						# X17 = X17 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"yield_terminate\")")
			
		# movlr $imm(Xs), Xd, $inc_flag, $bytes
		# Xd ← LM[Xs+$imm : Xs+$imm +$bytes-1] & mask. If $inc_flag==1, Xs += $bytes
		# args = [val, imm_val, addr, inc_flag, byte_num, val4, val3, val2, val1, val0, addr_high, addr_low]
		case "movlr":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {num_split_p0(args[2])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p4(args[2])}\")")	# X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X17 X18 0\")")					# X18 = X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X17 X17\")")					# X17 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X16 {args[1]}(X17) 0 8\")")		# LM[X17+$imm : X17+$imm +$bytes-1] = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"movlr {args[1]}(X17) X19 {args[3]} {args[4]}\")")	# X19 = LM[X17+$imm : X17+$imm +$bytes-1] = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")					# X17 = X17 - X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"yieldt\")")


		# move_word Xs, Xb(Xd, $inc_flag, $scale)
		# LM[Xb+(Xd<<($scale+3)):Xb+(Xd<<($scale+3))+7] ← Xs. If $inc_flag==1, Xd += 1
		# args = [val, Xb_val, Xd_val, inc_flag, scale, addr]
		case "move_word_reg2lm":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = Xb_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X18 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p4(args[2])}\")")	# X18 = Xd_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X18 X19\")")					# X19 = X18 = Xd_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X17 X7 X17\")")						# X17 = Xb_val + X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"move_word X16 X17(X18,{args[3]},{args[4]})\")")  			# move_word X16, X17(X18, $inc_flag, $scale)
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")						# X17 = Xb_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"yield_terminate\")")

		# movwrl Xs, Xb(Xd, $inc_flag, $scale)
		# LM[Xb+(Xd<<($scale+3)):Xb+(Xd<<($scale+3))+7] ← Xs. If $inc_flag==1, Xd += 1
		# args = [val, Xb_val, Xd_val, inc_flag, scale, addr]
		case "movwrl":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = Xb_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X18 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p4(args[2])}\")")	# X18 = Xd_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X18 X19 0\")")						# X19 = X18 = Xd_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X17 X7 X17\")")						# X17 = Xb_val + X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"movwrl X16 X17(X18,{args[3]},{args[4]})\")")  # movwrl X16, X17(X18, $inc_flag, $scale)
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")						# X17 = Xb_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"yieldt\")")

		# move_word Xb(Xs, $inc_flag, $scale), Xd
		# Xd←LM[Xb+(Xs<<($scale+3)):Xb+(Xs<<($scale+3))+7]. If $inc_flag==1, Xs += 1
		# args = [val, Xb_val, Xs_val, inc_flag, scale, addr]
		case "move_word_lm2reg":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = Xb_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X18 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p4(args[2])}\")")	# X18 = Xd_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X18 X19\")")					# X19 = X18 = Xs_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X17 X7 X17\")")						# X17 = Xb_val + X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"move_word X16 X17(X18,0,{args[4]})\")")  	# move_word X16, X17(X18, 0, $scale)
			prog_lines.append(str_tab + f"tran0.writeAction(\"move_word X17(X18,{args[3]},{args[4]}) X20\")")  	# move_word X17(X18, $inc_flag, $scale), X20 (X20 = val)
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")						# X17 = Xb_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"yield_terminate\")")

		# movwlr Xb(Xs, $inc_flag, $scale), Xd
		# Xd←LM[Xb+(Xs<<($scale+3)):Xb+(Xs<<($scale+3))+7]. If $inc_flag==1, Xs += 1
		# args = [val, Xb_val, Xs_val, inc_flag, scale, addr]
		case "movwlr":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = Xb_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X18 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p4(args[2])}\")")	# X18 = Xd_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X18 X19 0\")")					# X19 = X18 = Xs_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X17 X7 X17\")")						# X17 = Xb_val + X7
			prog_lines.append(str_tab + f"tran0.writeAction(\"movwrl X16 X17(X18,0,{args[4]})\")")  	# move_word X16, X17(X18, 0, $scale)
			prog_lines.append(str_tab + f"tran0.writeAction(\"movwlr X17(X18,{args[3]},{args[4]}) X20\")")  	# move_word X17(X18, $inc_flag, $scale), X20 (X20 = val)
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")						# X17 = Xb_val
			prog_lines.append(str_tab + f"tran0.writeAction(\"yieldt\")")

		# bcopy_ops Xop1, Xd, Xnumops
		# args = [reg_id, addr, numops]
		case "bcopy_ops":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[1])}\")")	# X16 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X17 {args[2]}\")")			# X17 = numops
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X16 X16\")")						# X16 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"bcopy_ops X{args[0]} X16 X17\")")			# bcopy_ops Xop1, Xd, Xnumops
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")						# X16 = addr
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")
		
		# bcpyol Xop1, Xd, Xnumops
		# args = [reg_id, addr, numops]
		case "bcpyol":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[1])}\")")	# X16 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {args[2]}\")")			# X17 = numops
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X16 X16\")")				# X16 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"bcpyol X{args[0]} X16 X17\")")	# bcopy_ops Xop1, Xd, Xnumops
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")				# X16 = addr
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")
		
		# bcopy_opsi Xop1, Xd, $numops
		# args = [reg_id, addr, numops]
		case "bcopy_opsi":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[1])}\")")	# X16 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X16 X16\")")						# X16 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"bcopy_opsi X{args[0]} X16 {args[2]}\")")	# bcopy_opsi Xop1, Xd, $numops
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")						# X16 = addr
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")
		
		# bcpyoli Xop1, Xd, $numops
		# args = [reg_id, addr, numops]
		case "bcpyoli":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[1])}\")")	# X16 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X16 X16\")")				# X16 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"bcpyoli X{args[0]} X16 {args[2]}\")")	# bcpyoli Xop1, Xd, $numops
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")				# X16 = addr
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")

		# cmpswp X1, X2, X3, X4
		# LM[X1] = X4 if LM[X1] == X3 (X2 = LM[X1])
		# args = [addr, addr_val, X3_val, X4_val]
		case "cmpswp":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = addr

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X20 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X20 X20 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X20 X20 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X20 X20 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X20 X20 12 {num_split_p4(args[1])}\")")	# X20 = addr_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X7 X16\")")						# X16 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"move X20 0(X16) 0 8\")")

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X18 {num_split_p0(args[2])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p4(args[2])}\")")	# X18 = X3_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X19 {num_split_p0(args[3])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X19 X19 12 {num_split_p1(args[3])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X19 X19 12 {num_split_p2(args[3])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X19 X19 12 {num_split_p3(args[3])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X19 X19 12 {num_split_p4(args[3])}\")")	# X19 = X4_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"cmpswp X16 X17 X18 X19\")")				# LM[X16] = X19 if LM[X16] == X18 (X17 = LM[X16])
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")						# X16 = addr - X7
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")

		# cswp X1, X2, X3, X4
		# LM[X1] = X4 if LM[X1] == X3 (X2 = LM[X1])
		# args = [addr, addr_val, X3_val, X4_val]
		case "cswp":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = addr

			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X20 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X20 X20 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X20 X20 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X20 X20 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X20 X20 12 {num_split_p4(args[1])}\")")	# X20 = addr_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X7 X16\")")						# X16 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X20 0(X16) 0 8\")")

			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X18 {num_split_p0(args[2])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p4(args[2])}\")")	# X18 = X3_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X19 {num_split_p0(args[3])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X19 X19 12 {num_split_p1(args[3])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X19 X19 12 {num_split_p2(args[3])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X19 X19 12 {num_split_p3(args[3])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X19 X19 12 {num_split_p4(args[3])}\")")	# X19 = X4_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"cswp X16 X17 X18 X19\")")				# LM[X16] = X19 if LM[X16] == X18 (X17 = LM[X16])
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")						# X16 = addr - X7
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")

		# cmpswpi X1, X2, $imm1, $imm2
		# LM[X1] = $imm2 if LM[X1] == $imm1 (X2 = LM[X1])
		# args = [addr, addr_val, imm1, imm2]
		case "cmpswpi":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = addr

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X20 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X20 X20 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X20 X20 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X20 X20 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X20 X20 12 {num_split_p4(args[1])}\")")	# X20 = addr_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X7 X16\")")						# X16 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"move X20 0(X16) 0 8\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"cmpswpi X16 X17 {args[2]} {args[3]}\")")				# LM[X16] = X19 if LM[X16] == X18 (X17 = LM[X16])
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")						# X16 = addr - X7
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")

		# cswpi X1, X2, $imm1, $imm2
		# LM[X1] = $imm2 if LM[X1] == $imm1 (X2 = LM[X1])
		# args = [addr, addr_val, imm1, imm2]
		case "cswpi":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = addr

			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X20 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X20 X20 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X20 X20 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X20 X20 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X20 X20 12 {num_split_p4(args[1])}\")")	# X20 = addr_val

			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X7 X16\")")				# X16 = X7 + addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X20 0(X16) 0 8\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"cswpi X16 X17 {args[2]} {args[3]}\")")	# LM[X16] = X19 if LM[X16] == X18 (X17 = LM[X16])
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")				# X16 = addr - X7
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")

		# mov_reg2reg Xs, Xd
		# Xd ← Xs
		# args = [val, Xs_id, Xd_id]
		case "mov_reg2reg":
			Xs_id = args[1]
			if Xs_id >= 16:
				prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X{Xs_id} {num_split_p0(args[0])}\")")				
				prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X{Xs_id} X{Xs_id} 12 {num_split_p1(args[0])}\")")	
				prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X{Xs_id} X{Xs_id} 12 {num_split_p2(args[0])}\")")	
				prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X{Xs_id} X{Xs_id} 12 {num_split_p3(args[0])}\")")	
				prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X{Xs_id} X{Xs_id} 12 {num_split_p4(args[0])}\")")	# Xs = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X{Xs_id} X{args[2]}\")")					# Xd = Xs
			if args[2] != 31:
				prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X7 X31\")")								# X31 = X7
				prog_lines.append(str_tab + f"tran0.writeAction(\"move X{args[2]} 0(X31) 0 8\")")							# LM(0) = Xs
			else:
				prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X7 X16\")")								# X16 = X7
				prog_lines.append(str_tab + f"tran0.writeAction(\"move X{args[2]} 0(X16) 0 8\")")							# LM(0) = Xs
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")
		
		# movrr Xs, Xd
		# Xd ← Xs
		# args = [val, Xs_id, Xd_id]
		case "movrr":
			Xs_id = args[1]
			if Xs_id >= 16:
				prog_lines.append(str_tab + f"tran0.writeAction(\"movir X{Xs_id} {num_split_p0(args[0])}\")")					
				prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X{Xs_id} X{Xs_id} 12 {num_split_p1(args[0])}\")")	
				prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X{Xs_id} X{Xs_id} 12 {num_split_p2(args[0])}\")")	
				prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X{Xs_id} X{Xs_id} 12 {num_split_p3(args[0])}\")")	
				prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X{Xs_id} X{Xs_id} 12 {num_split_p4(args[0])}\")")	# Xs = val
			prog_lines.append(str_tab + f"tran0.writeAction(\"movrr X{Xs_id} X{args[2]}\")")					# Xd = Xs
			if args[2] != 31:
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrr X7 X31\")")									# X31 = X7
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X{args[2]} 0(X31) 0 8\")")					# LM(0) = Xs
			else:
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrr X7 X16\")")									# X16 = X7
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X{args[2]} 0(X16) 0 8\")")					# LM(0) = Xs
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")

		# mov_imm2reg Xd, $imm
		# Xd ← $imm
		# args = [imm, Xd_id]
		case "mov_imm2reg":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X{args[1]} {args[0]}\")")					# Xd = imm
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")
		
		# movir Xd, $imm
		# Xd ← $imm
		# args = [imm, Xd_id]
		case "movir":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X{args[1]} {args[0]}\")")					# Xd = imm
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")
		
		# swizzle Xs, Xd
		# Xd = Xd[based on mask in Xs]
		# args = [mask, addr, addr_new]
		case "swizzle":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = mask = Xs

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = addr = Xd

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X17 X18\")")								# X18 = X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"swizzle X16 X17\")")									# swizzle Xs, Xd
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")


		# swiz Xs, Xd
		# Xd = Xd[based on mask in Xs]
		# args = [mask, addr, addr_new]
		case "swiz":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = mask = Xs

			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = addr = Xd

			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X17 X18 0\")")								# X18 = X17 = addr
			prog_lines.append(str_tab + f"tran0.writeAction(\"swiz X16 X17\")")									# swizzle Xs, Xd
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")

		# mov_uip2reg Xd
		# Xd = UIP
		# args = [Xd_id]
		case "mov_uip2reg":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_uip2reg X{args[0]}\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")


		# movipr Xd
		# Xd = UIP
		# args = [Xd_id]
		case "movipr":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movipr X{args[0]}\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")

		# copy Xs, Xt, Xd
		# Xs - source pointer, Xt - destination pointer. 
		# update Xs, Xt and Xd. 
		# Xd=0 when copy is done
		# args = [Xs_addr, Xt_addr, len, Xs_addr_val_list_old, Xt_addr_val_list]
		case "copy":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X21\")")								# X21 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X7 X16\")")									# X16 = Xs + X7

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = Xt
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X17 X22\")")								# X22 = Xt
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X17 X7 X17\")")									# X17 = Xt + X7

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X18 {num_split_p0(args[2])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X18 X18 12 {num_split_p4(args[2])}\")")	# X18 = Xd
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X18 X23\")")								# X23 = Xd = len

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X19\")")			# X19 = Xs + X7
			for i in range(0,args[2]):
				prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X20 {args[3][i]}\")")	# X20 = Xs_addr_val_list_old[i]
				prog_lines.append(str_tab + f"tran0.writeAction(\"move X20 0(X19) 0 8\")")		# LM(X19) = X20
				prog_lines.append(str_tab + f"tran0.writeAction(\"addi X19 X19 1\")")			# X19 = X19 + 1
			prog_lines.append(str_tab + f"tran0.writeAction(\"copy X16 X17 X18\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")


		# bcpyll Xs, Xt, Xd
		# Xs - source pointer, Xt - destination pointer. 
		# update Xs, Xt and Xd. 
		# Xd=0 when copy is done
		# args = [Xs_addr, Xt_addr, len, Xs_addr_val_list_old, Xt_addr_val_list]
		case "bcpyll":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X21 0\")")								# X21 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X7 X16\")")									# X16 = Xs + X7

			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = Xt
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X17 X22 0\")")								# X22 = Xt
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X17 X7 X17\")")									# X17 = Xt + X7

			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X18 {num_split_p0(args[2])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p1(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p2(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p3(args[2])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X18 X18 12 {num_split_p4(args[2])}\")")	# X18 = Xd
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X18 X23 0\")")								# X23 = Xd = len

			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X19 0\")")			# X19 = Xs + X7
			for i in range(0,args[2]):
				prog_lines.append(str_tab + f"tran0.writeAction(\"movir X20 {args[3][i]}\")")	# X20 = Xs_addr_val_list_old[i]
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X20 0(X19) 0 8\")")		# LM(X19) = X20
				prog_lines.append(str_tab + f"tran0.writeAction(\"addi X19 X19 1\")")			# X19 = X19 + 1
			prog_lines.append(str_tab + f"tran0.writeAction(\"bcpyll X16 X17 X18\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")


		# copy_imm Xs, Xt, $length
		# Xs - source pointer, Xt - destination pointer. 
		# update Xs, Xt. 
		# args = [Xs_addr, Xt_addr, len, Xs_addr_val_list_old, Xt_addr_val_list]
		case "copy_imm":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X21\")")								# X21 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X7 X16\")")									# X16 = Xs + X7

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = Xt
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X17 X22\")")								# X22 = Xt
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X17 X7 X17\")")									# X17 = Xt + X7

			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X19\")")			# X19 = Xs + X7
			for i in range(0,args[2]):
				prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X20 {args[3][i]}\")")	# X20 = Xs_addr_val_list_old[i]
				prog_lines.append(str_tab + f"tran0.writeAction(\"move X20 0(X19) 0 8\")")			# LM(X19) = X20
				prog_lines.append(str_tab + f"tran0.writeAction(\"addi X19 X19 1\")")				# X19 = X19 + 1
			prog_lines.append(str_tab + f"tran0.writeAction(\"copy_imm X16 X17 {args[2]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")


		# bcpylli Xs, Xt, $length
		# Xs - source pointer, Xt - destination pointer. 
		# update Xs, Xt. 
		# args = [Xs_addr, Xt_addr, len, Xs_addr_val_list_old, Xt_addr_val_list]
		case "bcpylli":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X21 0\")")								# X21 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X7 X16\")")									# X16 = Xs + X7

			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 {num_split_p0(args[1])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p1(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p2(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p3(args[1])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X17 X17 12 {num_split_p4(args[1])}\")")	# X17 = Xt
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X17 X22 0\")")								# X22 = Xt
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X17 X7 X17\")")									# X17 = Xt + X7

			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X19 0\")")			# X19 = Xs + X7
			for i in range(0,args[2]):
				prog_lines.append(str_tab + f"tran0.writeAction(\"movir X20 {args[3][i]}\")")	# X20 = Xs_addr_val_list_old[i]
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X20 0(X19) 0 8\")")		# LM(X19) = X20
				prog_lines.append(str_tab + f"tran0.writeAction(\"addi X19 X19 1\")")			# X19 = X19 + 1
			prog_lines.append(str_tab + f"tran0.writeAction(\"bcpylli X16 X17 {args[2]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X7 X16\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X17 X7 X17\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")

		
		# put_bits Xs,$len,$bits
		# X = $len; LM[Xs].writeXBit($bits);
		# args = [Xs, len, bits, Xs_byte_addr, real_bits_val]
		case "put_bits":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X21\")")								# X21 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift X7 X19 3\")")									# X19 = X7 << 3 = X7*8
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X19 X16\")")									# X16 = Xs + X7*8

			prog_lines.append(str_tab + f"tran0.writeAction(\"put_bits X16 {args[1]} {args[2]}\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")

		
		# movbil Xs,$len,$bits
		# X = $len; LM[Xs].writeXBit($bits);
		# args = [Xs, len, bits, Xs_byte_addr, real_bits_val]
		case "movbil":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X21 0\")")								# X21 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"sli X7 X19 3\")")									# X19 = X7 << 3 = X7*8
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X19 X16\")")									# X16 = Xs + X7*8

			prog_lines.append(str_tab + f"tran0.writeAction(\"movbil X16 {args[1]} {args[2]}\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")


		# get_bits Xs, Xd, $len
		# X = $len; Xd = LM[Xs].readXBit();
		# args = [Xs, len, bits, Xs_byte_addr, real_bits_val, valid_bits]
		case "get_bits":
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_imm2reg X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift_or_imm X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"mov_reg2reg X16 X21\")")								# X21 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"lshift X7 X19 3\")")									# X19 = X7 << 3 = X7*8
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X19 X16\")")									# X16 = Xs + X7*8

			prog_lines.append(str_tab + f"tran0.writeAction(\"put_bits X16 7 {args[2]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"get_bits X16 X17 {args[1]}\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yield_terminate\")")

		
		# movblr Xs, Xd, $len
		# X = $len; Xd = LM[Xs].readXBit();
		# args = [Xs, len, bits, Xs_byte_addr, real_bits_val, valid_bits]
		case "movblr":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {num_split_p0(args[0])}\")")			
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p1(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p2(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p3(args[0])}\")")	
			prog_lines.append(str_tab + f"tran0.writeAction(\"slorii X16 X16 12 {num_split_p4(args[0])}\")")	# X16 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X21 0\")")								# X21 = Xs
			prog_lines.append(str_tab + f"tran0.writeAction(\"sli X7 X19 3\")")									# X19 = X7 << 3 = X7*8
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X19 X16\")")									# X16 = Xs + X7*8

			prog_lines.append(str_tab + f"tran0.writeAction(\"movbil X16 7 {args[2]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movblr X16 X17 {args[1]}\")")
			prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")



		

		
		case _:
			print("Instruction not implemented yet, exit.")
			sys.exit()

	return

# Add code to generate corresponding random arguments
def generate_random_args(instruction: str) -> list:
	args = []
	match instruction:
		# movil2(put_2bytes_imm) Xs, $bytes
		# LM[Xs].write2Byte($bytes); Xs+=2
		# args = [addr, $bytes]
		case "movil2" | "put_2byte_imm":
			addr = random.randint(0, local_memory_boundary - 2)
			val = random.randint(0, max_2_bytes)
			args = [addr, val]

		# movil1(put_1byte_imm) Xs, $bytes
		# LM[Xs].write1Byte($bytes); Xs+=1
		# args = [addr, $bytes]
		case "movil1" | "put_1byte_imm":
			addr = random.randint(0, local_memory_boundary - 1)
			val = random.randint(0, max_1_byte)
			args = [addr, val]

		# movrl(move) Xs, $imm(Xd), $inc_flag, $bytes
		# LM[Xd+$imm : Xd+$imm +$bytes-1] ← Xs & mask. If $inc_flag==1, Xd += $bytes
		# args = [val, imm_val, addr, inc_flag, byte_num]
		case "movrl" | "move_reg2lm":
			imm_val = int(random.randint(min_int_12, max_int_12)) 
			byte_num = random.randint(1, 8)
			# byte_num = 8
			inc_flag = int(random.randint(0, 1))
			addr_old = random.randint(0, local_memory_boundary - byte_num)
			addr = addr_old - imm_val
			val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			args = [val, imm_val, addr, inc_flag, byte_num]

		# movlr(move) $imm(Xs), Xd, $inc_flag, $bytes
		# Xd ← LM[Xs+$imm : Xs+$imm +$bytes-1] & mask. If $inc_flag==1, Xs += $bytes
		# args = [val, imm_val, addr, inc_flag, byte_num]
		case "movlr" | "move_lm2reg":
			imm_val = int(random.randint(min_int_12, max_int_12)) 
			byte_num = random.randint(1, 8)
			# byte_num = 8
			inc_flag = int(random.randint(0, 1))
			addr_old = random.randint(0, local_memory_boundary - byte_num)
			addr = addr_old - imm_val
			val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			args = [val, imm_val, addr, inc_flag, byte_num]

		# movwrl(move_word) Xs, Xb(Xd, $inc_flag, $scale)
		# LM[Xb+(Xd<<($scale+3)):Xb+(Xd<<($scale+3))+7] ← Xs. If $inc_flag==1, Xd += 1
		# args = [val, Xb_val, Xd_val, inc_flag, scale, addr]
		case "movwrl" | "move_word_reg2lm":
			val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			addr = int(random.randint(0, local_memory_boundary - 8))
			inc_flag = int(random.randint(0, 1))
			scale = int(random.randint(0, 7))
			Xd_val = addr >> (scale+3)
			Xb_val = addr - (Xd_val << (scale+3))
			args = [val, Xb_val, Xd_val, inc_flag, scale, addr]

		# movwlr(move_word) Xb(Xs, $inc_flag, $scale), Xd
		# Xd←LM[Xb+(Xs<<($scale+3)):Xb+(Xs<<($scale+3))+7]. If $inc_flag==1, Xs += 1
		# args = [val, Xb_val, Xs_val, inc_flag, scale, addr]
		case "movwlr" | "move_word_lm2reg":
			val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			addr = int(random.randint(0, local_memory_boundary - 8))
			inc_flag = int(random.randint(0, 1))
			scale = int(random.randint(0, 7))
			Xs_val = addr >> (scale+3)
			Xb_val = addr - (Xs_val << (scale+3))
			args = [val, Xb_val, Xs_val, inc_flag, scale, addr]

		# bcpyol(bcopy_ops) Xop1, Xd, Xnumops
		# args = [reg_id, addr, numops]
		case "bcpyol" | "bcopy_ops":
			reg_id = random.randint(8,15)
			numops = random.randint(1,16-reg_id)
			addr = int(random.randint(0, local_memory_boundary - numops))
			args = [reg_id, addr, numops]


		# bcpyoli(bcopy_opsi) Xop1, Xd, $numops
		# args = [reg_id, addr, numops]
		case "bcpyoli" | "bcopy_opsi":
			reg_id = random.randint(8,15)
			numops = random.randint(1,16-reg_id)
			addr = int(random.randint(0, local_memory_boundary - numops))
			args = [reg_id, addr, numops]
		
		
		# cswp(cmpswp) X1, X2, X3, X4
		# LM[X1] = X4 if LM[X1] == X3 (X2 = LM[X1])
		# args = [addr, addr_val, X3_val, X4_val]
		case "cswp" | "cmpswp":
			addr_val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			X3_val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			X4_val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			if random.randint(0, 1) == 0:
				X3_val = addr_val
			addr = int(random.randint(0, local_memory_boundary - 8))
			args = [addr, addr_val, X3_val, X4_val]


		# cswpi(cmpswpi) X1, X2, $imm1, $imm2
		# LM[X1] = $imm2 if LM[X1] == $imm1 (X2 = LM[X1])
		# args = [addr, addr_val, imm1, imm2]
		case "cswpi" | "cmpswpi":
			addr = int(random.randint(0, local_memory_boundary - 8))
			addr_val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			imm1 = random.randint(min_int_4, max_int_4)
			imm2 = random.randint(min_int_4, max_int_4)
			if random.randint(0, 1) == 0:
				addr_val = imm1
			args = [addr, addr_val, imm1, imm2]

		# movrr(mov_reg2reg) Xs, Xd
		# Xd ← Xs
		# args = [val, Xs_id, Xd_id]
		case "movrr" | "mov_reg2reg":
			val = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			Xs_id = random.randint(0,31)
			Xd_id = random.randint(16,31)
			args = [val, Xs_id, Xd_id]

		# movir(mov_imm2reg) Xd, $imm
		# Xd ← $imm
		# args = [imm, Xd_id]
		case "movir" | "mov_imm2reg":
			imm = random.randint(min_int_21, max_int_21)
			Xd_id = random.randint(16,31)
			args = [imm, Xd_id]

		# swiz(swizzle) Xs, Xd
		# Xd = Xd[based on mask in Xs]
		# args = [mask, addr, addr_new]
		case "swiz" | "swizzle":
			y = random.randint(1, 15)
			mask = 0
			for i in range(21,-1,-1):
				mask = mask << 1
				if i >= y+6:
					mask += 1
				elif i <= y-1:
					mask += 1
			
			mask_p = 0
			for i in range(0,42,1):
				mask_p = mask_p << 1
				mask_p += 1
			# print("%x" %(mask_p))
			mask_p = mask_p << 22
			# print("%x" %(mask_p))

			mask_f = 0
			mask_b = 0
			mask_c = 0
			for i in range(21,-1,-1):
				mask_f = mask_f << 1
				mask_b = mask_b << 1
				mask_c = mask_c << 1
				if i >= y+6:
					mask_f += 1
				elif i <= y-1:
					mask_c += 1
				else:
					mask_b += 1

			addr = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
			addr_new = (addr & mask_p) + ((addr & mask_b) << (16-y)) + ((addr & mask_f) >> 6) + (addr & mask_c)
			# print("%d %x %x %x %x %x %x %x" %(y,addr,addr_new,mask,mask_p,mask_f,mask_b,mask_c))
			args = [mask, addr, addr_new]


		# movipr(mov_uip2reg) Xd
		# Xd = UIP
		# args = [Xd_id]
		case "movipr" | "mov_uip2reg":
			Xd_id = random.randint(16,31)
			args = [Xd_id]
	
		
		# bcpyll(copy) Xs, Xt, Xd
		# Xs - source pointer, Xt - destination pointer. 
		# update Xs, Xt and Xd. 
		# Xd=0 when copy is done
		# args = [Xs_addr, Xt_addr, len, Xs_addr_val_list_old, Xt_addr_val_list]
		case "bcpyll" | "copy":
			len = int(random.randint(0, 30))
			# len = int(random.randint(0, local_memory_boundary))
			Xs_addr = random.randint(0, local_memory_boundary - len)
			Xt_addr = random.randint(0, local_memory_boundary - len)
			while Xt_addr in range(Xs_addr-len+1,Xs_addr+len):
				Xt_addr = random.randint(0, local_memory_boundary - len)
			Xs_addr_val_list = []
			Xt_addr_val_list = []
			for i in range(0,len):
				val = random.randint(0, max_1_byte)
				Xs_addr_val_list.append(val)
				Xt_addr_val_list.append(val)
			args = [Xs_addr, Xt_addr, len, Xs_addr_val_list, Xt_addr_val_list]
		
		# bcpylli(copy_imm) Xs, Xt, $length
		# Xs - source pointer, Xt - destination pointer. 
		# update Xs, Xt. 
		# args = [Xs_addr, Xt_addr, len, Xs_addr_val_list_old, Xt_addr_val_list]
		case "bcpylli" | "copy_imm":
			len = int(random.randint(0, 30))
			# len = int(random.randint(0, local_memory_boundary))
			Xs_addr = random.randint(0, local_memory_boundary - len)
			Xt_addr = random.randint(0, local_memory_boundary - len)
			while Xt_addr in range(Xs_addr-len+1,Xs_addr+len):
				Xt_addr = random.randint(0, local_memory_boundary - len)
			Xs_addr_val_list = []
			Xt_addr_val_list = []
			for i in range(0,len):
				val = random.randint(0, max_1_byte)
				Xs_addr_val_list.append(val)
				Xt_addr_val_list.append(val)
			args = [Xs_addr, Xt_addr, len, Xs_addr_val_list, Xt_addr_val_list]


		# movbil(put_bits) Xs,$len,$bits
		# X = $len; LM[Xs].writeXBit($bits);
		# args = [Xs, len, bits, Xs_byte_addr, real_bits_val]
		case "movbil" | "put_bits":
			len = int(random.randint(1, 7))
			bits = random.randint(0, 2<<7)
			mask = 0
			for i in range(0,len):
				mask = (mask << 1) + 1
			valid_bits = bits & mask
			Xs = random.randint(0, local_memory_boundary*8 - len)
			Xs_byte_addr = int(Xs/8)
			offset = Xs - Xs_byte_addr*8
			real_bits_val = valid_bits << offset
			args = [Xs, len, bits, Xs_byte_addr, real_bits_val]

		# movblr(get_bits) Xs, Xd, $len
		# X = $len; Xd = LM[Xs].readXBit();
		# args = [Xs, len, bits, Xs_byte_addr, real_bits_val, valid_bits]
		case "movblr" | "get_bits":
			len = int(random.randint(1, 7))
			bits = random.randint(0, 2<<7)
			mask = 0
			for i in range(0,len):
				mask = (mask << 1) + 1
			valid_bits = bits & mask
			Xs = random.randint(0, local_memory_boundary*8 - len)
			Xs_byte_addr = int(Xs/8)
			offset = Xs - Xs_byte_addr*8
			real_bits_val = (bits & 0b1111111) << offset
			args = [Xs, len, bits, Xs_byte_addr, real_bits_val, valid_bits]

		case _:
			print("Instruction not implemented yet, exit.")
			sys.exit()

	return args

# Add google test code to assert the results
def generate_assertion(instruction: str, test_lines: list, args: list):
	match instruction:
		# movil2(put_2bytes_imm) Xs, $bytes
		# LM[Xs].write2Byte($bytes); Xs+=2
		# args = [addr, $bytes]
		case "movil2" | "put_2byte_imm":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[0]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]+2}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, {args[0]+8}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {args[0]}, {args[1]}));")
		
		# movil1(put_1byte_imm) Xs, $bytes
		# LM[Xs].write1Byte($bytes); Xs+=1
		# args = [addr, $bytes]
		case "movil1" | "put_1byte_imm":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[0]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]+1}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, {args[0]+8}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {args[0]}, {args[1]}));")

		# movrl(move) Xs, $imm(Xd), $inc_flag, $bytes
		# LM[Xd+$imm : Xd+$imm +$bytes-1] ← Xs & mask. If $inc_flag==1, Xd += $bytes
		# args = [val, imm_val, addr, inc_flag, byte_num]
		case "movrl" | "move_reg2lm":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, {args[2]}));")
			mask = 0
			for i in range(0,args[4]*8):
				mask = (mask << 1) + 1
			# print("mask = %lx" %(mask))
			store_val = int(args[0]) & mask
			addr = int(args[1]) + int(args[2])
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {addr}, {store_val}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[2] + args[3] * args[4]}));")
			
		# movlr(move) $imm(Xs), Xd, $inc_flag, $bytes
		# Xd ← LM[Xs+$imm : Xs+$imm +$bytes-1] & mask. If $inc_flag==1, Xs += $bytes
		# args = [val, imm_val, addr, inc_flag, byte_num]
		case "movlr" | "move_lm2reg":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, {args[2]}));")
			addr = int(args[1]) + int(args[2])
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {addr}, {args[0]}u));")
			mask = 0
			for i in range(0,args[4]*8):
				mask = (mask << 1) + 1
			load_val = args[0] & mask
			# print("mask = %lx, val = %ld (%lx), load_val = %ld (%lx) %d" %(mask,args[0],args[0],load_val,load_val,args[4]))
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X19, {load_val}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[2] + args[3] * args[4]}));")

		# movwrl(move_word) Xs, Xb(Xd, $inc_flag, $scale)
		# LM[Xb+(Xd<<($scale+3)):Xb+(Xd<<($scale+3))+7] ← Xs. If $inc_flag==1, Xd += 1
		# args = [val, Xb_val, Xd_val, inc_flag, scale, addr]
		case "movwrl" | "move_word_reg2lm":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[1]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X19, {args[2]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, {args[2]}u+{args[3]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {args[5]}, {args[0]}u));")

		# movwlr(move_word) Xb(Xs, $inc_flag, $scale), Xd
		# Xd←LM[Xb+(Xs<<($scale+3)):Xb+(Xs<<($scale+3))+7]. If $inc_flag==1, Xs += 1
		# args = [val, Xb_val, Xs_val, inc_flag, scale, addr]
		case "movwlr" | "move_word_lm2reg":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[1]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X19, {args[2]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, {args[2]}u+{args[3]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {args[5]}, {args[0]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X20, {args[0]}u));")

		# bcpyol(bcopy_ops) Xop1, Xd, Xnumops
		# args = [reg_id, addr, numops]
		case "bcpyol" | "bcopy_ops":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[1]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[2]}));")
			for i in range(0,args[2]):
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {args[1]+i*8}, {i+args[0]}));")


		# bcpyoli(bcopy_opsi) Xop1, Xd, $numops
		# args = [reg_id, addr, numops]
		case "bcpyoli" | "bcopy_opsi":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[1]}));")
			for i in range(0,args[2]):
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {args[1]+i*8}, {i+args[0]}));")
		
		# cswp(cmpswp) X1, X2, X3, X4
		# LM[X1] = X4 if LM[X1] == X3 (X2 = LM[X1])
		# args = [addr, addr_val, X3_val, X4_val]
		case "cswp" | "cmpswp":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, {args[2]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X19, {args[3]}u));")
			if args[1] == args[2]:
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[1]}u));")
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i<<16) + {args[0]}, {args[3]}u));")
			else:
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[1]}u));")
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i<<16) + {args[0]}, {args[1]}u));")


		# cswpi(cmpswpi) X1, X2, $imm1, $imm2
		# LM[X1] = $imm2 if LM[X1] == $imm1 (X2 = LM[X1])
		# args = [addr, addr_val, imm1, imm2]
		case "cswpi" | "cmpswpi":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}));")
			if args[1] == args[2]:
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[1]}));")
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i<<16) + {args[0]}, {args[3]}));")
			else:
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[1]}u));")
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i<<16) + {args[0]}, {args[1]}u));")


		# movrr(mov_reg2reg) Xs, Xd
		# Xd ← Xs
		# args = [val, Xs_id, Xd_id]
		case "movrr" | "mov_reg2reg":
			Xs_id = args[1]
			Xd_id = args[2]
			if Xs_id >= 16:
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X{Xd_id}, {args[0]}u));")
			test_lines.append(str_tab + str_tab + f"word_t reg_val=0;")
			test_lines.append(str_tab + str_tab + f"acc0.readScratchPad(8, i << 16, (uint8_t*)&reg_val);")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X{Xd_id}, reg_val));")

		# movir(mov_imm2reg) Xd, $imm
		# Xd ← $imm
		# args = [imm, Xd_id]
		case "movir" | "mov_imm2reg":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X{args[1]}, {args[0]}));")

		# swiz(swizzle) Xs, Xd
		# Xd = Xd[based on mask in Xs]
		# args = [mask, addr, addr_new]
		case "swiz" | "swizzle":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[2]}u));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18, {args[1]}u));")

		# movipr(mov_uip2reg) Xd
		# Xd = UIP
		# args = [Xd_id]
		case "movipr" | "mov_uip2reg":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X{args[0]}, 4));")

		# bcpyll(copy) Xs, Xt, Xd
		# Xs - source pointer, Xt - destination pointer. 
		# update Xs, Xt and Xd. 
		# Xd=0 when copy is done
		# args = [Xs_addr, Xt_addr, len, Xs_addr_val_list_old, Xt_addr_val_list]
		case "bcpyll" | "copy":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X21, {args[0]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X22, {args[1]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X23, {args[2]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}+{args[2]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[1]}+{args[2]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X18,0));")
			test_lines.append(str_tab + str_tab + f"uint8_t val=0;")
			for j in range(0,args[2]):
				test_lines.append(str_tab + str_tab + f"acc0.readScratchPad(1, (i<<16) + {args[1]+j}, (uint8_t*)&val);")
				# test_lines.append(str_tab + str_tab + f"printf(\"%lu {args[4][j]}\\n\",val);")
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(val == {args[4][j]}u);")

		# bcpylli(copy_imm) Xs, Xt, $length
		# Xs - source pointer, Xt - destination pointer. 
		# update Xs, Xt. 
		# args = [Xs_addr, Xt_addr, len, Xs_addr_val_list_old, Xt_addr_val_list]
		case "bcpylli" | "copy_imm":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X21, {args[0]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X22, {args[1]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, {args[0]}+{args[2]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[1]}+{args[2]}));")
			test_lines.append(str_tab + str_tab + f"word_t val=0;")
			for j in range(0,args[2]):
				test_lines.append(str_tab + str_tab + f"acc0.readScratchPad(1, (i<<16) + {args[1]+j}, (uint8_t*)&val);")
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(val == {args[4][j]}u);")

		# movbil(put_bits) Xs,$len,$bits
		# X = $len; LM[Xs].writeXBit($bits);
		# args = [Xs, len, bits, Xs_byte_addr, real_bits_val]
		case "movbil" | "put_bits":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X21, {args[0]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i<<16) + {args[3]}, {args[4]}u));")

		# movblr(get_bits) Xs, Xd, $len
		# X = $len; Xd = LM[Xs].readXBit();
		# args = [Xs, len, bits, Xs_byte_addr, real_bits_val, valid_bits]
		case "movblr" | "get_bits":
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X21, {args[0]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X17, {args[5]}));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i<<16) + {args[3]}, {args[4]}u));")


		


		
		

		case _:
			print("Instruction not implemented yet, exit.")
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
	
