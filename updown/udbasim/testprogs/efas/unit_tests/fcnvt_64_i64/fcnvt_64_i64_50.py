from EFA_v2 import *
def fcnvt_64_i64_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12271923319488241675]
    tran0.writeAction("movir X16 43598")
    tran0.writeAction("slorii X16 X16 12 2579")
    tran0.writeAction("slorii X16 X16 12 3416")
    tran0.writeAction("slorii X16 X16 12 3806")
    tran0.writeAction("slorii X16 X16 12 11")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
