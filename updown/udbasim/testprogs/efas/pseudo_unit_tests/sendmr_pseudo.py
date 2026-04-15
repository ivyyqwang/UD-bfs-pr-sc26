from EFA_v2 import *

def sendmr_pseudo():
    efa = EFA([])
    efa.code_level = "machine"
    blksize = 64

    state0 = State()  # Initial State?
    efa.add_initId(state0.state_id)
    efa.add_state(state0)

    # Add events to dictionary
    event_map = {
        "launch": 0,
        "write_ret": 1,
        "read_ret": 2,
    }

    # X8 -> mem address
    # X19 -> continuation 
    # X17 is LM PTR?
    tran0 = state0.writeTransition("eventCarry", state0, state0, event_map['launch'])
    tran0.writeAction("addi X8 X16 0")                             
    tran0.writeAction("addi X7 X18 0")                             
    tran0.writeAction("addi X9 X17 225")  
    tran0.writeAction("evi X2 X19 " + str(event_map['write_ret']) + " 1") #  
    tran0.writeAction("evi X19 X19 0 4") #  
    tran0.writeAction("sendr_dmlm X16 X19 X17")
    tran0.writeAction("yield")

    tran1 = state0.writeTransition("eventCarry", state0, state0, event_map["read_ret"])
    tran1.writeAction("movrl X8 8(X18) 0 8")
    tran1.writeAction("movir X17 1")
    tran1.writeAction("movrl X17 0(X18) 0 8")
    tran1.writeAction("yieldt")
    
    tran2 = state0.writeTransition("eventCarry", state0, state0, event_map["write_ret"])
    tran2.writeAction("evi X19 X19 " + str(event_map['read_ret']) + " 1") #  
    tran2.writeAction("send_dmlm_ld X16 X19 1")
    tran2.writeAction("yield")
    
    
    return efa