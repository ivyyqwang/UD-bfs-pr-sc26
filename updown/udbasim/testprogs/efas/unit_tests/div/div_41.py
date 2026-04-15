from EFA_v2 import *
def div_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8131421440058601766, -1076633909504103796]
    tran0.writeAction("movir X16 28888")
    tran0.writeAction("slorii X16 X16 12 2507")
    tran0.writeAction("slorii X16 X16 12 1973")
    tran0.writeAction("slorii X16 X16 12 2819")
    tran0.writeAction("slorii X16 X16 12 294")
    tran0.writeAction("movir X17 61711")
    tran0.writeAction("slorii X17 X17 12 114")
    tran0.writeAction("slorii X17 X17 12 2526")
    tran0.writeAction("slorii X17 X17 12 3554")
    tran0.writeAction("slorii X17 X17 12 2700")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
