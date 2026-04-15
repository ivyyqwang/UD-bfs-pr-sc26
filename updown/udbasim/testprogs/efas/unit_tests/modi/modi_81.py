from EFA_v2 import *
def modi_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-9109717732456000237, -5557]
    tran0.writeAction("movir X16 33171")
    tran0.writeAction("slorii X16 X16 12 3199")
    tran0.writeAction("slorii X16 X16 12 3288")
    tran0.writeAction("slorii X16 X16 12 3617")
    tran0.writeAction("slorii X16 X16 12 1299")
    tran0.writeAction("modi X16 X17 -5557")
    tran0.writeAction("yieldt")
    return efa
