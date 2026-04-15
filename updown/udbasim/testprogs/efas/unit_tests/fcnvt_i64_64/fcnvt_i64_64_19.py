from EFA_v2 import *
def fcnvt_i64_64_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4421601221619277230]
    tran0.writeAction("movir X16 15708")
    tran0.writeAction("slorii X16 X16 12 2798")
    tran0.writeAction("slorii X16 X16 12 617")
    tran0.writeAction("slorii X16 X16 12 205")
    tran0.writeAction("slorii X16 X16 12 3502")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
