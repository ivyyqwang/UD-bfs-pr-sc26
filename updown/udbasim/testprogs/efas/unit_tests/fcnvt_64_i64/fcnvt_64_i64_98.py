from EFA_v2 import *
def fcnvt_64_i64_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9818309275602655968]
    tran0.writeAction("movir X16 34881")
    tran0.writeAction("slorii X16 X16 12 2628")
    tran0.writeAction("slorii X16 X16 12 1083")
    tran0.writeAction("slorii X16 X16 12 897")
    tran0.writeAction("slorii X16 X16 12 2784")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
