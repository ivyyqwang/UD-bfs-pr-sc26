from EFA_v2 import *
def sub_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6238172361161629729, -321364507867076353]
    tran0.writeAction("movir X16 43373")
    tran0.writeAction("slorii X16 X16 12 2292")
    tran0.writeAction("slorii X16 X16 12 2541")
    tran0.writeAction("slorii X16 X16 12 1233")
    tran0.writeAction("slorii X16 X16 12 4063")
    tran0.writeAction("movir X17 64394")
    tran0.writeAction("slorii X17 X17 12 1162")
    tran0.writeAction("slorii X17 X17 12 3785")
    tran0.writeAction("slorii X17 X17 12 674")
    tran0.writeAction("slorii X17 X17 12 2303")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
