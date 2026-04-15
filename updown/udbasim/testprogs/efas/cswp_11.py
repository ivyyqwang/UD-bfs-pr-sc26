from EFA_v2 import *
def cswp_11():
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
    tran0.writeAction("slorii X16 X16 12 13")
    tran0.writeAction("slorii X16 X16 12 994")
    tran0.writeAction("movir X20 25147")
    tran0.writeAction("slorii X20 X20 12 11")
    tran0.writeAction("slorii X20 X20 12 618")
    tran0.writeAction("slorii X20 X20 12 2693")
    tran0.writeAction("slorii X20 X20 12 50")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 14930")
    tran0.writeAction("slorii X18 X18 12 1960")
    tran0.writeAction("slorii X18 X18 12 3126")
    tran0.writeAction("slorii X18 X18 12 1890")
    tran0.writeAction("slorii X18 X18 12 327")
    tran0.writeAction("movir X19 24215")
    tran0.writeAction("slorii X19 X19 12 1170")
    tran0.writeAction("slorii X19 X19 12 2903")
    tran0.writeAction("slorii X19 X19 12 1673")
    tran0.writeAction("slorii X19 X19 12 1514")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
