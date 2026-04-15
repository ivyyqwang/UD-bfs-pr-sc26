from EFA_v2 import *
def mul_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2269657571092720242, -4603759118173568756]
    tran0.writeAction("movir X16 8063")
    tran0.writeAction("slorii X16 X16 12 1816")
    tran0.writeAction("slorii X16 X16 12 2342")
    tran0.writeAction("slorii X16 X16 12 3102")
    tran0.writeAction("slorii X16 X16 12 2674")
    tran0.writeAction("movir X17 49180")
    tran0.writeAction("slorii X17 X17 12 663")
    tran0.writeAction("slorii X17 X17 12 2377")
    tran0.writeAction("slorii X17 X17 12 3272")
    tran0.writeAction("slorii X17 X17 12 268")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
