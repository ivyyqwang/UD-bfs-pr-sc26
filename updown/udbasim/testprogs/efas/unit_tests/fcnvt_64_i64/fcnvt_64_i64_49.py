from EFA_v2 import *
def fcnvt_64_i64_49():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17062474268513172648]
    tran0.writeAction("movir X16 60618")
    tran0.writeAction("slorii X16 X16 12 351")
    tran0.writeAction("slorii X16 X16 12 579")
    tran0.writeAction("slorii X16 X16 12 3975")
    tran0.writeAction("slorii X16 X16 12 3240")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
