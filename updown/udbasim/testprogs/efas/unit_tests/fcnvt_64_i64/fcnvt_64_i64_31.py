from EFA_v2 import *
def fcnvt_64_i64_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4962548130872747690]
    tran0.writeAction("movir X16 17630")
    tran0.writeAction("slorii X16 X16 12 2099")
    tran0.writeAction("slorii X16 X16 12 2937")
    tran0.writeAction("slorii X16 X16 12 1838")
    tran0.writeAction("slorii X16 X16 12 1706")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
