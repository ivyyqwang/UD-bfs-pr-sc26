from EFA_v2 import *
def add_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-644456219747958161, 5291865016994969587]
    tran0.writeAction("movir X16 63246")
    tran0.writeAction("slorii X16 X16 12 1767")
    tran0.writeAction("slorii X16 X16 12 2956")
    tran0.writeAction("slorii X16 X16 12 2588")
    tran0.writeAction("slorii X16 X16 12 623")
    tran0.writeAction("movir X17 18800")
    tran0.writeAction("slorii X17 X17 12 1971")
    tran0.writeAction("slorii X17 X17 12 521")
    tran0.writeAction("slorii X17 X17 12 1235")
    tran0.writeAction("slorii X17 X17 12 2035")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
