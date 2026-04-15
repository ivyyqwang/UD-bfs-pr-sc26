from EFA_v2 import *

def test0():
    efa = EFA([])
    efa.code_level = "machine"
    state0 = State()  # Initial State?
    efa.add_initId(state0.state_id)
    efa.add_state(state0)

    # Add events to dictionary
    event_map = {
        "launch_events": 0,
    }

    # OB_1 repeated for OB count
    tran0 = state0.writeTransition("eventCarry", state0, state0, event_map['launch_events'])
    tran0.writeAction("addi X16 X17 10")                             
    tran0.writeAction("yield_terminate")

    return efa