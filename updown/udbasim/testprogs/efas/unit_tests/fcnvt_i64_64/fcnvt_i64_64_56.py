from EFA_v2 import *
def fcnvt_i64_64_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6230416364679859272]
    tran0.writeAction("movir X16 22134")
    tran0.writeAction("slorii X16 X16 12 3626")
    tran0.writeAction("slorii X16 X16 12 3179")
    tran0.writeAction("slorii X16 X16 12 2144")
    tran0.writeAction("slorii X16 X16 12 3144")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
