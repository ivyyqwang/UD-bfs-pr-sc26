from EFA_v2 import *
def fcnvt_64_i64_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9919430519848008663]
    tran0.writeAction("movir X16 35240")
    tran0.writeAction("slorii X16 X16 12 3672")
    tran0.writeAction("slorii X16 X16 12 157")
    tran0.writeAction("slorii X16 X16 12 2903")
    tran0.writeAction("slorii X16 X16 12 3031")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
