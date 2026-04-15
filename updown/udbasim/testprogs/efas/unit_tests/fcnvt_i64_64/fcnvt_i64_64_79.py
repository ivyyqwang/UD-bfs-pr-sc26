from EFA_v2 import *
def fcnvt_i64_64_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2133836350455271141]
    tran0.writeAction("movir X16 7580")
    tran0.writeAction("slorii X16 X16 12 3725")
    tran0.writeAction("slorii X16 X16 12 2797")
    tran0.writeAction("slorii X16 X16 12 2876")
    tran0.writeAction("slorii X16 X16 12 3813")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
