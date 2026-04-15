from EFA_v2 import *
def modi_100():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1930970866267723176, 0]
    tran0.writeAction("movir X16 58675")
    tran0.writeAction("slorii X16 X16 12 3331")
    tran0.writeAction("slorii X16 X16 12 2644")
    tran0.writeAction("slorii X16 X16 12 1982")
    tran0.writeAction("slorii X16 X16 12 2648")
    tran0.writeAction("modi X16 X17 0")
    tran0.writeAction("addi X7 X18 0")
    tran0.writeAction("movrl X4 0(X18) 0 8")
    tran0.writeAction("yieldt")
    return efa
