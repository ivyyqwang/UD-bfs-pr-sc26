from EFA_v2 import *

def sendmops_pseudo():
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
    tran0.writeAction(f"sendops_dmlm_wret X8 {event_map['terminate']} X9 4 X25")
    tran0.writeAction("yield")
    
    
    tran1 = state0.writeTransition("eventCarry", state0, state0, event_map['terminate'])
    tran1.writeAction("movir X17 1")
    tran1.writeAction("movrl X17 0(X18) 0 8")
    tran1.writeAction("yieldt")

    return efa