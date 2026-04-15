from EFA_v2 import *
def fcnvt_i64_64_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1581427708548381356]
    tran0.writeAction("movir X16 59917")
    tran0.writeAction("slorii X16 X16 12 2622")
    tran0.writeAction("slorii X16 X16 12 186")
    tran0.writeAction("slorii X16 X16 12 56")
    tran0.writeAction("slorii X16 X16 12 1364")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
