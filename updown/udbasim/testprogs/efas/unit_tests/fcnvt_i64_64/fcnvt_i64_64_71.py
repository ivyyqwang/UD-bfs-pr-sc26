from EFA_v2 import *
def fcnvt_i64_64_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5122948279932545357]
    tran0.writeAction("movir X16 18200")
    tran0.writeAction("slorii X16 X16 12 1509")
    tran0.writeAction("slorii X16 X16 12 364")
    tran0.writeAction("slorii X16 X16 12 318")
    tran0.writeAction("slorii X16 X16 12 2381")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
