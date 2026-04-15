from EFA_v2 import *
def fcnvt_i64_64_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5572030901217495001]
    tran0.writeAction("movir X16 45740")
    tran0.writeAction("slorii X16 X16 12 694")
    tran0.writeAction("slorii X16 X16 12 2767")
    tran0.writeAction("slorii X16 X16 12 1767")
    tran0.writeAction("slorii X16 X16 12 2087")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
