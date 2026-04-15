from EFA_v2 import *
def fcnvt_64_i64_62():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11126560786491433351]
    tran0.writeAction("movir X16 39529")
    tran0.writeAction("slorii X16 X16 12 1985")
    tran0.writeAction("slorii X16 X16 12 1426")
    tran0.writeAction("slorii X16 X16 12 2510")
    tran0.writeAction("slorii X16 X16 12 391")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
