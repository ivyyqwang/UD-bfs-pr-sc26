from EFA_v2 import *
def fcnvt_i64_64_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7687958811687883619]
    tran0.writeAction("movir X16 27313")
    tran0.writeAction("slorii X16 X16 12 476")
    tran0.writeAction("slorii X16 X16 12 3714")
    tran0.writeAction("slorii X16 X16 12 2009")
    tran0.writeAction("slorii X16 X16 12 867")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
