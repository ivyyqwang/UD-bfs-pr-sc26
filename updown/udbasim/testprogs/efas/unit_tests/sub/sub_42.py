from EFA_v2 import *
def sub_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8509321613716356810, 6287600170787785342]
    tran0.writeAction("movir X16 30231")
    tran0.writeAction("slorii X16 X16 12 750")
    tran0.writeAction("slorii X16 X16 12 3169")
    tran0.writeAction("slorii X16 X16 12 479")
    tran0.writeAction("slorii X16 X16 12 3786")
    tran0.writeAction("movir X17 22338")
    tran0.writeAction("slorii X17 X17 12 176")
    tran0.writeAction("slorii X17 X17 12 2765")
    tran0.writeAction("slorii X17 X17 12 2012")
    tran0.writeAction("slorii X17 X17 12 2686")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
