from EFA_v2 import *
def fdiv_64_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14828441482398691072, 2434452642089992114]
    tran0.writeAction("movir X16 52681")
    tran0.writeAction("slorii X16 X16 12 847")
    tran0.writeAction("slorii X16 X16 12 1723")
    tran0.writeAction("slorii X16 X16 12 166")
    tran0.writeAction("slorii X16 X16 12 3840")
    tran0.writeAction("movir X17 8648")
    tran0.writeAction("slorii X17 X17 12 3740")
    tran0.writeAction("slorii X17 X17 12 1946")
    tran0.writeAction("slorii X17 X17 12 1167")
    tran0.writeAction("slorii X17 X17 12 4018")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
