from EFA_v2 import *
def add_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [23357974634885182, 6049312137965517613]
    tran0.writeAction("movir X16 82")
    tran0.writeAction("slorii X16 X16 12 4031")
    tran0.writeAction("slorii X16 X16 12 1092")
    tran0.writeAction("slorii X16 X16 12 3215")
    tran0.writeAction("slorii X16 X16 12 62")
    tran0.writeAction("movir X17 21491")
    tran0.writeAction("slorii X17 X17 12 1941")
    tran0.writeAction("slorii X17 X17 12 1726")
    tran0.writeAction("slorii X17 X17 12 3659")
    tran0.writeAction("slorii X17 X17 12 2861")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
