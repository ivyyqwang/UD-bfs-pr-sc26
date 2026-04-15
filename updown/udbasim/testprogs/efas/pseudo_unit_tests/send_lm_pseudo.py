from EFA_v2 import *

def send_lm_pseudo():
    efa = EFA([])
    efa.code_level = "machine"
    blksize = 64

    state0 = State()  # Initial State?
    efa.add_initId(state0.state_id)
    efa.add_state(state0)

    # Add events to dictionary
    event_map = {
        "launch_events": 0,
        "process_events": 1,
        "terminate": 2,
    }

    # Try 2 and 3 register sends
    # 
    tran0 = state0.writeTransition("eventCarry", state0, state0, event_map['launch_events'])
    tran0.writeAction("addi X7 X18 0")                             
    tran0.writeAction("addi X18 X19 5")                             
    tran0.writeAction("addi X18 X20 10")                             
    tran0.writeAction("addi X18 X21 0")                             
    tran0.writeAction("movrl X18 0(X21) 1 8")
    tran0.writeAction("movrl X19 0(X21) 1 8")
    tran0.writeAction("movrl X20 0(X21) 0 8")
    tran0.writeAction("subi X21 X21 16")
    tran0.writeAction("evi X2 X16 " + str(event_map['process_events']) + " 1") #  
    tran0.writeAction("evi X16 X16 0 4") #  
    tran0.writeAction("evi X16 X17 " + str(event_map['terminate']) + " 1") #  
    tran0.writeAction("send_wcont X16 X17 X21 3")
    tran0.writeAction("yield")

    tran1 = state0.writeTransition("eventCarry", state0, state0, event_map["terminate"])
    tran1.writeAction("bne X8 X18 op_wrong")
    tran1.writeAction("bne X9 X19 op_wrong")
    tran1.writeAction("bne X10 X20 op_wrong")
    tran1.writeAction("movir X17 1")
    tran1.writeAction("movrl X17 0(X18) 0 8")
    tran1.writeAction("yieldt")
    tran1.writeAction("op_wrong: movir X17 2")
    tran1.writeAction("movrl X17 0(X18) 0 8")
    tran1.writeAction("yieldt")
    
    tran2 = state0.writeTransition("eventCarry", state0, state0, event_map["process_events"])
    tran2.writeAction("addi X8 X21 0")
    tran2.writeAction("addi X9 X22 0")
    tran2.writeAction("addi X10 X23 0")
    tran2.writeAction("sendr3_reply X21 X22 X23 X24")
    tran2.writeAction("yield")
    
    return efa
