from EFA_v2 import *
def modi_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3019669646873180403, -28099]
    tran0.writeAction("movir X16 54807")
    tran0.writeAction("slorii X16 X16 12 4007")
    tran0.writeAction("slorii X16 X16 12 1151")
    tran0.writeAction("slorii X16 X16 12 388")
    tran0.writeAction("slorii X16 X16 12 1805")
    tran0.writeAction("modi X16 X17 -28099")
    tran0.writeAction("yieldt")
    return efa
