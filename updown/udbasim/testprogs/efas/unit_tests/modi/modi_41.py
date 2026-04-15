from EFA_v2 import *
def modi_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2938885396370264920, -10684]
    tran0.writeAction("movir X16 55094")
    tran0.writeAction("slorii X16 X16 12 4020")
    tran0.writeAction("slorii X16 X16 12 3465")
    tran0.writeAction("slorii X16 X16 12 3142")
    tran0.writeAction("slorii X16 X16 12 3240")
    tran0.writeAction("modi X16 X17 -10684")
    tran0.writeAction("yieldt")
    return efa
