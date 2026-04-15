from EFA_v2 import *
def mul_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-810326972407866237, -3360739813266110964]
    tran0.writeAction("movir X16 62657")
    tran0.writeAction("slorii X16 X16 12 574")
    tran0.writeAction("slorii X16 X16 12 2417")
    tran0.writeAction("slorii X16 X16 12 2913")
    tran0.writeAction("slorii X16 X16 12 3203")
    tran0.writeAction("movir X17 53596")
    tran0.writeAction("slorii X17 X17 12 1039")
    tran0.writeAction("slorii X17 X17 12 543")
    tran0.writeAction("slorii X17 X17 12 3116")
    tran0.writeAction("slorii X17 X17 12 1548")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
