import sys
import random
from pathlib import Path, PosixPath
import subprocess
import argparse
import os

transition_idx = {
	0: "common_TX",
}

transition_map = {
	"event_TX": "eventCarry",
	"common_TX": "commonCarry_with_action",
}

def get_transition_eventLabel(instruction: str, transition: int):
	if instruction == "siw" and transition == 0:
		return 56
	if instruction == "refill" and transition == 0:
		return 80
	if instruction == "movlsb" and transition == 0:
		return 1092
	if instruction == "movsbr" and transition == 0:
		return 72
	if instruction == "movsbr_cycle" and transition == 0:
		return 72
	if instruction == "ssprop" and transition == 0:
		return 60

	return 0

# transition_eventLabel = {
# 	"event_TX": 0,
# 	"common_TX": 52,
# }

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
test_path = Path(f'../tests/inst_unit_tests/{inst_type}_test.cpp') # The c++ google test script
prog_path = Path('./efas/') # The directory to hold the efa programs
# top_exe_path = Path('fastsim_exe_jiya') # The top program to generate expected results
bin_path = Path("efa2bin.py")


def generate_efa_unit_test(test_path: PosixPath, prog_path: PosixPath, instruction: str, args: list, transition: int):
	prog_lines = ["from EFA_v2 import *"]
	prog_lines.append(f"def {prog_path.stem}():")
	prog_lines.append(str_tab + "efa = EFA([])")
	prog_lines.append(str_tab + "efa.code_level = \"machine\"")
	prog_lines.append(str_tab + "state = State()")
	prog_lines.append(str_tab + "efa.add_initId(state.state_id)")
	prog_lines.append(str_tab + "efa.add_state(state)")
	prog_lines.append(str_tab + "state0 = State()")
	prog_lines.append(str_tab + "state0.alphabet = [0-255]")
	prog_lines.append(str_tab + "efa.add_state(state0)")
	prog_lines.append(str_tab + f"tran0 = state.writeTransition(\"{transition_map[transition_idx[transition]]}\", state, state0, 1)")
			
	# args = [val[16], rdMode, issueWidth, advanceWidth, byte_offset ...]
	if(inst_type == "movlsb" or inst_type == "movsbr" or inst_type == "movsbr_cycle"):
		prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 0\")")
		prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X17 X17\")")								# X17 = X7
		for i in range(16):
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
	
	prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X20 {args[4]}\")") # X20 = X7 + btye_offset = SBP in byte address
	prog_lines.append(str_tab + f"tran0.writeAction(\"movir X21 0\")")		    # X21 = 0
	if args[1] == 1:	# SBMode (StreamBuffer Mode)
		prog_lines.append(str_tab + f"tran0.writeAction(\"sli X20 X20 3\")")	# X20 = X20 << 3 = X20 * 8 bit_address
		prog_lines.append(str_tab + f"tran0.writeAction(\"addi X21 X17 {args[4]*8 + 512}\")")
	else: # LMMode (LocalMemory Mode)
		prog_lines.append(str_tab + f"tran0.writeAction(\"addi X21 X17 {args[4] + 64}\")")
	prog_lines.append(str_tab + f"tran0.writeAction(\"add X20 X21 X5\")")		# X5 (SBP) = X20
	prog_lines.append(str_tab + f"tran0.writeAction(\"or X17 X16 X4\")")		# Update maxSBP to SBP
	prog_lines.append(str_tab + f"tran0.writeAction(\"addi X4 X18 0\")")
	# prog_lines.append(str_tab + f"tran0.writeAction(\"yield\")")
	prog_lines.append(str_tab + f"tran0.writeAction(\"lastact\")")

	prog_lines.append(str_tab + f"tran1 = state0.writeTransition(\"{transition_map[transition_idx[transition]]}\", state0, state0, 0)")



	test_lines = [f"TEST_F({inst_type}, Basic_{prog_path.stem}){{",
			str_tab + f"acc0.initSetup(0, \"testprogs/binaries/{prog_path.stem}.bin\", 0);",
			str_tab + f"int numop = 8;",
			str_tab + f"eventword_t ev0(0);",
			str_tab + f"ev0.setEventLabel({get_transition_eventLabel(instruction,transition)});",
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
		
	generate_assertion(instruction, test_lines, args, transition)


	generate_efa(instruction, prog_lines, args, transition)
	prog_lines.append(str_tab + f"tran1.writeAction(\"yieldt\")")
	
	prog_lines.append(str_tab + f"efa.appendBlockAction(\"end_of_input_terminate_efa1\",\"sub X31 X10 X31\")")
	prog_lines.append(str_tab + f"efa.appendBlockAction(\"end_of_input_terminate_efa1\",\"yieldt\")")
	prog_lines.append(str_tab + f"efa.linkBlocktoState(\"end_of_input_terminate_efa1\", state0)")

	prog_lines.append(str_tab + "return efa")

	with open(prog_path, 'w') as writer:
		writer.writelines('\n'.join(prog_lines) + '\n')

	return test_lines

def generate_bin(efa_fname):
	os.chdir("../assembler/")
	os.system("python3 " + str(bin_path) + " --efa ../testprogs/efas/" + efa_fname + " --outpath ../testprogs/binaries/ --toplinker  --debug-messages " )
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
		for t in range(1):
			test_lines = generate_efa_unit_test(test_path, prog_path.joinpath(f'{instruction}_{i}_{transition_idx[t]}.py'), instruction, args, t)
			generate_bin(f'{instruction}_{i}_{transition_idx[t]}.py')
			print(f'{instruction}_{i}_{transition_idx[t]}.py')
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
def generate_efa(instruction: str, prog_lines: list, args: list, transition: int):
	if instruction == "siw":
		# siw $width
		# SBCR.issue_width = $width
		# args = [val, rdMode, issueWidth, advanceWidth, byte_offset = 0, new_issueWidth]
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X4 X16 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"siw {args[5]}\")")
			
	elif instruction == "refill":
		# refill $imm
		# SBP ← SBP - $imm + SBCR.advance_width
		# args = [val, rdMode, issueWidth, advanceWidth, byte_offset = 0, val2, imm, SBP_val]
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X16 {num_split_p0(args[5])}\")")			
		prog_lines.append(str_tab + f"tran1.writeAction(\"slorii X16 X16 12 {num_split_p1(args[5])}\")")	
		prog_lines.append(str_tab + f"tran1.writeAction(\"slorii X16 X16 12 {num_split_p2(args[5])}\")")	
		prog_lines.append(str_tab + f"tran1.writeAction(\"slorii X16 X16 12 {num_split_p3(args[5])}\")")	
		prog_lines.append(str_tab + f"tran1.writeAction(\"slorii X16 X16 12 {num_split_p4(args[5])}\")")	# X16 = val2

		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X17 0\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"add X16 X17 X5\")")				# SBP = val2

		prog_lines.append(str_tab + f"tran1.writeAction(\"refill {args[6]}\")")				# refill $imm
			
	elif instruction == "movlsb":
		# movlsb Xs
		# SB ← LM[Xs:Xs + SB_size], Xs += SB_size
		# args = [val, rdMode = 1, issueWidth = 8, advanceWidth = 8, byte_offset]
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X7 X17 {args[4]}\")")				# X17 = X7
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X17 X16 0\")")						# X16 = X7
		prog_lines.append(str_tab + f"tran1.writeAction(\"movlsb X17\")")					

		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X7 X18 128 \")")						# X18 = X7 + 128
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X21 {args[2]}\")")

		for i in range(64):
			prog_lines.append(str_tab + f"tran1.writeAction(\"movsbr X20\")")					# X20 = SB[SBP:SBP+issueWidth]
			prog_lines.append(str_tab + f"tran1.writeAction(\"movir X21 8\")")
			prog_lines.append(str_tab + f"tran1.writeAction(\"add X5 X21 X5\")")
			prog_lines.append(str_tab + f"tran1.writeAction(\"movrl X20 0(X18) 1 1\")")			# LM[X18] = X20 & 1 byte

	elif instruction == "movsbr":
		# movsbr Xd
		# Xd ← SB[SBP:SBP + CR.issue]
		# args = [val, rdMode = 1, issueWidth, advanceWidth = 8, byte_offset = 0, SBP_addr, final_val]
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X7 X17 {args[4]}\")")		# X17 = X7 + byte_offset
		prog_lines.append(str_tab + f"tran1.writeAction(\"movlsb X17\")")					

		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X7 X20 {args[5]}\")")		# X20 = X7 + SBP_addr
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X21 0\")")					# X21 = 0
		prog_lines.append(str_tab + f"tran1.writeAction(\"add X20 X21 X5\")")				# X5 (SBP) = X20 = SBP_addr
		prog_lines.append(str_tab + f"tran1.writeAction(\"movsbr X16\")")	

	elif inst_type == "movsbr_cycle":
		# movsbr Xd
		# Xd ← SB[SBP:SBP + CR.issue]
		# args = [val, rdMode = 1, issueWidth, advanceWidth = 8, byte_offset = 63, SBP_addr = 511, final_val]
		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X7 X17 {args[4]}\")")		# X17 = X7 + byte_offset
		prog_lines.append(str_tab + f"tran1.writeAction(\"movlsb X17\")")					

		prog_lines.append(str_tab + f"tran1.writeAction(\"addi X7 X20 {args[5]}\")")		# X20 = X7 + SBP_addr
		prog_lines.append(str_tab + f"tran1.writeAction(\"movir X21 0\")")					# X21 = 0
		prog_lines.append(str_tab + f"tran1.writeAction(\"add X20 X21 X5\")")				# X5 (SBP) = X20 = SBP_addr
		prog_lines.append(str_tab + f"tran1.writeAction(\"movsbr X16\")")	



	elif instruction == "ssprop":
		# ssprop $type $value
		# set next_active_state’s property ($type, $value)
		# args = [val, rdMode, issueWidth, advanceWidth = 8, byte_offset = 0, state_type, state_val]
		prog_lines.append(str_tab + f"tran1.writeAction(\"movrr X7 X16\")")		# X16 = X7
		prog_lines.append(str_tab + f"tran1.writeAction(\"ssprop {args[5]} {args[6]}\")")
		prog_lines.append(str_tab + f"tran1.writeAction(\"movrl X6 0(X16) 0 8\")")

		
	else:
		print("Instruction not implemented yet, exit.")
		sys.exit()

	return

# Add code to generate corresponding random arguments
def generate_random_args(instruction: str) -> list:
	args = []
	if instruction == "siw":
		# siw $width
		# SBCR.issue_width = $width
		# args = [val, rdMode, issueWidth, advanceWidth, byte_offset = 0, new_issueWidth]
		val = []
		for i in range(16):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = random.randint(0,1)
		issueWidth = 1
		if(rdMode == 1): # SBMode
			issueWidth = random.randint(1,8)
		else:
			issueWidth = 1 << random.randint(0,3)

		advanceWidth = random.randint(1,8)

		new_issueWidth = 1
		if(rdMode == 1): # SBMode
			new_issueWidth = random.randint(1,8)
		else:
			new_issueWidth = 1 << random.randint(0,3)

		args = [val, rdMode, issueWidth, advanceWidth, 0, new_issueWidth]

	elif instruction == "refill":
		# refill $imm
		# SBP ← SBP - $imm + SBCR.advance_width
		# args = [val, rdMode, issueWidth, advanceWidth, byte_offset = 0, val2, imm, SBP_val]
		val = []
		for i in range(16):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = random.randint(0,1)
		issueWidth = 1
		if(rdMode == 1): # SBMode
			issueWidth = random.randint(1,8)
		else:
			issueWidth = 1 << random.randint(0,3)
		advanceWidth = random.randint(1,8)
		val2 = random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16)
		imm = random.randint(0, max_uint_16)
		SBP_val = (val2 - imm + advanceWidth) & int('ffffffffffffffff', 16)
		args = [val, rdMode, issueWidth, advanceWidth, 0, val2, imm, SBP_val]

	elif instruction == "movlsb":
		# movlsb Xs
		# SB ← LM[Xs:Xs + SB_size], Xs += SB_size
		# args = [val, rdMode = 0, issueWidth = 8, advanceWidth = 8, byte_offset]
		val = []
		for i in range(16):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = 1
		issueWidth = 8
		advanceWidth = 8
		byte_offset = random.randint(0, 63)
		# byte_offset = random.randint(0, 8) * 8
		args = [val, rdMode, issueWidth, advanceWidth, byte_offset]

	elif instruction == "movsbr":
		# movsbr Xd
		# Xd ← SB[SBP:SBP + CR.issue]
		# args = [val, rdMode = 0, issueWidth, advanceWidth = 8, SBP_addr, final_val]
		val = []
		for i in range(16):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = 1
		issueWidth = random.randint(1,8)
		advanceWidth = 8
		SBP_addr = random.randint(0, (512 - issueWidth))
		final_val = 0
		tmp_addr = SBP_addr
		for i in range(0,issueWidth):
			idx = int(tmp_addr / 64)
			low_offset = tmp_addr - (idx * 64)
			bit_val = (val[idx] >> low_offset) & 0b1
			final_val = final_val | (bit_val  << i)
			tmp_addr += 1
			
		byte_offset = 0

		args = [val, rdMode, issueWidth, advanceWidth, byte_offset, SBP_addr, final_val]

	elif inst_type == "movsbr_cycle":
		# movsbr Xd
		# Xd ← SB[SBP:SBP + CR.issue]
		# args = [val, rdMode = 1, issueWidth, advanceWidth = 8, byte_offset = 63, SBP_addr = 511, final_val]
		val = []
		for i in range(16):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = 1
		issueWidth = random.randint(1,8)
		advanceWidth = 8
		SBP_addr = 511
		final_val = 0
		tmp_addr = SBP_addr
		byte_offset = 63
		for i in range(0,issueWidth):
			idx = int(tmp_addr / 64)
			low_offset = tmp_addr - (idx * 64)
			bit_val = (val[idx] >> low_offset) & 0b1
			final_val = final_val | (bit_val  << i)
			tmp_addr += 1

		args = [val, rdMode, issueWidth, advanceWidth, byte_offset, SBP_addr, final_val]


	elif instruction == "ssprop":
		# ssprop $type $value
		# set next_active_state’s property ($type, $value)
		# args = [val, rdMode, issueWidth, advanceWidth = 8, byte_offset = 0, state_type, state_value]
		val = []
		for i in range(16):
			val.append(random.randint(min_int_64, max_int_64) & int('ffffffffffffffff', 16))
		rdMode = random.randint(0,1)
		issueWidth = 1
		if(rdMode == 1): # SBMode
			issueWidth = random.randint(1,8)
		else:
			issueWidth = 1 << random.randint(0,3)
		advanceWidth = 8
		state_type = random.randint(0,11)
		while(state_type == 8):
			state_type = random.randint(0,11)
		state_value = random.randint(0,max_uint_12)
		args = [val, rdMode, issueWidth, advanceWidth, 0, state_type, state_value]


	else:
		print("Instruction not implemented yet, exit.")
		sys.exit()

	return args

# Add google test code to assert the results
def generate_assertion(instruction: str, test_lines: list, args: list, transition: int):
	if instruction == "siw":
		# siw $width
		# SBCR.issue_width = $width
		# args = [val, rdMode, issueWidth, advanceWidth, byte_offset = 0, new_issueWidth]
		SBCR = (args[0][0] >> 41) << 41
		advanceWidth = args[3]
		SBCR1 = SBCR | (args[1] << 40) | (args[2] << 36) | (advanceWidth << 32)
		SBCR2 = SBCR | (args[1] << 40) | (args[5] << 36) | (advanceWidth << 32)
		if args[1] == 1:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, ({SBCR1}u + (({args[4]+64})<<3))));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4 , ({SBCR2}u + (({args[4]+64})<<3))));")
		else:
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X16, ({SBCR1}u + {args[4]+64})));")
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, RegId::X4 , ({SBCR2}u + {args[4]+64})));")
		
	elif instruction == "refill":
		# refill $imm
		# SBP ← SBP - $imm + SBCR.advance_width
		# args = [val, rdMode, issueWidth, advanceWidth, byte_offset = 0, val2, imm, SBP_val]
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X16), {args[5]}u));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X5), {args[7]}u));")


	elif instruction == "movlsb":
		# movlsb Xs
		# SB ← LM[Xs:Xs + SB_size], Xs += SB_size
		# args = [val, rdMode = 1, issueWidth = 8, advanceWidth = 8, byte_offset]
		byte_offset = args[4]
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X16), (i << 16) + {byte_offset}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X17), (i << 16) + {byte_offset}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X18), (i << 16) + 128 + 64));")
		# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X31), 8));")
		for j in range(8):
			if (byte_offset % 8) == 0:
				# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {j*8}, {args[0][byte_offset/8 + j]}u));")
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {j*8 + 128}, {args[0][int(byte_offset/8) + j]}u));")
			else:
				offset = (byte_offset % 8) * 8
				mask = 0
				for i in range(0,64-offset):
					mask = (mask << 1) | 1
				val = (((args[0][int(byte_offset/8)+ j] >> offset) & mask) | (args[0][int(byte_offset/8)+ j + 1] << (64 - offset))) & 0xFFFFFFFFFFFFFFFF
				# test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {j*8}, {val}u));")
				test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {j*8 + 128}, {val}u));")

	elif instruction == "movsbr":
		# movsbr Xd
		# Xd ← SB[SBP:SBP + CR.issue]
		# args = [val, rdMode = 1, issueWidth, advanceWidth = 8, byte_offset = 0, SBP_addr, final_val]
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X17), (i << 16)));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X16), {args[6]}));")
		for j in range(16):
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {j*8}, {args[0][j]}u));")
				

	elif inst_type == "movsbr_cycle":
		# movsbr Xd
		# Xd ← SB[SBP:SBP + CR.issue]
		# args = [val, rdMode = 1, issueWidth, advanceWidth = 8, byte_offset = 63, SBP_addr = 511, final_val]
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X17), (i << 16) + {args[4]}));")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testReg(i, (RegId::X16), {args[6]}));")
		for j in range(16):
			test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(acc0.testMem((i << 16) + {j*8}, {args[0][j]}u));")
				

	elif instruction == "ssprop":
		# ssprop $type $value
		# set next_active_state’s property ($type, $value)
		# args = [val, rdMode, issueWidth, advanceWidth = 8, byte_offset = 0, state_type, state_value]
		test_lines.append(str_tab + str_tab + f"word_t val=0;")
		test_lines.append(str_tab + str_tab + f"acc0.readScratchPad(8, (i<<16), (uint8_t*)&val);")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE((val & 0b1111) == {args[5]});")
		test_lines.append(str_tab + str_tab + f"EXPECT_TRUE(((val >> 16) & 0b111111111111) == {args[6]});")

		
	else:
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
	
