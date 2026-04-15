from EFA_v2 import *
def modi_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7676266403070976350, 11819]
    tran0.writeAction("movir X16 27271")
    tran0.writeAction("slorii X16 X16 12 2361")
    tran0.writeAction("slorii X16 X16 12 3964")
    tran0.writeAction("slorii X16 X16 12 1274")
    tran0.writeAction("slorii X16 X16 12 350")
    tran0.writeAction("modi X16 X17 11819")
    tran0.writeAction("yieldt")
    return efa
