from EFA_v2 import *
def muli_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3459974560991525812, -12937]
    tran0.writeAction("movir X16 12292")
    tran0.writeAction("slorii X16 X16 12 1224")
    tran0.writeAction("slorii X16 X16 12 2063")
    tran0.writeAction("slorii X16 X16 12 3227")
    tran0.writeAction("slorii X16 X16 12 2996")
    tran0.writeAction("muli X16 X17 -12937")
    tran0.writeAction("yieldt")
    return efa
