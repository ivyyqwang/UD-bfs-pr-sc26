from EFA_v2 import *
def fcnvt_64_i64_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12770558307999838384]
    tran0.writeAction("movir X16 45370")
    tran0.writeAction("slorii X16 X16 12 561")
    tran0.writeAction("slorii X16 X16 12 3755")
    tran0.writeAction("slorii X16 X16 12 3047")
    tran0.writeAction("slorii X16 X16 12 176")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
