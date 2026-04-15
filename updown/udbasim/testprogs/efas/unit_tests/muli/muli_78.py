from EFA_v2 import *
def muli_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7646826403220131889, -7014]
    tran0.writeAction("movir X16 27166")
    tran0.writeAction("slorii X16 X16 12 4033")
    tran0.writeAction("slorii X16 X16 12 2399")
    tran0.writeAction("slorii X16 X16 12 57")
    tran0.writeAction("slorii X16 X16 12 49")
    tran0.writeAction("muli X16 X17 -7014")
    tran0.writeAction("yieldt")
    return efa
