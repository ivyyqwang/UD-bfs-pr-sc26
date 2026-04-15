import sys
import os
import random
from pathlib import Path, PosixPath
import subprocess

str_tab = "    "
max_int_64 = (1<<63) - 1
min_int_64 = -(1<<63)
max_int_32 = (1<<31) - 1
min_int_32 = -(1<<31)
max_int_16 = (1<<15) - 1
min_int_16 = -(1<<15)
min_int = {prec: -(1<<prec-1) for prec in [4,12,16,32,64]}
max_int = {prec: (1<<prec-1) - 1 for prec in [4,12,16,32,64]}
# Change path to your testing programs
test_path = Path('../tests/inst_unit_tests') # The c++ google test script
# prog_path = Path('../tests/') # The directory to hold the efa programs
prog_path = Path.cwd()
top_exe_path = Path('fastsim_exe') # The top program to generate expected results

def int_to_unsigned(num):
	if num >= 0:
		return num
	else:
		return int(int_to_bin(num), 2)

def int_to_bin(num, precision = 64):
	if num >= 0:
		if num > max_int[precision]:
			return '0' + format(num, 'b')[-(precision-1):]
		return format(num, 'b').zfill(precision)
	else:
		return format(num + (1<<precision), 'b')

def bin_to_int(bin_str, precision = 64):
	if bin_str[0] == '0':
		return int(bin_str, 2)
	else:
		return int(bin_str, 2) - (1<<precision)

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

	test_lines = [f"TEST_F({instruction.capitalize()}Test, {fpath.stem}){{",
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


##################################################
# To add unit tests with random input, implement following three functions
# Add the instruction in the match cases
# Naming as
# generage_efa
# generate_random_args
# generate_assertion
##################################################

def generate_edge_case_efa(instruction: str, fpath: PosixPath, start_count: int):
	args_list, output_list = generate_edge_case_args(instruction), []
	count = start_count
	for args in args_list:
		test_lines = generate_efa_unit_test(test_path, fpath.joinpath(f'{instruction}_{count}.py'), instruction, args)
		count += 1
		match instruction:
			case "addi":
				out = int_to_unsigned(args[0]) + int_to_unsigned(args[1])
				out_bin = int_to_bin(out)
				out_dec = bin_to_int(out_bin)
				
			case "subi":
				out = int_to_unsigned(args[0]) - int_to_unsigned(args[1])
				print(args[0], args[1])
				print(int_to_unsigned(args[0]), int_to_unsigned(args[1]))
				out_bin = int_to_bin(out)
				print(out_bin)
				out_dec = bin_to_int(out_bin)
				print(out_dec)

			case "muli":
				out = int_to_unsigned(args[0]) * int_to_unsigned(args[1])
				out_bin = int_to_bin(out)
				out_dec = bin_to_int(out_bin)

			case "divi":
				if args[1] == 0:
					out_dec = 0
				else:
					out_dec = args[0] // args[1]
					# out = int_to_unsigned(args[0]) // int_to_unsigned(args[1])
					# out_bin = int_to_bin(out)
					# out_dec = bin_to_int(out_bin)

			case "modi":
				if args[1] == 0:
					out_dec = 0
				else:
					out_dec = args[0] % args[1]
					# out = int_to_unsigned(args[0]) % int_to_unsigned(args[1])
					# out_bin = int_to_bin(out)
					# out_dec = bin_to_int(out_bin)
			case _:
				print("Instruction not implemented yet, exit.")
				sys.exit()

		output_list.append(out_dec)
		generate_assertion(instruction, test_lines, out_dec)
		with open(test_path, 'a') as test_writer:
			test_writer.writelines('\n'.join(test_lines) + '\n')

	return args_list, output_list

# Add the efa program in the corresponding case
def generate_efa(instruction: str, prog_lines: list, args: list):
	print(args)
	prog_lines.append(f"# Input arguments: {args}")
	match instruction:
		case "addi":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X17 {args[1]}\")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
		case "subi":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			prog_lines.append(str_tab + f"tran0.writeAction(\"subi X16 X17 {args[1]}\")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
		case "muli":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			prog_lines.append(str_tab + f"tran0.writeAction(\"muli X16 X17 {args[1]}\")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
		case "divi":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			prog_lines.append(str_tab + f"tran0.writeAction(\"divi X16 X17 {args[1]}\")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
		case "modi":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			prog_lines.append(str_tab + f"tran0.writeAction(\"modi X16 X17 {args[1]}\")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
		case "add":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			mov_imm2reg_64(prog_lines, args[1], 'X17')
			prog_lines.append(str_tab + f"tran0.writeAction(\"add X16 X17 X17 \")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d' {'X17'}\")")
		case "sub":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			mov_imm2reg_64(prog_lines, args[1], 'X17')
			prog_lines.append(str_tab + f"tran0.writeAction(\"sub X16 X17 X17 \")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d' {'X17'}\")")
		case "mul":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			mov_imm2reg_64(prog_lines, args[1], 'X17')
			prog_lines.append(str_tab + f"tran0.writeAction(\"mul X16 X17 X17 \")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d' {'X17'}\")")
		case "div":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			mov_imm2reg_64(prog_lines, args[1], 'X17')
			prog_lines.append(str_tab + f"tran0.writeAction(\"div X16 X17 X17 \")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d' {'X17'}\")")
		case "mod":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			mov_imm2reg_64(prog_lines, args[1], 'X17')
			prog_lines.append(str_tab + f"tran0.writeAction(\"mod X16 X17 X17 \")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d' {'X17'}\")")
		case "sladdii":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			prog_lines.append(str_tab + f"tran0.writeAction(\"sladdii X16 X17 {args[1]} {args[2]}, {args[3]}\")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d' {'X17'}\")")
		case "slsubii":
			mov_imm2reg_64(prog_lines, args[0], 'X16')
			prog_lines.append(str_tab + f"tran0.writeAction(\"slsubii X16 X17 {args[1]} {args[2]}, {args[3]}\")")
			# prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d' {'X17'}\")")
		case "sraddii":
			pass
		case "srsubii":
			pass
		case "fadd.64":
			pass
		case "fsub.64":
			pass
		case "fmul.64":
			pass
		case "fdiv.64":
			pass
		case "fsqrt.64":
			pass
		case "fmadd.32":
			pass
		case "fadd.32":
			pass
		case "fsub.32":
			pass
		case "fmul.32":
			pass
		case "fdiv.32":
			pass
		case "fsqrt.32":
			pass
		case "fmadd.b16":
			pass
		case "fadd.b16":
			pass
		case "fsub.b16":
			pass
		case "fmul.b16":
			pass
		case "fdiv.b16":
			pass
		case "fsqrt.b16":
			pass
		case "vmadd.32":
			pass
		case "vadd.32":
			pass
		case "vsub.32":
			pass
		case "vmul.32":
			pass
		case "vdiv.32":
			pass
		case "vsqrt.32":
			pass
		case "vmadd.b16":
			pass
		case "vadd.b16":
			pass
		case "vsub.b16":
			pass
		case "vmul.b16":
			pass
		case "vdiv.b16":
			pass
		case "vsqrt.b16":
			pass
		case "vmadd.i32":
			pass
		case "vadd.i32":
			pass
		case "vsub.i32":
			pass
		case "vmul.i32":
			pass
		case "vdiv.i32":
			pass
		case "vsqrt.i32":
			pass
		case "vgt.32":
			pass
		case "vgt.b16":
			pass
		case "vgt.i32":
			pass
		case "fcnvt_i2f.64":
			pass
		case "fcnvt_f2i.64":
			pass
		case "fcnvt_i2f.32":
			pass
		case "fcnvt_f2i.32":
			pass

		# Add your instruction cases here

		case _:
			print("Instruction not implemented yet, exit.")
			sys.exit()

	return

# Add code to generate corresponding random arguments
def generate_edge_case_args(instruction: str) -> list:
	args = []
	match instruction:
		case "addi":
			args = [[min_int[64], random.randint(min_int[16], -1)],
					[max_int[64], random.randint(1, max_int[16])]]
		case "subi":
			args = [[min_int[64], random.randint(1, max_int[16])],
					[max_int[64], random.randint(min_int[16], -1)]]
		case "muli":
			args = [[random.randint(min_int[64], min_int[64]/3), 3],
					[random.randint(max_int[64]/3, max_int[64]), -3],
					[random.randint(min_int[64], min_int[64]/3), -3],
					[random.randint(max_int[64]/3, max_int[64]), 3],
					[random.randint(min_int[64], max_int[64]), 0],
					[0, random.randint(min_int[16], max_int[16])]]
		case "divi":
			args = [[random.randint(min_int[64], max_int[64]), 0],
					[0, random.randint(min_int[16], max_int[16])]]
		case "modi":
			args = [[random.randint(min_int[64], max_int[64]), 0],
					[0, random.randint(min_int[16], max_int[16])]]
		case "add":
			args = [[min_int[64], random.randint(min_int[64], -1)],
					[max_int[64], random.randint(1, max_int[64])]]
		case "sub":
			args = [[min_int[64], random.randint(1, max_int[64])],
					[max_int[64], random.randint(min_int[64], -1)]]
		case "mul":
			args = [[random.randint(min_int[64], min_int[64]/3), 3],
					[random.randint(max_int[64]/3, max_int[64]), -3],
					[random.randint(min_int[64], min_int[64]/3), -3],
					[random.randint(max_int[64]/3, max_int[64]), 3],
					[random.randint(min_int[64], max_int[64]), 0],
					[0, random.randint(min_int[64], max_int[64])]]
		case "div":
			args = [[random.randint(min_int[64], max_int[64]), 0],
					[0, random.randint(min_int[64], max_int[64])]]
		case "mod":
			args = [[random.randint(min_int[64], max_int[64]), 0],
					[0, random.randint(min_int[64], max_int[64])]]
		case "sladdii":
			args = [[min_int[64], 4, random.randint(min_int[16], -32)],
					[max_int[64], 4, random.randint(32, max_int[16])]]
		case "slsubii":
			args = [[min_int[64], 4, random.randint(32, max_int[16])],
					[max_int[64], 4, random.randint(min_int[16], -32)]]
		case "sraddii":
			args = []
		case "srsubii":
			args = []
		case "fadd.64":
			pass
		case "fsub.64":
			pass
		case "fmul.64":
			pass
		case "fdiv.64":
			pass
		case "fsqrt.64":
			pass
		case "fmadd.32":
			pass
		case "fadd.32":
			pass
		case "fsub.32":
			pass
		case "fmul.32":
			pass
		case "fdiv.32":
			pass
		case "fsqrt.32":
			pass
		case "fmadd.b16":
			pass
		case "fadd.b16":
			pass
		case "fsub.b16":
			pass
		case "fmul.b16":
			pass
		case "fdiv.b16":
			pass
		case "fsqrt.b16":
			pass
		case "vmadd.32":
			pass
		case "vadd.32":
			pass
		case "vsub.32":
			pass
		case "vmul.32":
			pass
		case "vdiv.32":
			pass
		case "vsqrt.32":
			pass
		case "vmadd.b16":
			pass
		case "vadd.b16":
			pass
		case "vsub.b16":
			pass
		case "vmul.b16":
			pass
		case "vdiv.b16":
			pass
		case "vsqrt.b16":
			pass
		case "vmadd.i32":
			pass
		case "vadd.i32":
			pass
		case "vsub.i32":
			pass
		case "vmul.i32":
			pass
		case "vdiv.i32":
			pass
		case "vsqrt.i32":
			pass
		case "vgt.32":
			pass
		case "vgt.b16":
			pass
		case "vgt.i32":
			pass
		case "fcnvt_i2f.64":
			pass
		case "fcnvt_f2i.64":
			pass
		case "fcnvt_i2f.32":
			pass
		case "fcnvt_f2i.32":
			pass

		# Add your instruction cases here

		case _:
			print("Instruction not implemented yet, exit.")
			sys.exit()

	return args

# Add google test code to assert the output
def generate_assertion(instruction: str, test_lines: list, output: list):
	args = []
	match instruction:
		case "addi":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "subi":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "muli":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "divi":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "modi":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "add":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "sub":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "mul":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "div":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "mod":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "sladdii":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "slsubii":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "sraddii":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "srsubii":
			test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testReg(0, RegId::X17, {output}));")
		case "fadd.64":
			pass
		case "fsub.64":
			pass
		case "fmul.64":
			pass
		case "fdiv.64":
			pass
		case "fsqrt.64":
			pass
		case "fmadd.32":
			pass
		case "fadd.32":
			pass
		case "fsub.32":
			pass
		case "fmul.32":
			pass
		case "fdiv.32":
			pass
		case "fsqrt.32":
			pass
		case "fmadd.b16":
			pass
		case "fadd.b16":
			pass
		case "fsub.b16":
			pass
		case "fmul.b16":
			pass
		case "fdiv.b16":
			pass
		case "fsqrt.b16":
			pass
		case "vmadd.32":
			pass
		case "vadd.32":
			pass
		case "vsub.32":
			pass
		case "vmul.32":
			pass
		case "vdiv.32":
			pass
		case "vsqrt.32":
			pass
		case "vmadd.b16":
			pass
		case "vadd.b16":
			pass
		case "vsub.b16":
			pass
		case "vmul.b16":
			pass
		case "vdiv.b16":
			pass
		case "vsqrt.b16":
			pass
		case "vmadd.i32":
			pass
		case "vadd.i32":
			pass
		case "vsub.i32":
			pass
		case "vmul.i32":
			pass
		case "vdiv.i32":
			pass
		case "vsqrt.i32":
			pass
		case "vgt.32":
			pass
		case "vgt.b16":
			pass
		case "vgt.i32":
			pass
		case "fcnvt_i2f.64":
			pass
		case "fcnvt_f2i.64":
			pass
		case "fcnvt_i2f.32":
			pass
		case "fcnvt_f2i.32":
			pass

		# Add your instruction cases here

		case _:
			print("Instruction not implemented yet, exit.")
			sys.exit()

	test_lines.append("}")
	return


# A wrpper function to handle the unit test
def generate_edge_case_unit_test(fpath: PosixPath, instruction: str, start_count: str):
	args_list, output_list = generate_edge_case_efa(instruction, fpath, start_count)
	print(f'Instruction: {instruction}')
	print('args -> output')
	for args, out in zip(args_list, output_list):
		print(f'{args} -> {out}')


if __name__ == '__main__':

	instruction = sys.argv[1]
	start_count = int(sys.argv[2])
	test_path = test_path.joinpath(f"{instruction}_test.cpp")
	generate_edge_case_unit_test(prog_path, instruction, start_count)









