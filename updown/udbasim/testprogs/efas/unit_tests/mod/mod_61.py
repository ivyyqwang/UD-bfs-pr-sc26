from EFA_v2 import *
def mod_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1840105951098685458, -5283391715067565013]
    tran0.writeAction("movir X16 6537")
    tran0.writeAction("slorii X16 X16 12 1513")
    tran0.writeAction("slorii X16 X16 12 3324")
    tran0.writeAction("slorii X16 X16 12 1308")
    tran0.writeAction("slorii X16 X16 12 2066")
    tran0.writeAction("movir X17 46765")
    tran0.writeAction("slorii X17 X17 12 2547")
    tran0.writeAction("slorii X17 X17 12 2638")
    tran0.writeAction("slorii X17 X17 12 638")
    tran0.writeAction("slorii X17 X17 12 3115")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
