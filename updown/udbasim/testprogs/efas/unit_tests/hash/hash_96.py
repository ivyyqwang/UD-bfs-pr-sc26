from EFA_v2 import *
def hash_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1880258598994272047, 268808901298904838]
    tran0.writeAction("movir X16 58855")
    tran0.writeAction("slorii X16 X16 12 4012")
    tran0.writeAction("slorii X16 X16 12 1065")
    tran0.writeAction("slorii X16 X16 12 298")
    tran0.writeAction("slorii X16 X16 12 209")
    tran0.writeAction("movir X17 955")
    tran0.writeAction("slorii X17 X17 12 4")
    tran0.writeAction("slorii X17 X17 12 1410")
    tran0.writeAction("slorii X17 X17 12 1573")
    tran0.writeAction("slorii X17 X17 12 3846")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
