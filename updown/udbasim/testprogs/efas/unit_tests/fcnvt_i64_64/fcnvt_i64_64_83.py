from EFA_v2 import *
def fcnvt_i64_64_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8419672966793539767]
    tran0.writeAction("movir X16 29912")
    tran0.writeAction("slorii X16 X16 12 2815")
    tran0.writeAction("slorii X16 X16 12 1078")
    tran0.writeAction("slorii X16 X16 12 2819")
    tran0.writeAction("slorii X16 X16 12 183")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
