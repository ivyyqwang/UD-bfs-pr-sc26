from EFA_v2 import *
def add_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2707605030218973024, -45455003969203470]
    tran0.writeAction("movir X16 9619")
    tran0.writeAction("slorii X16 X16 12 1414")
    tran0.writeAction("slorii X16 X16 12 3570")
    tran0.writeAction("slorii X16 X16 12 1075")
    tran0.writeAction("slorii X16 X16 12 3936")
    tran0.writeAction("movir X17 65374")
    tran0.writeAction("slorii X17 X17 12 2094")
    tran0.writeAction("slorii X17 X17 12 2603")
    tran0.writeAction("slorii X17 X17 12 621")
    tran0.writeAction("slorii X17 X17 12 754")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
