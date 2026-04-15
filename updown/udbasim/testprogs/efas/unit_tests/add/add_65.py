from EFA_v2 import *
def add_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6800622703083993227, -7517357945362787106]
    tran0.writeAction("movir X16 41375")
    tran0.writeAction("slorii X16 X16 12 1370")
    tran0.writeAction("slorii X16 X16 12 3787")
    tran0.writeAction("slorii X16 X16 12 908")
    tran0.writeAction("slorii X16 X16 12 1909")
    tran0.writeAction("movir X17 38828")
    tran0.writeAction("slorii X17 X17 12 4012")
    tran0.writeAction("slorii X17 X17 12 1793")
    tran0.writeAction("slorii X17 X17 12 781")
    tran0.writeAction("slorii X17 X17 12 1246")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
