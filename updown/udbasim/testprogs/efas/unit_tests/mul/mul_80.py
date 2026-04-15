from EFA_v2 import *
def mul_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4879236757223086348, 6983701597043039977]
    tran0.writeAction("movir X16 17334")
    tran0.writeAction("slorii X16 X16 12 2175")
    tran0.writeAction("slorii X16 X16 12 2745")
    tran0.writeAction("slorii X16 X16 12 1273")
    tran0.writeAction("slorii X16 X16 12 2316")
    tran0.writeAction("movir X17 24811")
    tran0.writeAction("slorii X17 X17 12 377")
    tran0.writeAction("slorii X17 X17 12 2541")
    tran0.writeAction("slorii X17 X17 12 321")
    tran0.writeAction("slorii X17 X17 12 3817")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
