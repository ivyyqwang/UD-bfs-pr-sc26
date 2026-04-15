from EFA_v2 import *
def fcnvt_64_i64_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [469388360169898618]
    tran0.writeAction("movir X16 1667")
    tran0.writeAction("slorii X16 X16 12 2467")
    tran0.writeAction("slorii X16 X16 12 2565")
    tran0.writeAction("slorii X16 X16 12 2580")
    tran0.writeAction("slorii X16 X16 12 634")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
