from EFA_v2 import *
def add_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2904016692364481609, -5174401112247792167]
    tran0.writeAction("movir X16 55218")
    tran0.writeAction("slorii X16 X16 12 3523")
    tran0.writeAction("slorii X16 X16 12 1109")
    tran0.writeAction("slorii X16 X16 12 3318")
    tran0.writeAction("slorii X16 X16 12 2999")
    tran0.writeAction("movir X17 47152")
    tran0.writeAction("slorii X17 X17 12 3417")
    tran0.writeAction("slorii X17 X17 12 2691")
    tran0.writeAction("slorii X17 X17 12 344")
    tran0.writeAction("slorii X17 X17 12 3545")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
