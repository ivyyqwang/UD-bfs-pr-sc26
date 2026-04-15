from EFA_v2 import *
def add_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1513508928332607630, -7148605250215260212]
    tran0.writeAction("movir X16 60158")
    tran0.writeAction("slorii X16 X16 12 3834")
    tran0.writeAction("slorii X16 X16 12 1546")
    tran0.writeAction("slorii X16 X16 12 1444")
    tran0.writeAction("slorii X16 X16 12 3954")
    tran0.writeAction("movir X17 40139")
    tran0.writeAction("slorii X17 X17 12 214")
    tran0.writeAction("slorii X17 X17 12 1629")
    tran0.writeAction("slorii X17 X17 12 1748")
    tran0.writeAction("slorii X17 X17 12 4044")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
