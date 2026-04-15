from EFA_v2 import *
def fcnvt_64_i64_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1267780118240448806]
    tran0.writeAction("movir X16 4504")
    tran0.writeAction("slorii X16 X16 12 244")
    tran0.writeAction("slorii X16 X16 12 3313")
    tran0.writeAction("slorii X16 X16 12 101")
    tran0.writeAction("slorii X16 X16 12 294")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
