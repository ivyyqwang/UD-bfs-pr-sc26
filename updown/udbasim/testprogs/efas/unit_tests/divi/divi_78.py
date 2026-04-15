from EFA_v2 import *
def divi_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1250373925659423879, 11846]
    tran0.writeAction("movir X16 61093")
    tran0.writeAction("slorii X16 X16 12 3192")
    tran0.writeAction("slorii X16 X16 12 2580")
    tran0.writeAction("slorii X16 X16 12 2700")
    tran0.writeAction("slorii X16 X16 12 2937")
    tran0.writeAction("divi X16 X17 11846")
    tran0.writeAction("yieldt")
    return efa
