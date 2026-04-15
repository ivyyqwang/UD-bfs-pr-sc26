from EFA_v2 import *

def basic_tx_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)

    state0 = State()
    state0.alphabet = [0-255]
    efa.add_state(state0)

    state1 = State()
    state1.alphabet = [0-255]
    efa.add_state(state1)

    tran = state.writeTransition("basic_with_action", state, state0, 1)
    #tran.writeAction("movir X30 0")     #X30 used temporarily to hold 0

    #X8 is the LM local address
    tran.writeAction("add X8 X7 X5")   #set SBP X5 = X8 + X7
    tran.writeAction("add X9 X8 X30")   #X30 (MaxSBP)= X9(InputSize) + X8(SBP Init)
    #clear rdMode, CR_Issue, CR_Advance, MaxSBP in SBCR
    tran.writeAction("sri X4 X29 41") #(rshift) X29 clear SBCR(X4) left hand side
    tran.writeAction("sli X29 X29 41")   #(lshift) shift cleared SBCR back
    #Set rdMode if working in SB mode
    #this code is LM mode
    #Set CR_Issue
    tran.writeAction("movir X28 1")   #(mov_imm2reg) 
    tran.writeAction("sli X28 X27 36")   #(lshift) X27: CR_Issue
    tran.writeAction("or X29 X27 X29")   #(orr) Update CR_Issue
    #Set CR_Advance
    tran.writeAction("sli X28 X27 32")   #(lshift) X27: CR_Advance
    tran.writeAction("or X29 X27 X29")     #(orr) Update CR_Advance
    #Set MaxSBP
    tran.writeAction("or X29 X30 X4")     #(orr) Update MaxSBP(in X30) write to SBCR
    tran.writeAction("lastact")

    tran = state0.writeTransition("basic_with_action", state0, state0, 98)
    tran.writeAction("add X6 X7 UDPR_14")
    tran.writeAction("yieldt")
    tran = state0.writeTransition("commonCarry_with_action", state0, state1, 99)
    tran.writeAction("sub X6 X7 UDPR_14")
    tran.writeAction("yieldt")
    tran = state0.writeTransition("commonCarry_with_action", state0, state1, 100)
    tran.writeAction("orr X6 X7 UDPR_14")
    tran.writeAction("yieldt")
    tran = state0.writeTransition("commonCarry_with_action", state0, state1, 101)
    tran.writeAction("orr X6 X7 UDPR_14")
    tran.writeAction("yieldt")
    #tran.writeAction("beq X16 X30 test")

    #efa.appendBlockAction("test","sub X31 X10 X31")
    #efa.appendBlockAction("test","yieldt")

    efa.appendBlockAction("end_of_input_terminate_efa1","sub X31 X10 X31")
    efa.appendBlockAction("end_of_input_terminate_efa1","yieldt")

    efa.linkBlocktoState("end_of_input_terminate_efa1", state0)
    return efa
