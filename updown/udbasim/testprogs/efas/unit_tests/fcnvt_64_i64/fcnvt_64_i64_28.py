from EFA_v2 import *
def fcnvt_64_i64_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10000289470299053395]
    tran0.writeAction("movir X16 35528")
    tran0.writeAction("slorii X16 X16 12 676")
    tran0.writeAction("slorii X16 X16 12 2584")
    tran0.writeAction("slorii X16 X16 12 1041")
    tran0.writeAction("slorii X16 X16 12 3411")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
