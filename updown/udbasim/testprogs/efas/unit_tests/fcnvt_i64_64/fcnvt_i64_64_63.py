from EFA_v2 import *
def fcnvt_i64_64_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1544872585634728390]
    tran0.writeAction("movir X16 5488")
    tran0.writeAction("slorii X16 X16 12 2006")
    tran0.writeAction("slorii X16 X16 12 3705")
    tran0.writeAction("slorii X16 X16 12 4084")
    tran0.writeAction("slorii X16 X16 12 2502")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
