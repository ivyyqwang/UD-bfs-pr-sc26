from EFA_v2 import *
def fcnvt_i64_64_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5404644148731026591]
    tran0.writeAction("movir X16 46334")
    tran0.writeAction("slorii X16 X16 12 3468")
    tran0.writeAction("slorii X16 X16 12 2081")
    tran0.writeAction("slorii X16 X16 12 2022")
    tran0.writeAction("slorii X16 X16 12 865")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
