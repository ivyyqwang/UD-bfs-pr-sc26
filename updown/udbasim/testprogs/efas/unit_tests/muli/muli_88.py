from EFA_v2 import *
def muli_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5662373565486472059, -21822]
    tran0.writeAction("movir X16 20116")
    tran0.writeAction("slorii X16 X16 12 3244")
    tran0.writeAction("slorii X16 X16 12 476")
    tran0.writeAction("slorii X16 X16 12 1569")
    tran0.writeAction("slorii X16 X16 12 2939")
    tran0.writeAction("muli X16 X17 -21822")
    tran0.writeAction("yieldt")
    return efa
