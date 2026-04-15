from EFA_v2 import *
def add_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1673189416711694052, 860480737633289993]
    tran0.writeAction("movir X16 59591")
    tran0.writeAction("slorii X16 X16 12 2609")
    tran0.writeAction("slorii X16 X16 12 1830")
    tran0.writeAction("slorii X16 X16 12 3917")
    tran0.writeAction("slorii X16 X16 12 2332")
    tran0.writeAction("movir X17 3057")
    tran0.writeAction("slorii X17 X17 12 170")
    tran0.writeAction("slorii X17 X17 12 3070")
    tran0.writeAction("slorii X17 X17 12 2860")
    tran0.writeAction("slorii X17 X17 12 1801")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
