from EFA_v2 import *
def fcnvt_64_i64_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11580138020603244982]
    tran0.writeAction("movir X16 41140")
    tran0.writeAction("slorii X16 X16 12 3746")
    tran0.writeAction("slorii X16 X16 12 3312")
    tran0.writeAction("slorii X16 X16 12 211")
    tran0.writeAction("slorii X16 X16 12 438")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
