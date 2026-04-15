from EFA_v2 import *
def fcnvt_i64_64_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6876825528593729969]
    tran0.writeAction("movir X16 41104")
    tran0.writeAction("slorii X16 X16 12 2489")
    tran0.writeAction("slorii X16 X16 12 3553")
    tran0.writeAction("slorii X16 X16 12 3411")
    tran0.writeAction("slorii X16 X16 12 1615")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
