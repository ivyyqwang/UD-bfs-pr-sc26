from EFA_v2 import *
def fcnvt_64_i64_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2959339246902612888]
    tran0.writeAction("movir X16 10513")
    tran0.writeAction("slorii X16 X16 12 2805")
    tran0.writeAction("slorii X16 X16 12 3493")
    tran0.writeAction("slorii X16 X16 12 2057")
    tran0.writeAction("slorii X16 X16 12 920")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
