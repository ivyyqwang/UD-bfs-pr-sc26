from EFA_v2 import *
def addi():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 10")
    tran0.writeAction("addi X16 X17 20")
    tran0.writeAction("addi X7 X18 0")
    tran0.writeAction("movrl X17 0(X18) 0 8")
    tran0.writeAction("yieldt")
    return efa
