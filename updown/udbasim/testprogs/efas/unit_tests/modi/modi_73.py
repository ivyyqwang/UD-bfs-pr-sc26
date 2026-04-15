from EFA_v2 import *
def modi_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9071436531182434019, 11142]
    tran0.writeAction("movir X16 33307")
    tran0.writeAction("slorii X16 X16 12 3208")
    tran0.writeAction("slorii X16 X16 12 2452")
    tran0.writeAction("slorii X16 X16 12 1512")
    tran0.writeAction("slorii X16 X16 12 2333")
    tran0.writeAction("modi X16 X17 11142")
    tran0.writeAction("yieldt")
    return efa
