from EFA_v2 import *
def modi_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7510209904089325874, 15059]
    tran0.writeAction("movir X16 26681")
    tran0.writeAction("slorii X16 X16 12 2561")
    tran0.writeAction("slorii X16 X16 12 3569")
    tran0.writeAction("slorii X16 X16 12 3542")
    tran0.writeAction("slorii X16 X16 12 306")
    tran0.writeAction("modi X16 X17 15059")
    tran0.writeAction("yieldt")
    return efa
