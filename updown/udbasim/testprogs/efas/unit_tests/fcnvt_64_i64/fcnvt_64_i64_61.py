from EFA_v2 import *
def fcnvt_64_i64_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13457393179590595361]
    tran0.writeAction("movir X16 47810")
    tran0.writeAction("slorii X16 X16 12 1084")
    tran0.writeAction("slorii X16 X16 12 3048")
    tran0.writeAction("slorii X16 X16 12 1073")
    tran0.writeAction("slorii X16 X16 12 801")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
