from EFA_v2 import *
def divi_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6436439963834651183, 3610]
    tran0.writeAction("movir X16 42669")
    tran0.writeAction("slorii X16 X16 12 703")
    tran0.writeAction("slorii X16 X16 12 1121")
    tran0.writeAction("slorii X16 X16 12 2078")
    tran0.writeAction("slorii X16 X16 12 3537")
    tran0.writeAction("divi X16 X17 3610")
    tran0.writeAction("yieldt")
    return efa
