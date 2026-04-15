from EFA_v2 import *
def fcnvt_i64_64_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2960895610245317364]
    tran0.writeAction("movir X16 10519")
    tran0.writeAction("slorii X16 X16 12 877")
    tran0.writeAction("slorii X16 X16 12 3769")
    tran0.writeAction("slorii X16 X16 12 2808")
    tran0.writeAction("slorii X16 X16 12 756")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
