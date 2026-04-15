from EFA_v2 import *
def cswpi_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 11")
    tran0.writeAction("slorii X16 X16 12 240")
    tran0.writeAction("movir X20 0")
    tran0.writeAction("slorii X20 X20 12 0")
    tran0.writeAction("slorii X20 X20 12 0")
    tran0.writeAction("slorii X20 X20 12 0")
    tran0.writeAction("slorii X20 X20 12 5")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("cswpi X16 X17 5 -1")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
