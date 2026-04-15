from EFA_v2 import *
def modi_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1107349869766185539, 14982]
    tran0.writeAction("movir X16 61601")
    tran0.writeAction("slorii X16 X16 12 3698")
    tran0.writeAction("slorii X16 X16 12 2322")
    tran0.writeAction("slorii X16 X16 12 2094")
    tran0.writeAction("slorii X16 X16 12 3517")
    tran0.writeAction("modi X16 X17 14982")
    tran0.writeAction("yieldt")
    return efa
