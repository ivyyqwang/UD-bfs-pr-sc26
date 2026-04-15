from EFA_v2 import *
def modi_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6062328239160385096, 5946]
    tran0.writeAction("movir X16 21537")
    tran0.writeAction("slorii X16 X16 12 2934")
    tran0.writeAction("slorii X16 X16 12 2550")
    tran0.writeAction("slorii X16 X16 12 3989")
    tran0.writeAction("slorii X16 X16 12 3656")
    tran0.writeAction("modi X16 X17 5946")
    tran0.writeAction("yieldt")
    return efa
