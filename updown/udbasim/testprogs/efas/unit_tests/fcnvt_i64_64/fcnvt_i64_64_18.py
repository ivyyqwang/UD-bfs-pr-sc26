from EFA_v2 import *
def fcnvt_i64_64_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1139916262383672096]
    tran0.writeAction("movir X16 61486")
    tran0.writeAction("slorii X16 X16 12 835")
    tran0.writeAction("slorii X16 X16 12 746")
    tran0.writeAction("slorii X16 X16 12 3810")
    tran0.writeAction("slorii X16 X16 12 1248")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
