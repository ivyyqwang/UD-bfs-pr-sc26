from EFA_v2 import *
def mod_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7425913625040269573, 1210251642988911191]
    tran0.writeAction("movir X16 39153")
    tran0.writeAction("slorii X16 X16 12 3502")
    tran0.writeAction("slorii X16 X16 12 1782")
    tran0.writeAction("slorii X16 X16 12 3036")
    tran0.writeAction("slorii X16 X16 12 3835")
    tran0.writeAction("movir X17 4299")
    tran0.writeAction("slorii X17 X17 12 2775")
    tran0.writeAction("slorii X17 X17 12 1285")
    tran0.writeAction("slorii X17 X17 12 765")
    tran0.writeAction("slorii X17 X17 12 2647")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
