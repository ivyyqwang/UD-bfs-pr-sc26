from EFA_v2 import *
def modi_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3996218630623546089, -1772]
    tran0.writeAction("movir X16 51338")
    tran0.writeAction("slorii X16 X16 12 2373")
    tran0.writeAction("slorii X16 X16 12 1036")
    tran0.writeAction("slorii X16 X16 12 3627")
    tran0.writeAction("slorii X16 X16 12 1303")
    tran0.writeAction("modi X16 X17 -1772")
    tran0.writeAction("yieldt")
    return efa
