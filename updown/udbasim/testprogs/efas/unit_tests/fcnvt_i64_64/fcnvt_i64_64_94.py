from EFA_v2 import *
def fcnvt_i64_64_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-354220047894575592]
    tran0.writeAction("movir X16 64277")
    tran0.writeAction("slorii X16 X16 12 2283")
    tran0.writeAction("slorii X16 X16 12 3648")
    tran0.writeAction("slorii X16 X16 12 3776")
    tran0.writeAction("slorii X16 X16 12 1560")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
