from EFA_v2 import *
def fcnvt_64_i64_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15523858951431873137]
    tran0.writeAction("movir X16 55151")
    tran0.writeAction("slorii X16 X16 12 3383")
    tran0.writeAction("slorii X16 X16 12 1959")
    tran0.writeAction("slorii X16 X16 12 1494")
    tran0.writeAction("slorii X16 X16 12 625")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
