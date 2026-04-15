from EFA_v2 import *

TFORM_procedure_name = "TFORM_procedure"
OUTPUT_PTR_REG = "X31"
INIT_OUTPUT_PTR_REG = "X30"
TEMP_REG0 = "X29"
TEMP_REG1 = "X28"
ISSUE_WIDTH = 8
ADV_WIDTH = 8
STORE_WIDTH = 8

def COO2CSR():
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
	state2.alphabet = [0]
	efa.add_state(state2)

	state3 = State()
	state3.alphabet = [0]
	efa.add_state(state3)

	state4 = State()
	state4.alphabet = [0,1]
	efa.add_state(state4)

	state5 = State()
	state5.alphabet = [0,1]
	efa.add_state(state5)

	state6 = State()
	state6.alphabet = [0,1]
	efa.add_state(state6)

	state7 = State()
	state7.alphabet = [0]
	efa.add_state(state7)

	state8 = State()
	state8.alphabet = [0,1]
	efa.add_state(state8)

	state9 = State()
	state9.alphabet = [0]
	efa.add_state(state9)

	state10 = State()
	state10.alphabet = [0]
	efa.add_state(state10)

	tran = state.writeTransition("commonCarry_with_action", state, state0, TFORM_procedure_name)
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
	tran.writeAction(f"movir X28 {ISSUE_WIDTH}")
	tran.writeAction("sli X28 X27 36")  	                            # X27: CR_Issue
	tran.writeAction(f"or X29 X27 X29")  	                            # Update CR_Issue
	#Set CR_Advance
	tran.writeAction(f"movir X28 {ADV_WIDTH}")
	tran.writeAction(f"sli X28 X27 32")  	                            # X27: CR_Advance
	tran.writeAction(f"or X29 X27 X29")  	                            # Update CR_Advance
	#Set MaxSBP
	tran.writeAction(f"or X29 X30 X4")  	                            # Write MaxSBP(in X30) to SBCR(X4)
	#Set output LM ptr
	tran.writeAction(f"add X10 X7 {OUTPUT_PTR_REG}")  	                # {OUTPUT_PTR_REG} (output stream offset, in global LM address) = X10 (output offset,local to lane's LM) + X7 (LM Base) 
	#Save original input pointer for output length calc.
	tran.writeAction(f"addi {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} 0") # {INIT_OUTPUT_PTR_REG}: stores original output pointer (for output size calculation at the end)
	tran.writeAction(f"movir UDPR_6 0")
	tran.writeAction(f"movir UDPR_7 0")
	tran.writeAction(f"movrl UDPR_7 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	tran.writeAction("lastact")  	

	tran = state0.writeTransition("commonCarry_with_action",state0, state1, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_2 0 {ISSUE_WIDTH}")
	tran.writeAction("lastact")   

	tran = state1.writeTransition("epsilonCarry_with_action",state1, state2, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_3 0 {ISSUE_WIDTH}")
	tran.writeAction("lastact")   

	tran = state2.writeTransition("commonCarry",state2, state3, 0)

	tran = state3.writeTransition("flagCarry_with_action",state3, state4, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_4 0 {ISSUE_WIDTH}")
	tran.writeAction(f"sub UDPR_4 UDPR_6 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = state4.writeTransition("flagCarry_with_action",state4, state5, 0)
	tran.writeAction(f"sub UDPR_4 UDPR_6 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = state4.writeTransition("flagCarry_with_action",state4, state6, 1)
	tran.writeAction(f"addi UDPR_7 UDPR_7 1")
	tran.writeAction(f"sub UDPR_3 UDPR_7 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = state5.writeTransition("flagCarry_with_action",state5, state6, 1)
	tran.writeAction(f"addi UDPR_7 UDPR_7 1")
	tran.writeAction(f"sub UDPR_3 UDPR_7 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = state5.writeTransition("epsilonCarry_with_action",state5, state7, 0)
	tran.writeAction(f"movrl UDPR_7 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	#tran.writeAction(f"movlr 0(X5) UDPR_7 0 {ISSUE_WIDTH}")
	tran.writeAction(f"addi UDPR_6 UDPR_6 1")
	tran.writeAction("lastact")   

	tran = state6.writeTransition("commonCarry",state6, state3, 0)

	tran = state6.writeTransition("flagCarry_with_action",state6, state8, 1)
	tran.writeAction(f"sub UDPR_2 UDPR_6 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = state7.writeTransition("flagCarry_with_action",state7, state5, 0)
	tran.writeAction(f"sub UDPR_4 UDPR_6 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = state8.writeTransition("epsilonCarry_with_action",state8, state9, 0)
	tran.writeAction(f"movrl UDPR_7 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	#tran.writeAction(f"movlr 0(X5) UDPR_7 0 {ISSUE_WIDTH}")
	tran.writeAction(f"addi UDPR_6 UDPR_6 1")
	tran.writeAction("lastact")   

	tran = state8.writeTransition("epsilonCarry_with_action",state8, state10, 1)
	tran.writeAction(f"sub {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG}")
	tran.writeAction(f"sendr_reply {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG} X16")
	tran.writeAction(f"yieldt")
	tran.writeAction("lastact")   

	tran = state9.writeTransition("flagCarry_with_action",state9, state8, 0)
	tran.writeAction(f"sub UDPR_2 UDPR_6 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = state10.writeTransition("commonCarry_with_action",state10, state0, 0)
	tran.writeAction(f"movir UDPR_6 0")
	tran.writeAction(f"movir UDPR_7 0")
	tran.writeAction(f"movrl UDPR_7 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	tran.writeAction("lastact")   

	efa.appendBlockAction("end_of_input_terminate_efa",f"sub {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG}")  #{OUTPUT_PTR_REG}: will hold the output size after sub , {INIT_OUTPUT_PTR_REG} : hold the output pointer
	#INCREASE MaxSBP (required in cases that reading last input charachter with a common, basic, etc transitions should be followed by epsilon or flagged transitions for further actions)
	#Extract MaxSBP from X4
	efa.appendBlockAction("end_of_input_terminate_efa",f"movir {TEMP_REG0} 1")
	efa.appendBlockAction("end_of_input_terminate_efa",f"sli {TEMP_REG0} {TEMP_REG0} 32")
	efa.appendBlockAction("end_of_input_terminate_efa",f"subi {TEMP_REG0} {TEMP_REG0} 1")                                        #{TEMP_REG0} :0xFFFFF..F (32 1 bits)
	efa.appendBlockAction("end_of_input_terminate_efa",f"and {TEMP_REG0} X4 {TEMP_REG0}")                                        #{TEMP_REG0} = current maxSBP
	#Increment and Update MaxSBP
	efa.appendBlockAction("end_of_input_terminate_efa",f"addi {TEMP_REG0} {TEMP_REG0} 1")                                        #{TEMP_REG0} = current maxSBP + 1
	efa.appendBlockAction("end_of_input_terminate_efa",f"sri X4 {TEMP_REG1} 32")
	efa.appendBlockAction("end_of_input_terminate_efa",f"sli {TEMP_REG1} {TEMP_REG1} 32")                                        #{TEMP_REG1}= FCSR with cleared maxSBP
	efa.appendBlockAction("end_of_input_terminate_efa",f"or {TEMP_REG0} {TEMP_REG1} X4")

	#efa.appendBlockAction("end_of_input_terminate_efa",f"sendr_reply {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG} X16")
	efa.appendBlockAction("end_of_input_terminate_efa","yieldt")
	efa.linkBlocktoState("end_of_input_terminate_efa",state0)


	return efa
