from EFA_v2 import *
def modi_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4882323429119366674, -32477]
    tran0.writeAction("movir X16 48190")
    tran0.writeAction("slorii X16 X16 12 2059")
    tran0.writeAction("slorii X16 X16 12 1400")
    tran0.writeAction("slorii X16 X16 12 3166")
    tran0.writeAction("slorii X16 X16 12 2542")
    tran0.writeAction("modi X16 X17 -32477")
    tran0.writeAction("yieldt")
    return efa
