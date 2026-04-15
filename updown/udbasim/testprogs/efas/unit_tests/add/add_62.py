from EFA_v2 import *
def add_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7410852841503972919, -7083964687746751533]
    tran0.writeAction("movir X16 26328")
    tran0.writeAction("slorii X16 X16 12 2614")
    tran0.writeAction("slorii X16 X16 12 1308")
    tran0.writeAction("slorii X16 X16 12 2205")
    tran0.writeAction("slorii X16 X16 12 3639")
    tran0.writeAction("movir X17 40368")
    tran0.writeAction("slorii X17 X17 12 2874")
    tran0.writeAction("slorii X17 X17 12 1569")
    tran0.writeAction("slorii X17 X17 12 1818")
    tran0.writeAction("slorii X17 X17 12 979")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
