from EFA_v2 import *
def add_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4322022607865236407, -6688551888633550151]
    tran0.writeAction("movir X16 15354")
    tran0.writeAction("slorii X16 X16 12 3722")
    tran0.writeAction("slorii X16 X16 12 2477")
    tran0.writeAction("slorii X16 X16 12 60")
    tran0.writeAction("slorii X16 X16 12 2999")
    tran0.writeAction("movir X17 41773")
    tran0.writeAction("slorii X17 X17 12 2007")
    tran0.writeAction("slorii X17 X17 12 3752")
    tran0.writeAction("slorii X17 X17 12 938")
    tran0.writeAction("slorii X17 X17 12 2745")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
