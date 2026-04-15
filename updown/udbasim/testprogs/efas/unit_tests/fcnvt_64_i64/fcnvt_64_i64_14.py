from EFA_v2 import *
def fcnvt_64_i64_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7500754220102625419]
    tran0.writeAction("movir X16 26648")
    tran0.writeAction("slorii X16 X16 12 131")
    tran0.writeAction("slorii X16 X16 12 2292")
    tran0.writeAction("slorii X16 X16 12 2986")
    tran0.writeAction("slorii X16 X16 12 2187")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
