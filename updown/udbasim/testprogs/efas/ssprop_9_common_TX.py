from EFA_v2 import *

def ssprop_9_common_TX():
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
    
    state2 = State()
    state2.alphabet = [0-255]
    efa.add_state(state2)

    state3 = State()
    state3.alphabet = [0-255]
    efa.add_state(state3)

    tran = state.writeTransition("defaultCarry", state, state0, 1)
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
    #counter initializer
    tran.writeAction("movir X17 0")
    tran.writeAction("movir X18 0")
    tran.writeAction("lastact")

    tran = state0.writeTransition("defaultCarry", state0, state1, 'default')

    tran = state1.writeTransition("defaultCarry", state1, state2, 99)
    tran.writeAction("addi X18 X18 1")
    tran.writeAction("lastact")

    tran = state1.writeTransition("basic", state1, state3, 'default')

    tran = state2.writeTransition("basic", state2, state3, 'default')

    for i in range (0,256):
        if i != 100:
            tran = state3.writeTransition("basic_with_action", state3, state3, i)
            tran.writeAction("addi X17 X17 1")
            tran.writeAction("lastact")
        else:
            tran = state3.writeTransition("defaultCarry", state3, state0, i)
            tran.writeAction("yieldt")

    #efa.appendBlockAction("test","sub X31 X10 X31")
    #efa.appendBlockAction("test","yieldt")

    efa.appendBlockAction("end_of_input_terminate_efa1","sub X31 X10 X31")
    efa.appendBlockAction("end_of_input_terminate_efa1","yieldt")

    efa.linkBlocktoState("end_of_input_terminate_efa1", state0)
    return efa
