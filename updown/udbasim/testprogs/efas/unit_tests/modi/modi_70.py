from EFA_v2 import *
def modi_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4023676277656922579, -24509]
    tran0.writeAction("movir X16 51241")
    tran0.writeAction("slorii X16 X16 12 123")
    tran0.writeAction("slorii X16 X16 12 3691")
    tran0.writeAction("slorii X16 X16 12 381")
    tran0.writeAction("slorii X16 X16 12 1581")
    tran0.writeAction("modi X16 X17 -24509")
    tran0.writeAction("yieldt")
    return efa
