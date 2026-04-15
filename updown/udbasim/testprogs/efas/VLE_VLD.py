from EFA_v2 import *

VLE_procedure_name = "VLE_procedure"
VLD_procedure_name = "VLD_procedure"
OUTPUT_PTR_REG = "X31"
INIT_OUTPUT_PTR_REG = "X30"
TEMP_REG0 = "X29"
TEMP_REG1 = "X28"
VLE_ISSUE_WIDTH = 8
VLE_ADV_WIDTH = 8
VLE_STORE_WIDTH = 1
VLD_ISSUE_WIDTH=1
VLD_ADV_WIDTH=1
VLD_STORE_WIDTH=8

def VLE_VLD():
	efa = EFA([])
	efa.code_level = "machine"

	state = State()  #Initial State
	efa.add_initId(state.state_id)
	efa.add_state(state)

	state0 = State()
	state0.alphabet = [0]
	efa.add_state(state0)

	state1 = State()
	state1.alphabet = [0]
	efa.add_state(state1)

	state2 = State()
	state2.alphabet = [0,1]
	efa.add_state(state2)

	state3 = State()
	state3.alphabet = [0]
	efa.add_state(state3)

	state4 = State()
	state4.alphabet = [0]
	efa.add_state(state4)

	state5 = State()
	state5.alphabet = [0]
	efa.add_state(state5)

	state6 = State()
	state6.alphabet = [0,1]
	efa.add_state(state6)

	state7 = State()
	state7.alphabet = [0]
	efa.add_state(state7)

	tran = state.writeTransition("commonCarry", state, state0, VLE_procedure_name)
	#Find input LM offset (aligned DRAM memory copy)
	tran.writeAction(f"sri X11 X16 6")                                  # X11 (Input stream non aligned DRAM address)
	tran.writeAction(f"sli X16 X16 6")                                  # X16 (64-byte aligned DRAM address)
	tran.writeAction(f"sub X11 X16 X16")                                # X16 (input stream offset from the beginning of IN_LM_OFFSET)
	#Set SBP
	tran.writeAction(f"add X8 X16 X16")                                 # X8 (IN_LM_OFFSET), X16 (input stream offset, local to lane's LM)
	tran.writeAction(f"add X16 X7 X5")                                  # X5 (SBP in global LM address) = X16 + X7
	tran.writeAction(f"add X9 X16 X30")  	                            # X30 (MaxSBP) = X9(InputSize) + X16(SBP)
	#clear rdMode, CR_Issue, CR_Advance, MaxSBP in SBCR
	tran.writeAction(f"sri X4 X29 41")  	                            # rshift X29 clear SBCR(X4) left hand side
	tran.writeAction(f"sli X29 X29 41")  	                            # lshift cleared SBCR back
	#Note: Set rdMode here if working in SB mode (i.e., reading input from stream buffer)
	#tran.writeAction(f)
	#Set CR_Issue
	tran.writeAction(f"movir X28 {VLE_ISSUE_WIDTH}")
	tran.writeAction("sli X28 X27 36")  	                            # X27: CR_Issue
	tran.writeAction(f"or X29 X27 X29")  	                            # Update CR_Issue
	#Set CR_Advance
	tran.writeAction(f"movir X28 {VLE_ADV_WIDTH}")
	tran.writeAction(f"sli X28 X27 32")  	                            # X27: CR_Advance
	tran.writeAction(f"or X29 X27 X29")  	                            # Update CR_Advance
	#Set MaxSBP
	tran.writeAction(f"or X29 X30 X4")  	                            # Write MaxSBP(in X30) to SBCR(X4)
	#Set output LM ptr
	tran.writeAction(f"add X10 X7 {OUTPUT_PTR_REG}")  	                # {OUTPUT_PTR_REG} (output stream offset, in global LM address) = X10 (output offset,local to lane's LM) + X7 (LM Base) 
	#Save original input pointer for output length calc.
	tran.writeAction(f"addi {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} 0") # {INIT_OUTPUT_PTR_REG}: stores original output pointer (for output size calculation at the end)
	tran.writeAction("lastact")  	

	tran = state0.writeTransition("epsilonCarry_with_action",state0, state1, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_2 0 {VLE_ISSUE_WIDTH}")
	tran.writeAction(f"lshift UDPR_2 UDPR_3 1")
	tran.writeAction(f"sari UDPR_2 UDPR_4 63")
	tran.writeAction(f"xor UDPR_4 UDPR_3 UDPR_2")
	tran.writeAction("lastact")   

	tran = state1.writeTransition("flagCarry_with_action",state1, state2, 0)
	tran.writeAction(f"movir UDPR_1 -128")
	tran.writeAction(f"and UDPR_1 UDPR_2 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = state2.writeTransition("epsilonCarry_with_action",state2, state1, 0)
	tran.writeAction(f"andi UDPR_2 UDPR_1 127")
	tran.writeAction(f"ori UDPR_1 UDPR_1 128")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {VLE_STORE_WIDTH}")
	tran.writeAction(f"rshift UDPR_2 UDPR_2 7")
	tran.writeAction("lastact")   

	tran = state2.writeTransition("epsilonCarry_with_action",state2, state3, 1)
	tran.writeAction(f"andi UDPR_2 UDPR_1 127")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {VLE_STORE_WIDTH}")
	tran.writeAction("lastact")   

	'''
	tran = state3.writeTransition("flagCarry_with_action",state3, state2, 0)
	tran.writeAction(f"andi UDPR_2 UDPR_1 128")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   
	'''

	tran = state3.writeTransition("commonCarry",state3, state0, 0)

	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"sub {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG}")  #{OUTPUT_PTR_REG}: will hold the output size after sub , {INIT_OUTPUT_PTR_REG} : hold the output pointer
	#INCREASE MaxSBP (required in cases that reading last input charachter with a common, basic, etc transitions should be followed by epsilon or flagged transitions for further actions)
	#Extract MaxSBP from X4
	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"movir {TEMP_REG0} 1")
	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"sli {TEMP_REG0} {TEMP_REG0} 32")
	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"subi {TEMP_REG0} {TEMP_REG0} 1")                                        #{TEMP_REG0} :0xFFFFF..F (32 1 bits)
	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"and {TEMP_REG0} X4 {TEMP_REG0}")                                        #{TEMP_REG0} = current maxSBP
	#Increment and Update MaxSBP
	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"addi {TEMP_REG0} {TEMP_REG0} 1")                                        #{TEMP_REG0} = current maxSBP + 1
	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"sri X4 {TEMP_REG1} 32")
	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"sli {TEMP_REG1} {TEMP_REG1} 32")                                        #{TEMP_REG1}= FCSR with cleared maxSBP
	efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"or {TEMP_REG0} {TEMP_REG1} X4")

	#efa.appendBlockAction("end_of_input_terminate_efa_VLE",f"sendr_reply {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG} X16")
	efa.appendBlockAction("end_of_input_terminate_efa_VLE","yieldt")
	efa.linkBlocktoState("end_of_input_terminate_efa_VLE",state0)





	tran = state.writeTransition("epsilonCarry_with_action", state, state4, VLD_procedure_name)
	#Find input LM offset (aligned DRAM memory copy)
	tran.writeAction(f"sri X11 X16 6")                                  # X11 (Input stream non aligned DRAM address)
	tran.writeAction(f"sli X16 X16 6")                                  # X16 (64-byte aligned DRAM address)
	tran.writeAction(f"sub X11 X16 X16")                                # X16 (input stream offset from the beginning of IN_LM_OFFSET)
	#Set SBP
	tran.writeAction(f"add X8 X16 X16")                                 # X8 (IN_LM_OFFSET), X16 (input stream offset, local to lane's LM)
	tran.writeAction(f"add X16 X7 X5")                                  # X5 (SBP in global LM address) = X16 + X7
	tran.writeAction(f"add X9 X16 X30")                                 # X30 (MaxSBP) = X9(InputSize) + X16(SBP)
	#clear rdMode, CR_Issue, CR_Advance, MaxSBP in SBCR
	tran.writeAction(f"sri X4 X29 41")                                  # rshift X29 clear SBCR(X4) left hand side
	tran.writeAction(f"sli X29 X29 41")                                 # lshift cleared SBCR back
	#Note: Set rdMode here if working in SB mode (i.e., reading input from stream buffer)
	#tran.writeAction(f)
	#Set CR_Issue
	tran.writeAction(f"movir X28 {VLD_ISSUE_WIDTH}")
	tran.writeAction("sli X28 X27 36")                                  # X27: CR_Issue
	tran.writeAction(f"or X29 X27 X29")                                 # Update CR_Issue
	#Set CR_Advance
	tran.writeAction(f"movir X28 {VLD_ADV_WIDTH}")
	tran.writeAction(f"sli X28 X27 32")                                 # X27: CR_Advance
	tran.writeAction(f"or X29 X27 X29")                                 # Update CR_Advance
	#Set MaxSBP
	tran.writeAction(f"or X29 X30 X4")                                  # Write MaxSBP(in X30) to SBCR(X4)
	#Set output LM ptr
	tran.writeAction(f"add X10 X7 {OUTPUT_PTR_REG}")                        # {OUTPUT_PTR_REG} (output stream offset, in global LM address) = X10 (output offset,local to lane's LM) + X7 (LM Base) 
	#Save original input pointer for output length calc.
	tran.writeAction(f"addi {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} 0") # {INIT_OUTPUT_PTR_REG}: stores original output pointer (for output size calculation at the end)
	tran.writeAction(f"movir UDPR_7 0")
	tran.writeAction(f"movir UDPR_2 0")
	tran.writeAction("lastact")     

	tran = state4.writeTransition("commonCarry",state4, state5, 0)

	tran = state5.writeTransition("flagCarry_with_action",state5, state6, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_1 0 {VLD_ISSUE_WIDTH}")
	tran.writeAction(f"andi UDPR_1 UDPR_3 127")
	tran.writeAction(f"lshift_t UDPR_3 UDPR_7 UDPR_3")
	tran.writeAction(f"addi UDPR_7 UDPR_7 7")
	tran.writeAction(f"or UDPR_2 UDPR_3 UDPR_2")
	tran.writeAction(f"andi UDPR_1 UDPR_1 128")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")

	tran = state6.writeTransition("commonCarry",state6, state5, 0)

	tran = state6.writeTransition("epsilonCarry_with_action",state6, state7, 1)
	tran.writeAction(f"rshift UDPR_2 UDPR_4 1")
	tran.writeAction(f"lshift UDPR_2 UDPR_6 63")
	tran.writeAction(f"sari UDPR_6 UDPR_6 63")
	tran.writeAction(f"xor UDPR_6 UDPR_4 UDPR_2")
	tran.writeAction(f"movrl UDPR_2 0({OUTPUT_PTR_REG}) 1 {VLD_STORE_WIDTH}")
	tran.writeAction("lastact")   

	tran = state7.writeTransition("epsilonCarry_with_action",state7, state4, 0)
	tran.writeAction(f"movir UDPR_7 0")
	tran.writeAction(f"movir UDPR_2 0")
	tran.writeAction("lastact")

	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"sub {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG}")  #{OUTPUT_PTR_REG}: will hold the output size after sub , {INIT_OUTPUT_PTR_R>
	#INCREASE MaxSBP (required in cases that reading last input charachter with a common, basic, etc transitions should be followed by epsilon or flagged transitions for further actions)
	#Extract MaxSBP from X4
	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"movir {TEMP_REG0} 1")
	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"sli {TEMP_REG0} {TEMP_REG0} 32")
	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"subi {TEMP_REG0} {TEMP_REG0} 1")                                        #{TEMP_REG0} :0xFFFFF..F (32 1 bits)
	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"and {TEMP_REG0} X4 {TEMP_REG0}")                                        #{TEMP_REG0} = current maxSBP
	#Increment and Update MaxSBP
	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"addi {TEMP_REG0} {TEMP_REG0} 1")                                        #{TEMP_REG0} = current maxSBP + 1
	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"sri X4 {TEMP_REG1} 32")
	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"sli {TEMP_REG1} {TEMP_REG1} 32")                                        #{TEMP_REG1}= FCSR with cleared maxSBP
	efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"or {TEMP_REG0} {TEMP_REG1} X4")

	#efa.appendBlockAction("end_of_input_terminate_efa_VLD",f"sendr_reply {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG} X16")
	efa.appendBlockAction("end_of_input_terminate_efa_VLD","yieldt")
	efa.linkBlocktoState("end_of_input_terminate_efa_VLD",state4)


	return efa
