from EFA_v2 import *
def cswpi_3():
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
    tran0.writeAction("slorii X16 X16 12 14")
    tran0.writeAction("slorii X16 X16 12 729")
    tran0.writeAction("movir X20 47962")
    tran0.writeAction("slorii X20 X20 12 2681")
    tran0.writeAction("slorii X20 X20 12 1383")
    tran0.writeAction("slorii X20 X20 12 1525")
    tran0.writeAction("slorii X20 X20 12 1903")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("cswpi X16 X17 4 -8")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
