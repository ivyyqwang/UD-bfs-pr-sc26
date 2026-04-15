from EFA_v2 import *
def fcnvt_64_i64_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2610303303927691362]
    tran0.writeAction("movir X16 9273")
    tran0.writeAction("slorii X16 X16 12 2704")
    tran0.writeAction("slorii X16 X16 12 1634")
    tran0.writeAction("slorii X16 X16 12 2615")
    tran0.writeAction("slorii X16 X16 12 2146")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
