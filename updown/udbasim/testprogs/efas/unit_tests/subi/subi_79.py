from EFA_v2 import *
def subi_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3260834266078520944, 16176]
    tran0.writeAction("movir X16 11584")
    tran0.writeAction("slorii X16 X16 12 3319")
    tran0.writeAction("slorii X16 X16 12 3333")
    tran0.writeAction("slorii X16 X16 12 130")
    tran0.writeAction("slorii X16 X16 12 1648")
    tran0.writeAction("subi X16 X17 16176")
    tran0.writeAction("yieldt")
    return efa
