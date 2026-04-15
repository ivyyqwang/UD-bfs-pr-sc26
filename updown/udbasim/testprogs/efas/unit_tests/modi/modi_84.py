from EFA_v2 import *
def modi_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1363999039742557565, 30982]
    tran0.writeAction("movir X16 60690")
    tran0.writeAction("slorii X16 X16 12 417")
    tran0.writeAction("slorii X16 X16 12 2466")
    tran0.writeAction("slorii X16 X16 12 700")
    tran0.writeAction("slorii X16 X16 12 643")
    tran0.writeAction("modi X16 X17 30982")
    tran0.writeAction("yieldt")
    return efa
