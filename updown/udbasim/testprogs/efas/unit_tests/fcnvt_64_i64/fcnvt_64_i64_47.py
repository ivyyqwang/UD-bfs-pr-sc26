from EFA_v2 import *
def fcnvt_64_i64_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13269019423569007863]
    tran0.writeAction("movir X16 47141")
    tran0.writeAction("slorii X16 X16 12 109")
    tran0.writeAction("slorii X16 X16 12 3339")
    tran0.writeAction("slorii X16 X16 12 2413")
    tran0.writeAction("slorii X16 X16 12 1271")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
