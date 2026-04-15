from EFA_v2 import *
def modi_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5755531901191086652, 25829]
    tran0.writeAction("movir X16 20447")
    tran0.writeAction("slorii X16 X16 12 3100")
    tran0.writeAction("slorii X16 X16 12 1311")
    tran0.writeAction("slorii X16 X16 12 3782")
    tran0.writeAction("slorii X16 X16 12 572")
    tran0.writeAction("modi X16 X17 25829")
    tran0.writeAction("yieldt")
    return efa
