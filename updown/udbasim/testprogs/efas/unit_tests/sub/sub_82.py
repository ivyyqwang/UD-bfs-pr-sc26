from EFA_v2 import *
def sub_82():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2711927275399115409, 4179739195417167352]
    tran0.writeAction("movir X16 55901")
    tran0.writeAction("slorii X16 X16 12 1224")
    tran0.writeAction("slorii X16 X16 12 749")
    tran0.writeAction("slorii X16 X16 12 584")
    tran0.writeAction("slorii X16 X16 12 3439")
    tran0.writeAction("movir X17 14849")
    tran0.writeAction("slorii X17 X17 12 1706")
    tran0.writeAction("slorii X17 X17 12 1836")
    tran0.writeAction("slorii X17 X17 12 2528")
    tran0.writeAction("slorii X17 X17 12 1528")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
