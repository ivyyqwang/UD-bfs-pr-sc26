from EFA_v2 import *
def add_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9072858545661036866, 4943802903473807506]
    tran0.writeAction("movir X16 32233")
    tran0.writeAction("slorii X16 X16 12 1100")
    tran0.writeAction("slorii X16 X16 12 1783")
    tran0.writeAction("slorii X16 X16 12 2020")
    tran0.writeAction("slorii X16 X16 12 2370")
    tran0.writeAction("movir X17 17563")
    tran0.writeAction("slorii X17 X17 12 3752")
    tran0.writeAction("slorii X17 X17 12 3101")
    tran0.writeAction("slorii X17 X17 12 414")
    tran0.writeAction("slorii X17 X17 12 146")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
