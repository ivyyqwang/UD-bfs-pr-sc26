from EFA_v2 import *

TFORM_procedure_name = "TFORM_procedure"
OUTPUT_PTR_REG = "X31"
INIT_OUTPUT_PTR_REG = "X30"
ISSUE_WIDTH = 8
ADV_WIDTH = 8
STORE_WIDTH = 8

def deltaDecode():
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

	tran = state.writeTransition("commonCarry", state, state0, "TFORM_DeltaDecode_procedure")
	#Find LM offset due to aligned DRAM memory copy
	tran.writeAction(f"sri X11 X16 6")       # X11 (Input stream non aligned DRAM address)
	tran.writeAction(f"sli X16 X16 6")       # X16 (64-byte aligned DRAM address)
	tran.writeAction(f"sub X11 X16 X16")     # X16 : input stream offset from teh beginning of IN_LM_OFFSET
	#Set SBP (LM Mode)
	tran.writeAction(f"add X8 X16 X16")  	# X16: Actual input stream offset
	tran.writeAction(f"add X16 X7 X5")  	    # X5(SBP in sp) = X16 + X7
	tran.writeAction(f"add X9 X16 X30")  	# X30 (MaxSBP)= X9(InputSize) + X16(SBP) 
	#Set output ptr
	tran.writeAction(f"add X10 X7 {OUTPUT_PTR_REG}")  	# {OUTPUT_PTR_REG} (lm out ptr) = X10 (output offset) + X7 (LM Base) 
	#clear rdMode, CR_Issue, CR_Advance, MaxSBP in SBCR
	tran.writeAction(f"sri X4 X29 41")  	# (rshift) X29 clear SBCR(X4) left hand side
	tran.writeAction(f"sli X29 X29 41")  	# (lshift) shift cleared SBCR back
	#Set rdMode if working in SB mode
	#This code is LM mode
	#Set CR_Issue
	tran.writeAction(f"movir X28 {ISSUE_WIDTH}")
	tran.writeAction(f"sli X28 X27 36")  	# (lshift) X27: CR_Issue
	tran.writeAction(f"or X29 X27 X29")  	# (orr) Update CR_Issue
	#Set CR_Advance
	tran.writeAction(f"movir X28 {ADV_WIDTH}")
	tran.writeAction(f"sli X28 X27 32")  	# (lshift) X27: CR_Advance
	tran.writeAction(f"or X29 X27 X29")  	# (orr) Update CR_Advance
	#Set MaxSBP
	tran.writeAction(f"or X29 X30 X4")  	# (orr) Update MaxSBP(in X30) write to SBCR
	#Save original input pointer for output length calc.
	tran.writeAction(f"addi {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} 0")  	# {INIT_OUTPUT_PTR_REG}: will hold the original output pointer (used for output size calculation at the end of processing)

	tran.writeAction("print '[TFORM]: outputtr: %lu original outputpr: %lu x5 : %lu, x7 :%lu' X31 X30 X5 X7")
	tran.writeAction("lastact")

	tran = state0.writeTransition("commonCarry_with_action",state0, state1, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_1 0 {ISSUE_WIDTH}")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	#tran.writeAction("print '[TFORM]: output: %lu ' X17")
	tran.writeAction("lastact")

	tran = state1.writeTransition("commonCarry_with_action",state1, state2, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_2 0 {ISSUE_WIDTH}")
	tran.writeAction(f"fadd.64 UDPR_2 UDPR_1 UDPR_1")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	#tran.writeAction("print '[TFORM]: output: %lu ' X17")
	tran.writeAction("lastact")

	tran = state2.writeTransition("commonCarry_with_action",state2, state2, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_2 0 {ISSUE_WIDTH}")
	tran.writeAction(f"fadd.64 UDPR_2 UDPR_1 UDPR_1")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	#tran.writeAction("print '[TFORM]: output: %lu ' X17")
	tran.writeAction("lastact")

	efa.appendBlockAction("end_of_input_terminate_efa_deltadecode",f"sub {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG}")  #{OUTPUT_PTR_REG}: will hold the output size after sub , {INIT_OUTPUT_P>
	efa.appendBlockAction("end_of_input_terminate_efa_deltadecode","yieldt")
	efa.linkBlocktoState("end_of_input_terminate_efa_deltadecode",state0)

	#efa = streaming_event_tx(efa)
	#efa = shared_blocks(efa,state0)

	return efa

