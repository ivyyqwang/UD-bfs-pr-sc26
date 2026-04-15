from EFA_v2 import *
def cswp_8():
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
    tran0.writeAction("slorii X16 X16 12 1")
    tran0.writeAction("slorii X16 X16 12 2127")
    tran0.writeAction("movir X20 34367")
    tran0.writeAction("slorii X20 X20 12 3026")
    tran0.writeAction("slorii X20 X20 12 2771")
    tran0.writeAction("slorii X20 X20 12 1993")
    tran0.writeAction("slorii X20 X20 12 694")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 30653")
    tran0.writeAction("slorii X18 X18 12 1338")
    tran0.writeAction("slorii X18 X18 12 2514")
    tran0.writeAction("slorii X18 X18 12 267")
    tran0.writeAction("slorii X18 X18 12 435")
    tran0.writeAction("movir X19 22702")
    tran0.writeAction("slorii X19 X19 12 3360")
    tran0.writeAction("slorii X19 X19 12 1942")
    tran0.writeAction("slorii X19 X19 12 77")
    tran0.writeAction("slorii X19 X19 12 1690")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
