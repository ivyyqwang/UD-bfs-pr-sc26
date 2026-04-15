from EFA_v2 import *
def fcnvt_64_i64_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5247477104350080383]
    tran0.writeAction("movir X16 18642")
    tran0.writeAction("slorii X16 X16 12 3209")
    tran0.writeAction("slorii X16 X16 12 4035")
    tran0.writeAction("slorii X16 X16 12 3202")
    tran0.writeAction("slorii X16 X16 12 3455")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
