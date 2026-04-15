from EFA_v2 import *
def modi_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5378627917491171577, 24545]
    tran0.writeAction("movir X16 19108")
    tran0.writeAction("slorii X16 X16 12 2969")
    tran0.writeAction("slorii X16 X16 12 2049")
    tran0.writeAction("slorii X16 X16 12 247")
    tran0.writeAction("slorii X16 X16 12 249")
    tran0.writeAction("modi X16 X17 24545")
    tran0.writeAction("yieldt")
    return efa
