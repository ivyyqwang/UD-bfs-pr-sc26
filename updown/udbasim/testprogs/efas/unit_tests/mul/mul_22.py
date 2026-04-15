from EFA_v2 import *
def mul_22():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [238134488010918603, -6343187779886033022]
    tran0.writeAction("movir X16 846")
    tran0.writeAction("slorii X16 X16 12 96")
    tran0.writeAction("slorii X16 X16 12 3614")
    tran0.writeAction("slorii X16 X16 12 2704")
    tran0.writeAction("slorii X16 X16 12 2763")
    tran0.writeAction("movir X17 43000")
    tran0.writeAction("slorii X17 X17 12 1925")
    tran0.writeAction("slorii X17 X17 12 612")
    tran0.writeAction("slorii X17 X17 12 1205")
    tran0.writeAction("slorii X17 X17 12 1922")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
