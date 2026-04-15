from EFA_v2 import *

def sendops_pseudo_ret():
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
    tran0.writeAction("evi X2 X16 " + str(event_map['process_events']) + " 1") #  
    tran0.writeAction("evi X16 X16 0 4") #  
    tran0.writeAction(f"sendops_wret X16 {str(event_map['terminate'])} X8 4 X25")
    tran0.writeAction("yield")

    tran1 = state0.writeTransition("eventCarry", state0, state0, event_map["terminate"])
    tran1.writeAction("movrl X8 8(X18) 0 8")
    tran1.writeAction("movir X17 1")
    tran1.writeAction("movrl X17 0(X18) 0 8")
    tran1.writeAction("yieldt")
    
    tran2 = state0.writeTransition("eventCarry", state0, state0, event_map["process_events"])
    tran2.writeAction("addi X8 X20 0")
    tran2.writeAction("add X9 X20 X20")
    tran2.writeAction("add X10 X20 X20")
    tran2.writeAction("add X11 X20 X20")
    tran2.writeAction("sendr_reply X20 X20 X25")
    tran2.writeAction("yield")
    
    return efa