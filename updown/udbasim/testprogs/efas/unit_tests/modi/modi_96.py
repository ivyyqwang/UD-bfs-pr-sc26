from EFA_v2 import *
def modi_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2625545536975665586, 32269]
    tran0.writeAction("movir X16 56208")
    tran0.writeAction("slorii X16 X16 12 771")
    tran0.writeAction("slorii X16 X16 12 3758")
    tran0.writeAction("slorii X16 X16 12 3904")
    tran0.writeAction("slorii X16 X16 12 1614")
    tran0.writeAction("modi X16 X17 32269")
    tran0.writeAction("yieldt")
    return efa
