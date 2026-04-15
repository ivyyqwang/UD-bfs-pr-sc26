from EFA_v2 import *
def add_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5629472423644026060, -2772786482619241104]
    tran0.writeAction("movir X16 19999")
    tran0.writeAction("slorii X16 X16 12 3701")
    tran0.writeAction("slorii X16 X16 12 2004")
    tran0.writeAction("slorii X16 X16 12 653")
    tran0.writeAction("slorii X16 X16 12 1228")
    tran0.writeAction("movir X17 55685")
    tran0.writeAction("slorii X17 X17 12 342")
    tran0.writeAction("slorii X17 X17 12 649")
    tran0.writeAction("slorii X17 X17 12 1946")
    tran0.writeAction("slorii X17 X17 12 3440")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
