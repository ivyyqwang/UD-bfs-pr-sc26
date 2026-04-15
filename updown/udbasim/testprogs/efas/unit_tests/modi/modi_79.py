from EFA_v2 import *
def modi_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6256837982650264566, 16039]
    tran0.writeAction("movir X16 22228")
    tran0.writeAction("slorii X16 X16 12 3087")
    tran0.writeAction("slorii X16 X16 12 3773")
    tran0.writeAction("slorii X16 X16 12 166")
    tran0.writeAction("slorii X16 X16 12 3062")
    tran0.writeAction("modi X16 X17 16039")
    tran0.writeAction("yieldt")
    return efa
