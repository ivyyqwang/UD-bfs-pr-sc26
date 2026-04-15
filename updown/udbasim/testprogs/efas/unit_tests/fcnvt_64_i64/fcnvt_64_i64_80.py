from EFA_v2 import *
def fcnvt_64_i64_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12992116505581191917]
    tran0.writeAction("movir X16 46157")
    tran0.writeAction("slorii X16 X16 12 1106")
    tran0.writeAction("slorii X16 X16 12 107")
    tran0.writeAction("slorii X16 X16 12 2688")
    tran0.writeAction("slorii X16 X16 12 749")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
