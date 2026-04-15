from EFA_v2 import *
def modi_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5004656124232740160, 30203]
    tran0.writeAction("movir X16 47755")
    tran0.writeAction("slorii X16 X16 12 3644")
    tran0.writeAction("slorii X16 X16 12 1364")
    tran0.writeAction("slorii X16 X16 12 509")
    tran0.writeAction("slorii X16 X16 12 704")
    tran0.writeAction("modi X16 X17 30203")
    tran0.writeAction("yieldt")
    return efa
