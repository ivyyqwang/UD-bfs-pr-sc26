import os
import sys
import random
from pathlib import Path, PosixPath
import subprocess
import argparse

str_tab = "    "
max_int_64 = (1 <<(64-1))-1
min_int_64 = -(1<<(64-1))
max_int_32 = (1 <<(32-1))-1
min_int_32 = -(1<<(32-1))
max_int_21 = (1 <<(21-1))-1
min_int_21 = -(1<<(21-1))
max_uint_21 = (1<<21)-1
min_uint_21 = 0
max_int_16 = (1 <<(16-1))-1
min_int_16 = -(1<<(16-1))
max_uint_16 = (1<<16)-1
min_uint_16 = 0
max_int_5 = (1 <<(5-1))-1
min_int_5 = -(1<<(5-1))
max_uint_5 = (1<<5)-1
min_uint_5 = 0

parser = argparse.ArgumentParser(description="input generated instruction and the number")
parser.add_argument("inst_type", type=str, help="the instruction to generated")
parser.add_argument("inst_num", type=int, help="the number of the instructions to generated")
args = parser.parse_args()

inst_type = args.inst_type
inst_num = args.inst_num

# Change path to your testing programs
test_path = Path(f'../tests/inst_unit_tests/{inst_type}_test.cpp').absolute() # The c++ google test script
prog_path = Path(f'./efas/unit_tests/{inst_type}').absolute() # The directory to hold the efa programs
top_exe_path = Path('fastsim_exe').absolute() # The top program to generate expected results
bin_path = Path("./binaries").absolute()

def generate_efa_unit_test(test_path: PosixPath, fpath: PosixPath, instruction: str, args: list, iter: int):
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

	test_lines = [f"TEST_F({instruction.upper()}, random_{iter}){{",
			str_tab + f"acc0.initSetup(0,\"testprogs/binaries/{fpath.stem}.bin\", 0);",
			str_tab + "uint8_t numop = 2;",
			str_tab + "eventword_t ev0(0);",
			str_tab + "ev0.setNumOperands(numop);",
			str_tab + "operands_t op0(numop);",
			str_tab + "word_t data[] = {8,0};",
			str_tab + "op0.setData(data);",
			str_tab + "eventoperands_t eops(&ev0, &op0);",
			str_tab + "acc0.pushEventOperands(eops, 0);",

			str_tab + "while(!acc0.isIdle())",
			str_tab + str_tab + "acc0.simulate(2);"]

	generate_efa(instruction, prog_lines, args)
	prog_lines.append(str_tab + "tran0.writeAction(\"yieldt\")")
	prog_lines.append(str_tab + "return efa")

	os.makedirs(fpath.parent,exist_ok=True)
	with open(fpath, 'w') as writer:
		writer.writelines('\n'.join(prog_lines) + '\n')

	return test_lines

def generate_output(fname):
	cwd = os.getcwd()
	os.chdir(prog_path)
	p = subprocess.Popen([top_exe_path, fname], stdout=subprocess.PIPE)
	out, _ = p.communicate()
	os.chdir(cwd)
	s = out.decode('ascii').split('\n')
	ind = -1
	for j in range(len(s)):
		if s[-1-j] == '[yieldt,]':
			ind = -2-j
			break
	output = s[ind].split(':')[-1].split(',')
	return output

def generate_bin(efa_fname):
	os.chdir('../assembler/')
	os.system(f"python3 ../assembler/efa2bin.py --efa {prog_path}/{efa_fname} --outpath {bin_path} --debug-messages")
	os.chdir("../testprogs/")
	
def generate_random_efa(instruction: str, fpath: PosixPath, count: int):
	args_list, output_list = [], []
	for i in range(count):
		args = generate_random_args(instruction)
		args_list.append(args)

		test_lines = generate_efa_unit_test(test_path, fpath.joinpath(f'{instruction}_{i}.py'), instruction, args, i)

		output = generate_output(f'{instruction}_{i}')
		output_list.append(output)
		generate_bin(f'{instruction}_{i}.py')
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
	match instruction:
		case "addi":
			prog_lines.append(str_tab + f"tran0.writeAction(\"movir X16 {args[0]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(\"addi X16 X17 {args[1]}\")")
			prog_lines.append(str_tab + f"tran0.writeAction(f\"print '%d,%d' {'X16'} {'X17'}\")")
		case "subi":
			pass
		case "muli":
			pass
		case "divi":
			pass
		case "modi":
			pass
		case "add":
			pass
		case "sub":
			pass
		case "mul":
			pass
		case "div":
			pass
		case "mod":
			pass
		case "saddi":
			pass
		case "ssubi":
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
		case 'beq' | 'bequ' | 'bne' | 'bneu' | 'bgt' | 'bgtu' | 'ble' | 'bleu':
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X16 {args[0]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X19 {args[1]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X17 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X18 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'{instruction} X16 X19 true\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'jmp test_false\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'true: movir X17 1\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'test_false: {instruction} X16 X19 false\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'jmp save\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'false: movir X18 1\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'save: addi X7 X20 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X17 0(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X18 8(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'print: print \\\'%d,%d\\\' X17 X18\')')
			pass
		case 'beqi' | 'beqiu' | 'bnei' | 'bneiu' | 'bgti' | 'bgei' | 'bgtiu' | 'blti' | 'bltiu' | 'blei' | 'bleiu':
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X16 {args[0]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X17 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X18 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'{instruction} X16 {args[1]} true\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'jmp test_false\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'true: movir X17 1\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'test_false: {instruction} X16 {args[2]} false\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'jmp save\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'false: movir X18 1\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'save: addi X7 X20 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X17 0(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X18 8(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'print: print \\\'%d,%d\\\' X17 X18\')')
			pass
		case 'jmp':
			prog_lines.append(str_tab+f'tran0.writeAction(\'jmp forward\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'backward: movir X17 1\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'jmp pass\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'forward: jmp backward\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X17 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'pass: addi X7 X20 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X17 0(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X17 8(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'print: print \\\'%d,%d\\\' X17 X17\')')
		case 'ceqi' | 'cgti' | 'clti':
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X16 {args[0]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'{instruction} X16 X17 {args[1]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'{instruction} X16 X18 {args[2]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'addi X7 X20 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X17 0(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X18 8(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'print: print \\\'%d,%d\\\' X17 X18\')')
			pass
		case 'ceq' | 'cgt' | 'clt':
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X16 {args[0]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X19 {args[1]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movir X20 {args[2]}\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'{instruction} X16 X19 X17\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'{instruction} X16 X20 X18\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'addi X7 X20 0\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X17 0(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'movrl X18 8(X20) 0 8\')')
			prog_lines.append(str_tab+f'tran0.writeAction(\'print: print \\\'%d,%d\\\' X17 X18\')')
			pass

		# Add your instruction cases here

		case _:
			print(instruction)
			print("Instruction not implemented yet, exit.")
			sys.exit()

	return

# Add code to generate corresponding random arguments
def generate_random_args(instruction: str) -> list:
	args = []
	match instruction:
		case "addi":
			args = [random.randint(min_int_64, max_int_64), random.randint(min_int_64, max_int_64)]
		case "subi":
			pass
		case "muli":
			pass
		case "divi":
			pass
		case "modi":
			pass
		case "add":
			pass
		case "sub":
			pass
		case "mul":
			pass
		case "div":
			pass
		case "mod":
			pass
		case "saddi":
			pass
		case "ssubi":
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
		case 'beq':
			val1 = random.randint(min_int_21, max_int_21)
			val2 = val1
			temp = random.randint(min_int_21, max_int_21)
			val3 = random.randint(min_int_21, max_int_21) if temp == val1 else temp
			args = [val1, val2, val3]
			pass
		case 'beqi':
			val1 = random.randint(min_int_5, max_int_5)
			val2 = val1
			temp = random.randint(min_int_5, max_int_5)
			val3 = random.randint(min_int_5, max_int_5) if temp == val1 else temp
			args = [val1, val2, val3]
			pass
		case 'bequ':
			val1 = random.randint(min_uint_21, max_uint_21)
			val2 = val1
			temp = random.randint(min_uint_21, max_uint_21)
			val3 = random.randint(min_uint_21, max_uint_21) if temp == val1 else temp
			args = [val1, val2, val3]
			pass
		case 'beqiu':
			val1 = random.randint(min_uint_5, max_uint_5)
			val2 = val1
			temp = random.randint(min_uint_5, max_uint_5)
			val3 = random.randint(min_uint_5, max_uint_5) if temp == val1 else temp
			args = [val1, val2, val3]
			pass
		case 'bne':
			val1 = random.randint(min_int_21, max_int_21)
			val2 = val1
			temp = random.randint(min_int_21, max_int_21)
			val3 = random.randint(min_int_21, max_int_21) if temp != val1 else temp
			args = [val1, val2, val3]
			pass
		case 'bnei':
			val1 = random.randint(min_int_5, max_int_5)
			val2 = val1
			temp = random.randint(min_int_5, max_int_5)
			val3 =  random.randint(min_int_5, max_int_5) if temp != val1 else temp
			args = [val1, val2, val3]
		case 'bneu':
			val1 = random.randint(min_uint_21, max_uint_21)
			val2 = val1
			temp = random.randint(min_uint_21, max_uint_21)
			val3 =  random.randint(min_uint_21, max_uint_21) if temp != val1 else temp
			args = [val1, val2, val3]
			pass
		case 'bneiu':
			val1 = random.randint(min_uint_5, max_uint_5)
			val2 = val1
			temp = random.randint(min_uint_5, max_uint_5)
			val3 =  random.randint(min_uint_5, max_uint_5) if temp != val1 else temp
			args = [val1, val2, val3]
			pass
		case 'bgt':
			val1 = random.randint(min_int_21, max_int_21)
			val2 = random.randint(val1+1, max_int_21)
			val3 = random.randint(min_int_21, val1)
			args = [val1, val2, val3]
			pass
		case 'bgti':
			val1 = random.randint(min_int_5, max_int_5)
			val2 = random.randint(val1+1, max_int_5)
			val3 = random.randint(min_int_5, val1)
			args = [val1, val2, val3]
			pass
		case 'bgtu':
			val1 = random.randint(min_uint_5, max_uint_5)
			val2 = random.randint(val1+1, max_uint_5)
			val3 = random.randint(min_uint_5, val1)
			args = [val1, val2, val3]
			pass
		case 'bgtiu':
			val1 = random.randint(min_uint_5, max_uint_5)
			val2 = random.randint(val1+1, max_uint_5)
			val3 = random.randint(min_uint_5, val1)
			args = [val1, val2, val3]
			pass
		case 'bgei':
			val1 = random.randint(min_int_5, max_int_5)
			val2 = random.randint(val1, max_int_5)
			val3 = random.randint(min_int_5, val1-1)
			args = [val1, val2, val3]
			pass
		case 'bgeiu':
			val1 = random.randint(min_uint_5, max_uint_5)
			val2 = random.randint(val1, max_uint_5)
			val3 = random.randint(min_uint_5, val1-1)
			args = [val1, val2, val3]
			pass
		case 'blti':
			val1 = random.randint(min_int_5, max_int_5)
			val2 = random.randint(min_int_5, val1-1)
			val3 = random.randint(val1, max_int_5)
			args = [val1, val2, val3]
			pass
		case 'bltiu':
			val1 = random.randint(min_uint_5, max_uint_5)
			val2 = random.randint(min_uint_5, val1-1)
			val3 = random.randint(val1, max_uint_5)
			args = [val1, val2, val3]
			pass
		case 'ble':
			val1 = random.randint(min_int_21, max_int_21)
			val2 = random.randint(min_int_21, val1)
			val3 = random.randint(val1+1, max_int_21)
			args = [val1, val2, val3]
			pass
		case 'blei':
			val1 = random.randint(min_int_5, max_int_5)
			val2 = random.randint(min_int_5, val1)
			val3 = random.randint(val1+1, max_int_5)
			args = [val1, val2, val3]
			pass
		case 'bleu':
			val1 = random.randint(min_uint_21, max_uint_21)
			val2 = random.randint(min_uint_21, val1)
			val3 = random.randint(val1+1, max_uint_21)
			args = [val1, val2, val3]
			pass
		case 'bleiu':
			val1 = random.randint(min_uint_5, max_uint_5)
			val2 = random.randint(min_uint_5, val1)
			val3 = random.randint(val1+1, max_uint_5)
			args = [val1, val2, val3]
			pass
		case 'jmp':
			args = []
			pass
		case 'ceqi':
			val1 = random.randint(min_int_16, max_int_16)
			val2 = val1
			val3 = random.randint(min_int_16, max_int_16)
			args = [val1, val2, val3]
			pass
		case 'cgti':
			val1 = random.randint(min_int_16, max_int_16)
			val2 = random.randint(min_int_16,val1-1)
			val3 = random.randint(val1+1,max_int_16)
			args = [val1, val2, val3]
			pass
		case 'clti':
			val1 = random.randint(min_int_16, max_int_16)
			val2 = random.randint(val1+1,max_int_16)
			val3 = random.randint(min_int_16,val1-1)
			args = [val1, val2, val3]
			pass
		case 'ceq':
			val1 = random.randint(min_int_21, max_int_21)
			val2 = val1
			val3 = random.randint(min_int_21, max_int_21)
			args = [val1, val2, val3]
			pass
		case 'cgt':
			val1 = random.randint(min_int_21, max_int_21)
			val2 = random.randint(min_int_21,val1-1)
			val3 = random.randint(val1+1,max_int_21)
			args = [val1, val2, val3]
			pass
		case 'clt':
			val1 = random.randint(min_int_21, max_int_21)
			val2 = random.randint(val1+1,max_int_21)
			val3 = random.randint(min_int_21,val1-1)
			args = [val1, val2, val3]
			pass

		# Add your instruction cases here

		case _:
			print(instruction)
			print("Instruction not implemented yet, exit.")
			sys.exit()

	return args

# Add google test code to assert the output
def generate_assertion(instruction: str, test_lines: list, output: list):
	i = 0
	for test_val in output:
		test_lines.append(str_tab + f"EXPECT_TRUE(acc0.testMem({i*8}, {int(test_val)}));")
		i += 1
	test_lines.append("}")
	return



def generate_edge_unit_test(fpath: PosixPath, instruction:str ):
	test_lines = [f"TEST_F({instruction.upper()}, edge){{",
		str_tab + f"acc0.initSetup(0,\"testprogs/binaries/{fpath.stem}.bin\", 0);",
		str_tab + "uint8_t numop = 2;",
		str_tab + "eventword_t ev0(0);",
		str_tab + "ev0.setNumOperands(numop);",
		str_tab + "operands_t op0(numop);",
		str_tab + "word_t data[] = {8,0};",
		str_tab + "op0.setData(data);",
		str_tab + "eventoperands_t eops(&ev0, &op0);",
		str_tab + "acc0.pushEventOperands(eops, 0);",

		str_tab + "while(!acc0.isIdle())",
		str_tab + str_tab + "acc0.simulate(2);"]

	generate_bin(f'{instruction}.py')
	generate_assertion(instruction, test_lines, ['1'])
	with open(test_path, 'a') as test_writer:
		test_writer.writelines('\n'.join(test_lines) + '\n')

# A wrpper function to handle the unit test
def generate_random_unit_test(fpath: PosixPath, instruction: str, count: int=10):
	args_list, output_list = generate_random_efa(instruction, fpath, count)
	for args, out in zip(args_list, output_list):
		print(f'{args} -> {out}')


if __name__ == '__main__':
	lines = ["#include <gtest/gtest.h>",
			"#include \"udlane.hh\"",
			"#include \"types.hh\"",
			"#include \"udaccelerator.hh\"",
			"",
			"using namespace basim;",
			"",
			f'class {inst_type.upper()} : public ::testing::Test {{',
			" protected:",
			str_tab + "UDAccelerator acc0 = UDAccelerator(1,0,1);",
			"};"]
	with open(test_path, 'w') as writer:
		writer.writelines('\n'.join(lines) + '\n')

	generate_edge_unit_test(prog_path, inst_type)
	generate_random_unit_test(prog_path, inst_type, inst_num)
	# TODO: Add generating random unit test function here
	# For example to generate unit tests for add:
	# generate_random_add_unit_test(prog_path, 'add')







