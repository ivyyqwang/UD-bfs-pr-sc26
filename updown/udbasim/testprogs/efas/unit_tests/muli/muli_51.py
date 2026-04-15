from EFA_v2 import *
def muli_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-284721485668758671, 14519]
    tran0.writeAction("movir X16 64524")
    tran0.writeAction("slorii X16 X16 12 1909")
    tran0.writeAction("slorii X16 X16 12 314")
    tran0.writeAction("slorii X16 X16 12 3244")
    tran0.writeAction("slorii X16 X16 12 2929")
    tran0.writeAction("muli X16 X17 14519")
    tran0.writeAction("yieldt")
    return efa
