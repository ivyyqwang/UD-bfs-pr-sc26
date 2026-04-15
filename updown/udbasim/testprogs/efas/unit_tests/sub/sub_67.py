from EFA_v2 import *
def sub_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2657247285301848011, -8017206213704271410]
    tran0.writeAction("movir X16 56095")
    tran0.writeAction("slorii X16 X16 12 2298")
    tran0.writeAction("slorii X16 X16 12 3127")
    tran0.writeAction("slorii X16 X16 12 869")
    tran0.writeAction("slorii X16 X16 12 2101")
    tran0.writeAction("movir X17 37053")
    tran0.writeAction("slorii X17 X17 12 662")
    tran0.writeAction("slorii X17 X17 12 3317")
    tran0.writeAction("slorii X17 X17 12 419")
    tran0.writeAction("slorii X17 X17 12 2510")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
