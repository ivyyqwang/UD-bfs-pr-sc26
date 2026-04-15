from EFA_v2 import *
def sub_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3370046711933893895, -356291893732698236]
    tran0.writeAction("movir X16 11972")
    tran0.writeAction("slorii X16 X16 12 3322")
    tran0.writeAction("slorii X16 X16 12 277")
    tran0.writeAction("slorii X16 X16 12 1199")
    tran0.writeAction("slorii X16 X16 12 3335")
    tran0.writeAction("movir X17 64270")
    tran0.writeAction("slorii X17 X17 12 806")
    tran0.writeAction("slorii X17 X17 12 2317")
    tran0.writeAction("slorii X17 X17 12 2913")
    tran0.writeAction("slorii X17 X17 12 1924")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
