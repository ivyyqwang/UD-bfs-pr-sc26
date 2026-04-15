from EFA_v2 import *
def add_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3579372229602756570, 5292827199524053473]
    tran0.writeAction("movir X16 52819")
    tran0.writeAction("slorii X16 X16 12 2110")
    tran0.writeAction("slorii X16 X16 12 3047")
    tran0.writeAction("slorii X16 X16 12 2579")
    tran0.writeAction("slorii X16 X16 12 2086")
    tran0.writeAction("movir X17 18803")
    tran0.writeAction("slorii X17 X17 12 3684")
    tran0.writeAction("slorii X17 X17 12 2973")
    tran0.writeAction("slorii X17 X17 12 642")
    tran0.writeAction("slorii X17 X17 12 481")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
