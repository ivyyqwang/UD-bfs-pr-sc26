from EFA_v2 import *
def add_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8741362148013921416, 6730496157191631336]
    tran0.writeAction("movir X16 34480")
    tran0.writeAction("slorii X16 X16 12 1815")
    tran0.writeAction("slorii X16 X16 12 170")
    tran0.writeAction("slorii X16 X16 12 2394")
    tran0.writeAction("slorii X16 X16 12 2936")
    tran0.writeAction("movir X17 23911")
    tran0.writeAction("slorii X17 X17 12 2153")
    tran0.writeAction("slorii X17 X17 12 2147")
    tran0.writeAction("slorii X17 X17 12 2207")
    tran0.writeAction("slorii X17 X17 12 488")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
