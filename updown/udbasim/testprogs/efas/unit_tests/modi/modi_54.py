from EFA_v2 import *
def modi_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8270466358480948878, 6076]
    tran0.writeAction("movir X16 29382")
    tran0.writeAction("slorii X16 X16 12 2453")
    tran0.writeAction("slorii X16 X16 12 1424")
    tran0.writeAction("slorii X16 X16 12 308")
    tran0.writeAction("slorii X16 X16 12 3726")
    tran0.writeAction("modi X16 X17 6076")
    tran0.writeAction("yieldt")
    return efa
