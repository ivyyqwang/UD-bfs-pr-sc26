from EFA_v2 import *

TFORM_procedure_name = "TFORM_procedure"
OUTPUT_PTR_REG = "X31"
INIT_OUTPUT_PTR_REG = "X30"
ISSUE_WIDTH = 8
ADV_WIDTH = 8
STORE_WIDTH = 8

def RLE():
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
    state3.alphabet = [0,1]
    efa.add_state(state3)    

    state4 = State()
    state4.alphabet = [0]
    efa.add_state(state4)

    state5 = State()
    state5.alphabet = [0]
    efa.add_state(state5)
    
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
    tran.writeAction(f"print '[TFORM]: start'")
    tran.writeAction(f"movir UDPR_1 1")
    tran.writeAction("lastact")  	
		
    tran = state0.writeTransition("epsilonCarry_with_action",state0, state1, 0)
    tran.writeAction(f"movlr 0(X5) UDPR_2 0 {ISSUE_WIDTH}")
    tran.writeAction("lastact")   
		
    tran = state1.writeTransition("commonCarry",state1, state2, 0)
    tran.writeAction("ori X23 X23 0")
    tran.writeAction("lastact")

    
    tran = state2.writeTransition("flagCarry_with_action",state2, state3, 0)
    tran.writeAction(f"movlr 0(X5) UDPR_3 0 {ISSUE_WIDTH}")
    tran.writeAction(f"sub UDPR_3 UDPR_2 UDPR_4")
    tran.writeAction(f"comp_eq UDPR_4 UDPR_0 0")
    tran.writeAction("lastact")   
		
    tran = state3.writeTransition("epsilonCarry_with_action",state3, state4, 1)
    tran.writeAction(f"addi UDPR_1 UDPR_1 1")
    tran.writeAction("lastact")   
		
    tran = state3.writeTransition("epsilonCarry_with_action",state3, state5, 0)
    tran.writeAction(f"movrl UDPR_1 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
    tran.writeAction(f"movrl UDPR_2 0({OUTPUT_PTR_REG}) 1 {STORE_WIDTH}")
    tran.writeAction(f"print '[TFORM]: output: %lu %lu' X17 X18")
    tran.writeAction(f"addi UDPR_3 UDPR_2 0")
    tran.writeAction(f"movir UDPR_1 1")
    tran.writeAction("lastact")   
		
    tran = state4.writeTransition("commonCarry",state4, state2, 0)
    tran.writeAction("ori X23 X23 0")
    tran.writeAction("lastact")
		
    tran = state5.writeTransition("commonCarry",state5, state2, 0)
    tran.writeAction("ori X24 X24 0")
    tran.writeAction("lastact")

    #    efa = streaming_event_tx(efa,self.issue_width, self.adv_width, self.tform_store_width, self.debug)
    #    efa = shared_blocks(efa, state0, ISSUE_WIDTH, ADV_WIDTH, STORE_WIDTH, false)

    efa.appendBlockAction("end_of_input_terminate_efa",f"sub {OUTPUT_PTR_REG} {INIT_OUTPUT_PTR_REG} {OUTPUT_PTR_REG}")       	#X31: will hold the output size after sub , X30 : hold the
    efa.appendBlockAction("end_of_input_terminate_efa","yieldt ")
    efa.linkBlocktoState("end_of_input_terminate_efa",state0)

    return efa
