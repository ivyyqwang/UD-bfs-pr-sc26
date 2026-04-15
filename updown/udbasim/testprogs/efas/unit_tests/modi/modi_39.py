from EFA_v2 import *
def modi_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5802682005728160855, 30177]
    tran0.writeAction("movir X16 20615")
    tran0.writeAction("slorii X16 X16 12 1096")
    tran0.writeAction("slorii X16 X16 12 2639")
    tran0.writeAction("slorii X16 X16 12 4006")
    tran0.writeAction("slorii X16 X16 12 3159")
    tran0.writeAction("modi X16 X17 30177")
    tran0.writeAction("yieldt")
    return efa
