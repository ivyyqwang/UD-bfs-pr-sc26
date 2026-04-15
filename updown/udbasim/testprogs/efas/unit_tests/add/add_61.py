from EFA_v2 import *
def add_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2826341174818666266, 5540963871548859905]
    tran0.writeAction("movir X16 55494")
    tran0.writeAction("slorii X16 X16 12 3354")
    tran0.writeAction("slorii X16 X16 12 3348")
    tran0.writeAction("slorii X16 X16 12 3576")
    tran0.writeAction("slorii X16 X16 12 2278")
    tran0.writeAction("movir X17 19685")
    tran0.writeAction("slorii X17 X17 12 1876")
    tran0.writeAction("slorii X17 X17 12 2220")
    tran0.writeAction("slorii X17 X17 12 3862")
    tran0.writeAction("slorii X17 X17 12 1537")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
