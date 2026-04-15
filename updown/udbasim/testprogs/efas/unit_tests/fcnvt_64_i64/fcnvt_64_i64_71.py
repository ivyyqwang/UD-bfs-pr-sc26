from EFA_v2 import *
def fcnvt_64_i64_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13488381492124481563]
    tran0.writeAction("movir X16 47920")
    tran0.writeAction("slorii X16 X16 12 1464")
    tran0.writeAction("slorii X16 X16 12 169")
    tran0.writeAction("slorii X16 X16 12 135")
    tran0.writeAction("slorii X16 X16 12 2075")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
