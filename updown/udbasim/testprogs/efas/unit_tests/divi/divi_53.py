from EFA_v2 import *
def divi_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6305021635192525177, -8080]
    tran0.writeAction("movir X16 43136")
    tran0.writeAction("slorii X16 X16 12 259")
    tran0.writeAction("slorii X16 X16 12 2669")
    tran0.writeAction("slorii X16 X16 12 806")
    tran0.writeAction("slorii X16 X16 12 3719")
    tran0.writeAction("divi X16 X17 -8080")
    tran0.writeAction("yieldt")
    return efa
