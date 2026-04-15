from EFA_v2 import *

OUTPUT_PTR_REG = "X31"
INIT_OUTPUT_PTR_REG = "X30"

OUTPUT_PTR_REG_DATA = "X29"
OUTPUT_PTR_REG_COL = "X28"
OUTPUT_PTR_REG_ROWPTR = "X27"

TEMP_REG0 = "X29"
TEMP_REG1 = "X28"
ISSUE_WIDTH = 8
ADV_WIDTH = 8
STORE_WIDTH = 8
VLE_STORE_WIDTH=1

def Dense2CSR_deltaEncode_VLE():
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
	state8.alphabet = [0]
	efa.add_state(state8)

	tran = state.writeTransition("commonCarry_with_action", state, state0, "TFORM_Dense2CSR_procedure")
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
	tran.writeAction(f"addi {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} 0")
	#Save original input pointer for output length calc.
	tran.writeAction("lastact")
		
	tran = state0.writeTransition("commonCarry_with_action",state0, state1, 0)
	tran.writeAction(f"mov_imm2reg UDPR_4 0")
	tran.writeAction(f"mov_imm2reg UDPR_3 0")
	tran.writeAction(f"movlr 0(X5) UDPR_5 0 {ISSUE_WIDTH}")                  #nnz is the first input element
	#tran.writeAction(f"print 'sp read first word: %lu' UDPR_5")
	tran.writeAction(f"sli UDPR_5 UDPR_5 3")                                #(nnz * 8) elements are 8 bytes
	#set up OUTPUT_PTR_REG_DATA and OUTPUT_PTR_REG_COL and OUTPUT_PTR_REG_ROWPTR
	tran.writeAction(f"addi {OUTPUT_PTR_REG} {OUTPUT_PTR_REG_DATA} 0")
	tran.writeAction(f"add {OUTPUT_PTR_REG_DATA} UDPR_5 {OUTPUT_PTR_REG_COL}")
	tran.writeAction(f"add {OUTPUT_PTR_REG_COL} UDPR_5 {OUTPUT_PTR_REG_ROWPTR}")

	tran.writeAction(f"movrl UDPR_3 0({OUTPUT_PTR_REG_ROWPTR}) 1 {STORE_WIDTH}")
	tran.writeAction("lastact")

	tran = state1.writeTransition("epsilonCarry_with_action",state1, state2, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_2 0 {ISSUE_WIDTH}")
	#tran.writeAction(f"print 'sp read: %lu' UDPR_2")
	tran.writeAction("lastact")

	tran = state2.writeTransition("commonCarry",state2, state3, 0)

	tran = state3.writeTransition("flagCarry_with_action",state3, state4, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_1 0 {ISSUE_WIDTH}")
	#tran.writeAction(f"print 'sp read: %lu' UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")

	tran = state4.writeTransition("flagCarry_with_action",state4, state5, 0)
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG_DATA}) 1 {STORE_WIDTH}")
	#tran.writeAction(f"print 'sp write data: %lu' UDPR_1")
	tran.writeAction(f"movrl UDPR_4 0({OUTPUT_PTR_REG_COL}) 1 {STORE_WIDTH}")
	#tran.writeAction(f"print 'sp write col: %lu' UDPR_4")
	tran.writeAction(f"addi UDPR_3 UDPR_3 1")
	tran.writeAction(f"addi UDPR_4 UDPR_4 1")
	tran.writeAction(f"sub UDPR_2 UDPR_4 UDPR_0")
	tran.writeAction(f"comp_eq UDPR_0 UDPR_0 0")
	tran.writeAction("lastact")

	tran = state4.writeTransition("flagCarry_with_action",state4, state6, 1)
	tran.writeAction(f"addi UDPR_4 UDPR_4 1")
	tran.writeAction(f"sub UDPR_2 UDPR_4 UDPR_0")
	tran.writeAction(f"comp_eq UDPR_0 UDPR_0 0")
	tran.writeAction("lastact")

	tran = state5.writeTransition("commonCarry",state5, state3, 0)

	tran = state5.writeTransition("epsilonCarry_with_action",state5, state7, 1)
	tran.writeAction(f"mov_imm2reg UDPR_4 0")
	tran.writeAction(f"movrl UDPR_3 0({OUTPUT_PTR_REG_ROWPTR}) 1 {STORE_WIDTH}")
	#tran.writeAction(f"print 'sp write row: %lu' UDPR_3")
	tran.writeAction("lastact")

	tran = state6.writeTransition("commonCarry",state6, state3, 0)

	tran = state6.writeTransition("epsilonCarry_with_action",state6, state8, 1)
	tran.writeAction(f"mov_imm2reg UDPR_4 0")
	tran.writeAction(f"movrl UDPR_3 0({OUTPUT_PTR_REG_ROWPTR}) 1 {STORE_WIDTH}")
	tran.writeAction("lastact")

	tran = state7.writeTransition("commonCarry",state7, state3, 0)

	tran = state8.writeTransition("commonCarry",state8, state3, 0)

	efa.appendBlockAction("end_of_input_terminate_efa_Dense2CSR",f"sub {OUTPUT_PTR_REG_ROWPTR} {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG}")
	#efa.appendBlockAction("end_of_input_terminate_efa_Dense2CSR",f"sendr_reply {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG} X16")
	efa.appendBlockAction("end_of_input_terminate_efa_Dense2CSR","yieldt")
	efa.linkBlocktoState("end_of_input_terminate_efa_Dense2CSR",state0)



	state_DeltaEncode0 = State()
	state_DeltaEncode0.alphabet = [0]
	efa.add_state(state_DeltaEncode0)

	state_DeltaEncode1 = State()
	state_DeltaEncode1.alphabet = [0]
	efa.add_state(state_DeltaEncode1)

	state_DeltaEncode2 = State()
	state_DeltaEncode2.alphabet = [0]
	efa.add_state(state_DeltaEncode2)

	tran = state.writeTransition("commonCarry", state, state_DeltaEncode0, "DeltaEncode_procedure")
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

	tran = state_DeltaEncode0.writeTransition("commonCarry_with_action",state_DeltaEncode0, state_DeltaEncode1, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_1 0 {ISSUE_WIDTH}")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	tran.writeAction("lastact")

	tran = state_DeltaEncode1.writeTransition("commonCarry_with_action",state_DeltaEncode1, state_DeltaEncode2, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_2 0 {ISSUE_WIDTH}")
	tran.writeAction(f"sub UDPR_2 UDPR_1 UDPR_1")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	tran.writeAction(f"addi UDPR_2 UDPR_1 0")
	tran.writeAction("lastact")

	tran = state_DeltaEncode2.writeTransition("commonCarry_with_action",state_DeltaEncode2, state_DeltaEncode2, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_2 0 {ISSUE_WIDTH}")
	tran.writeAction(f"sub UDPR_2 UDPR_1 UDPR_1")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
	tran.writeAction(f"addi UDPR_2 UDPR_1 0")
	tran.writeAction("lastact")

	efa.appendBlockAction("end_of_input_terminate_efa_DeltaEncode",f"sub {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG}")  #{OUTPUT_PTR_REG}: will hold the output size after sub , {INIT_OUTPUT_PTR_REG} : hold the output pointer
	efa.appendBlockAction("end_of_input_terminate_efa_DeltaEncode","yieldt")
	efa.linkBlocktoState("end_of_input_terminate_efa_DeltaEncode",state_DeltaEncode0)







	stateVLE0 = State()
	stateVLE0.alphabet = [0]
	efa.add_state(stateVLE0)

	stateVLE1 = State()
	stateVLE1.alphabet = [0]
	efa.add_state(stateVLE1)

	stateVLE2 = State()
	stateVLE2.alphabet = [0,1]
	efa.add_state(stateVLE2)

	stateVLE4 = State()
	stateVLE4.alphabet = [0]
	efa.add_state(stateVLE4)

	tran = state.writeTransition("commonCarry", state, stateVLE0, "VLE_procedure")
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
	tran.writeAction("lastact")  	

	tran = stateVLE0.writeTransition("epsilonCarry_with_action",stateVLE0, stateVLE1, 0)
	tran.writeAction(f"movlr 0(X5) UDPR_2 0 {ISSUE_WIDTH}")
	tran.writeAction(f"lshift UDPR_2 UDPR_3 1")
	tran.writeAction(f"sari UDPR_2 UDPR_4 63")
	tran.writeAction(f"xor UDPR_4 UDPR_3 UDPR_2")
	tran.writeAction("lastact")   

	tran = stateVLE1.writeTransition("flagCarry_with_action",stateVLE1, stateVLE2, 0)
	tran.writeAction(f"movir UDPR_1 -128")
	tran.writeAction(f"and UDPR_1 UDPR_2 UDPR_1")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   

	tran = stateVLE2.writeTransition("epsilonCarry_with_action",stateVLE2, stateVLE1, 0)
	tran.writeAction(f"andi UDPR_2 UDPR_1 127")
	tran.writeAction(f"ori UDPR_1 UDPR_1 128")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {VLE_STORE_WIDTH}")
	tran.writeAction(f"rshift UDPR_2 UDPR_2 7")
	tran.writeAction("lastact")   

	tran = stateVLE2.writeTransition("epsilonCarry_with_action",stateVLE2, stateVLE4, 1)
	tran.writeAction(f"andi UDPR_2 UDPR_1 127")
	tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {VLE_STORE_WIDTH}")
	tran.writeAction("lastact")   

	'''
	tran = state3.writeTransition("flagCarry_with_action",state3, state2, 0)
	tran.writeAction(f"andi UDPR_2 UDPR_1 128")
	tran.writeAction(f"comp_eq UDPR_1 UDPR_0 0")
	tran.writeAction("lastact")   
	'''

	tran = stateVLE4.writeTransition("commonCarry",stateVLE4, stateVLE0, 0)

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
	efa.linkBlocktoState("end_of_input_terminate_efa_VLE",stateVLE0)

	return efa
