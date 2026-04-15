from EFA_v2 import *
def fcnvt_i64_64_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1099799268016213765]
    tran0.writeAction("movir X16 61628")
    tran0.writeAction("slorii X16 X16 12 2982")
    tran0.writeAction("slorii X16 X16 12 1161")
    tran0.writeAction("slorii X16 X16 12 2699")
    tran0.writeAction("slorii X16 X16 12 251")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
