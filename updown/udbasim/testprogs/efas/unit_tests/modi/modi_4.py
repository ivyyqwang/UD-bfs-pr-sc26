from EFA_v2 import *
def modi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6472158870073177128, -19340]
    tran0.writeAction("movir X16 42542")
    tran0.writeAction("slorii X16 X16 12 1116")
    tran0.writeAction("slorii X16 X16 12 3187")
    tran0.writeAction("slorii X16 X16 12 1616")
    tran0.writeAction("slorii X16 X16 12 3032")
    tran0.writeAction("modi X16 X17 -19340")
    tran0.writeAction("yieldt")
    return efa
