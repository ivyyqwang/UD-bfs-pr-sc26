from EFA_v2 import *
def add_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2730995790274924941, -1470568467527162782]
    tran0.writeAction("movir X16 9702")
    tran0.writeAction("slorii X16 X16 12 1827")
    tran0.writeAction("slorii X16 X16 12 938")
    tran0.writeAction("slorii X16 X16 12 1737")
    tran0.writeAction("slorii X16 X16 12 397")
    tran0.writeAction("movir X17 60311")
    tran0.writeAction("slorii X17 X17 12 2012")
    tran0.writeAction("slorii X17 X17 12 1323")
    tran0.writeAction("slorii X17 X17 12 626")
    tran0.writeAction("slorii X17 X17 12 1122")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
