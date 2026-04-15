from EFA_v2 import *
def modi_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6781649218726043331, -30977]
    tran0.writeAction("movir X16 24093")
    tran0.writeAction("slorii X16 X16 12 1056")
    tran0.writeAction("slorii X16 X16 12 2209")
    tran0.writeAction("slorii X16 X16 12 1929")
    tran0.writeAction("slorii X16 X16 12 3779")
    tran0.writeAction("modi X16 X17 -30977")
    tran0.writeAction("yieldt")
    return efa
