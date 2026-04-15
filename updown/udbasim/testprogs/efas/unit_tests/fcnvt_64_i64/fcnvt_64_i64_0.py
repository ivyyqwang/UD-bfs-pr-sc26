from EFA_v2 import *
def fcnvt_64_i64_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7695841509132530330]
    tran0.writeAction("movir X16 27341")
    tran0.writeAction("slorii X16 X16 12 497")
    tran0.writeAction("slorii X16 X16 12 1031")
    tran0.writeAction("slorii X16 X16 12 2255")
    tran0.writeAction("slorii X16 X16 12 666")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
