import sys
import os
import random
from pathlib import Path, PosixPath
import subprocess
import ctypes
import pdb

str_tab = "    "
min_int = {prec: -(1<<prec-1) for prec in [4,8,12,16,32,64]}
max_int = {prec: (1<<prec-1) - 1 for prec in [4,8,12,16,32,64]}
hex_rep = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
		   '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
bin_rep = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
		   '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
# Change path to your testing programs
test_path = Path('../tests/inst_unit_tests') # The c++ google test script
# prog_path = Path('../tests/') # The directory to hold the efa programs
prog_path = Path('efas/unit_tests')
top_exe_path = Path('fastsim_exe') # The top program to generate expected results

overflow_count = 0
underflow_count = 0


class CRC64:
	POLY64REV = 0xC96C5795D7870F42
	crc64_tab = []

	@classmethod
	def crc64_init_table(cls):
		if not cls.crc64_tab:
			for b in range(256):
				crc = ctypes.c_uint64(b).value
				for _ in range(8):
					if crc & 1:
						crc = (crc >> 1) ^ cls.POLY64REV
					else:
						crc >>= 1
				cls.crc64_tab.append(ctypes.c_uint64(crc).value)

	@staticmethod
	def crc64_update(crc, byte):
		tbl_idx = (crc ^ byte) & 0xff
		return (CRC64.crc64_tab[tbl_idx] ^ (crc >> 8)) & 0xFFFFFFFFFFFFFFFF

	@classmethod
	def compute(cls, input_integer):
		cls.crc64_init_table()
		crc = 0xFFFFFFFFFFFFFFFF
		if type(input_integer) is int:
			input_bytes = input_integer.to_bytes(8, 'little')
		elif type(input_integer) is list:
			input_bytes = b""
			for num in input_integer:
				input_bytes += num.to_bytes(8, 'little')
		for b in input_bytes:
			crc = cls.crc64_update(crc, b)
		return crc ^ 0xFFFFFFFFFFFFFFFF

def int_to_unsigned(num, precision = 64):
	if num >= 0:
		return num
	else:
		return int(int_to_bin(num, precision), 2)

def int_to_bin(num, precision = 64):
	if num >= 0:
		if num > max_int[precision]:
			return format(num, 'b')[-precision:]
		return format(num, 'b').zfill(precision)
	else:
		return format(num + (1<<precision), 'b')

def bin_to_int(bin_str, precision = 64):
	if bin_str[0] == '0':
		return int(bin_str, 2)
	else:
		return int(bin_str, 2) - (1<<precision)

def bin_to_hex(bin_str):
	hex_str = ''
	for i in range(len(bin_str)//4):
		hex_str += hex_rep[bin_str[i*4:i*4+4]]
	return hex_str

def hex_to_bin(hex_str):
	bin_str = ''
	for hex_byte in hex_str:
		bin_str += bin_rep[hex_byte]
	return bin_str

def lshift(num, nbits, precision = 64):
	s = int_to_bin(num)[nbits:]
	for _ in range(nbits):
		s += '0'
	return bin_to_int(s, precision)

def rshift(num, nbits, precision = 64):
	s = int_to_bin(num)
	if nbits != 0:
		s = s[:-nbits].zfill(precision)
	return bin_to_int(s, precision)

def float(args):
	return args[0]/args[1]

def rand_fp(precision):
	invalid = True
	while invalid:
		val = random.randint(0,(1<<precision)-1)
		match precision:
			case 64:
				invalid = (val >> 52) & 1023 == 1023
			case 32:
				invalid = (val >> 23) & 255 == 255
			case 16:
				invalid = (val >> 7) & 255 == 255
			case _:
				print("Precision not implemented yet, exit.")
				sys.exit()
	return val

def crc64_helper_hashsb64(val):
	poly = 0xC96C5795D7870F42
	crc = val
	for i in range(64):
		if crc & 1:
			crc = (crc >> 1) ^ poly
		else:
			crc = (crc >> 1)
	return crc

def sim_hash64(args):
	stbuff, base = args[:-1], args[-1]//8
	# print(stbuff, base)
	if args[-1]%8 == 0:
		val = int_to_unsigned(stbuff[base])
	else:
		val0, val1 = stbuff[base], stbuff[base+1]
		offset = args[-1]%8 * 2
		bin0, bin1 = int_to_bin(val0), int_to_bin(val1)
		hex0, hex1 = bin_to_hex(bin0)[::-1], bin_to_hex(bin1)[::-1]
		cat_hex = hex0[offset:] + hex1[:offset]
		cat_bin = hex_to_bin(cat_hex[::-1])
		val = int_to_unsigned(bin_to_int(cat_bin))
	return CRC64.compute(val)

# def int_to_bin(num, precision = 64):
# 	if num > 0:
# 		return format(num, 'b').zfill(precision)
# 	else:
# 		return format(num + (1<<precision), 'b')

def mov_imm2reg_64(prog_lines, num, reg):
	bin_reg = int_to_bin(num)
	# print(bin_reg)
	# print(bin_reg[:16],int(bin_reg[:16], 2))
	prog_lines.append(str_tab + f"tran0.writeAction(\"movir {reg} {int(bin_reg[:16], 2)}\")")
	for i in range(1,5):
		prog_lines.append(str_tab + f"tran0.writeAction(\"slorii {reg} {reg} 12 {int(bin_reg[16+12*(i-1):16+12*i],2)}\")")
	return

def generate_efa_unit_test(test_path: PosixPath, fpath: PosixPath, instruction: str, args: list):

	prog_lines = ["from EFA_v2 import *",
			f"def {fpath.stem}():",
			str_tab + "efa = EFA([])",
			str_tab + "efa.code_level = \"machine\"",
			str_tab + "state = State()",
			str_tab + "efa.add_initId(state.state_id)",
			str_tab + "efa.add_state(state)",
			str_tab + "event_map = {",
			str_tab + str_tab + "\"launch_events\": 0,",
			str_tab + "}",
			str_tab + "tran0 = state.writeTransition(\"eventCarry\", state, state, event_map['launch_events'])"]

	instruction_fname = '_'.join(instruction.split('.'))
	test_lines = [f"TEST_F({instruction_fname.capitalize()}Test, {fpath.stem}){{",
			str_tab + f"acc0.initSetup(0,\"testprogs/binaries/{fpath.stem}.bin\", 0);",
			str_tab + "uint8_t numop = 2;",
			str_tab + "eventword_t ev0(0);",
			str_tab + "ev0.setNumOperands(numop);",
			str_tab + "operands_t op0(numop);",
			str_tab + "word_t* data = new word_t[numop];",
			str_tab + "for(auto i = 0; i < numop; i++)",
			str_tab + str_tab + "data[i] = i+5;",

			str_tab + "op0.setData(data);",
			str_tab + "eventoperands_t eops(&ev0, &op0);",
			str_tab + "acc0.pushEventOperands(eops, 0);",
			str_tab + "acc0.pushEventOperands(eops, 1);",

			str_tab + "while(!acc0.isIdle())",
			str_tab + str_tab + "acc0.simulate(2);"]

	generate_efa(instruction, prog_lines, args)
	prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")
	prog_lines.append(str_tab + "return efa")

	with open(fpath, 'w') as writer:
		writer.writelines('\n'.join(prog_lines) + '\n')

	return test_lines

def generate_output(fname):
	p = subprocess.Popen([f"./{top_exe_path}", fname], stdout=subprocess.PIPE)
	out, _ = p.communicate()
	s = out.decode('ascii').split('\n')
	ind = -1
	for j in range(len(s)):
		if s[-1-j] == '[yield_terminate,]':
			ind = -2-j
			break
	output = s[ind].split(':')[-1].split(',')
	return output

def generate_random_efa(instruction: str, fpath: PosixPath, count: int):
	global overflow_count, underflow_count
	args_list, output_list = [], []
	instruction_fname = '_'.join(instruction.split('.'))
	for i in range(count):
		args = generate_random_args(instruction)
		args_list.append(args)

		test_lines = generate_efa_unit_test(test_path, fpath.joinpath(f'{instruction_fname}_{i}.py'), instruction, args)

		# output = generate_output(f'{instruction}_{i}')
		output = []
		match instruction:
			case "hashsb64":
				output=[sim_hash64(args[:-2] + [args[-2]>>3])+args[-1]]
			case "hashl64":
				output=[sim_hash64(args[:-1])+args[-1]]
			case "hash":
				out = int_to_unsigned(args[0]) + int_to_unsigned(args[1])
				out_bin = int_to_bin(out)
				out_dec = bin_to_int(out_bin)
				output=[CRC64.compute(int_to_unsigned(out_dec))]
			case "hashl":
				res = int_to_unsigned(args[-1])
				for arg in args[:-1]:
					uarg = int_to_unsigned(arg)
					tmp = int_to_unsigned(bin_to_int(int_to_bin(res + uarg)))
					res = CRC64.compute(tmp)
					# res += crc64_helper_hashsb64(int_to_unsigned(arg))
				# res = int_to_unsigned(bin_to_int(int_to_bin(res)))
				output = [res]
			case "cstr":
				if len(args) == 0:
					output = [256]
				else:
					output = [len(args)]

			case _:
				print("Instruction not implemented yet, exit.")
				sys.exit()

		output_list.append(output)

		generate_assertion(instruction, test_lines, output)
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
	print(args)
	prog_lines.append(f"# Input arguments: {args}")
	match instruction:
		
		case "hashsb64":
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X16 0\")")
			for i,arg in enumerate(args[:8]):
				mov_imm2reg_64(prog_lines, arg, 'X17')
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X17 0(X16) 1 8\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X16 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movlsb X16\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {args[-2]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X17 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X17 X5\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {args[-1]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"hashsb64 X16 X17\")")

		case "hashl64":
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X16 0\")")
			for i,arg in enumerate(args[:8]):
				mov_imm2reg_64(prog_lines, arg, 'X17')
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X17 0(X16) 1 8\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X18 {args[-2]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X7 X18 X5\")")
			mov_imm2reg_64(prog_lines, args[-1], 'X16')
			prog_lines.append(str_tab + f"tran0.writeAction(\"hashl64 X16 X17\")")
		case "hash":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			mov_imm2reg_64(prog_lines, args[1], 'X17')
			prog_lines.append(str_tab + f"tran0.writeAction(\"hash X16 X17\")")

		case "hashl":
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X16 0\")")
			for arg in args[:-1]:
				mov_imm2reg_64(prog_lines, arg, 'X17')
				prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X17 0(X16) 1 8\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X16 0\")")
			mov_imm2reg_64(prog_lines, args[-1], 'X17')
			prog_lines.append(str_tab + f"tran0.writeAction(\"hashl X16 X17 {len(args)-1}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X16 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"movrl X17 0(X16) 0 8\")")

		case "cstr":
			max_size = 256
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X16 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X17 {max_size}\")")
			for arg in args:
				prog_lines.append(str_tab + f"tran0.writeAction(\"movil1 X16 {arg}\")")
				prog_lines.append(str_tab + f"tran0.writeAction(\"movil1 X17 {arg}\")")
			if len(args) < 256:
				prog_lines.append(str_tab + f"tran0.writeAction(\"movil1 X16 0\")")
				prog_lines.append(str_tab + f"tran0.writeAction(\"movil1 X17 {(1<<8)-1}\")")

			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X16 0\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X7 X17 {max_size}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"cstr X16 X17 X18\")")



		# Add your instruction cases here

		case _:
			print("Instruction not implemented yet, exit.")
			sys.exit()

	return

# Add code to generate corresponding random arguments
def generate_random_args(instruction: str) -> list:
	args = []
	match instruction:
		case "hashsb64":
			args = [random.randint(min_int[64], max_int[64]) for _ in range(8)] + [random.randint(0,56)<<3, random.randint(0,max_int[16])]
		case "hashl64":
			args = [random.randint(min_int[64], max_int[64]) for _ in range(8)] + [random.randint(0,56), random.randint(0,max_int[64])]
		case "hash":
			args = [random.randint(min_int[64], max_int[64]) for _ in range(2)]
			# args = [-4972264472110413858, -5766241645424604240]
		case "hashl":
			count = random.randint(1,8)
			args = [random.randint(min_int[64], max_int[64]) for _ in range(count+1)]
		case "cstr":
			str_len = random.randint(0,256)
			args = [random.randint(0, (1<<8)-1) for _ in range(str_len)]

		case _:
			print("Instruction not implemented yet, exit.")
			sys.exit()

	return args

# Add google test code to assert the output
def generate_assertion(instruction: str, test_lines: list, output: list):
	args = []
	match instruction:
		case "hashsb64":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output[0]}LLU));")
		case "hashl64":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output[0]}LLU));")
		case "hash":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output[0]}LLU));")
		case "hashl":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testMem(0, {output[0]}LLU));")
		case "cstr":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X18, {output[0]}LLU));")

		case _:
			print("Instruction not implemented yet, exit.")
			sys.exit()

	test_lines.append("}")
	return




# A wrpper function to handle the unit test
def generate_random_unit_test(fpath: PosixPath, instruction: str, count: int=10):
	args_list, output_list = generate_random_efa(instruction, fpath, count)
	print(f'Instruction: {instruction}')
	print('args -> output')
	for args, out in zip(args_list, output_list):
		print(f'{args} -> {out}')


if __name__ == '__main__':

	instruction = sys.argv[1]
	instruction_fname = '_'.join(instruction.split('.'))
	test_path = test_path.joinpath(f"{instruction_fname}_test.cpp")
	prog_path = prog_path.joinpath(f"{instruction_fname}")
	if not prog_path.exists():
		os.mkdir(prog_path)
	count = 10 if len(sys.argv) <= 2 else int(sys.argv[2])
	if not test_path.exists():
		lines = ["#include <gtest/gtest.h>",
				"#include \"udlane.hh\"",
				"#include \"types.hh\"",
				"#include \"lanetypes.hh\"",
				"#include \"udaccelerator.hh\"",
				"#include <cmath>",
				"#include <cfenv>",
				"",
				"using namespace basim;",
				"",
				f"class {instruction_fname.capitalize()}Test : public ::testing::Test {{",
				" protected:",
				str_tab + "size_t num_threads = 2;",
				str_tab + "int num_lanes = 64;",
				str_tab + "UDAccelerator acc0 = UDAccelerator(num_lanes, 0, 0);",
				str_tab + "int buffsize1 = 1024;",
				str_tab + "int buffsize2 = 1024;",
				"};"]


		with open(test_path, 'w') as writer:
			writer.writelines('\n'.join(lines) + '\n')

	generate_random_unit_test(prog_path, instruction, count)
	print(f"Overflow: {overflow_count}")
	print(f"Underflow: {underflow_count}")
	# TODO: Add generating random unit test function here
	# For example to generate unit tests for add:
	# generate_random_add_unit_test(prog_path, 'add')

































