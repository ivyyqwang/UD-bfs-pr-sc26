from EFA_v2 import *
def fcnvt_i64_64_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1873412720963613033]
    tran0.writeAction("movir X16 58880")
    tran0.writeAction("slorii X16 X16 12 1232")
    tran0.writeAction("slorii X16 X16 12 3673")
    tran0.writeAction("slorii X16 X16 12 1088")
    tran0.writeAction("slorii X16 X16 12 3735")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
