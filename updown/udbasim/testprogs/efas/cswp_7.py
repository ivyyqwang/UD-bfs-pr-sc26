from EFA_v2 import *
def cswp_7():
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
    tran0.writeAction("slorii X16 X16 12 9")
    tran0.writeAction("slorii X16 X16 12 1893")
    tran0.writeAction("movir X20 40421")
    tran0.writeAction("slorii X20 X20 12 3472")
    tran0.writeAction("slorii X20 X20 12 1619")
    tran0.writeAction("slorii X20 X20 12 163")
    tran0.writeAction("slorii X20 X20 12 2835")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 40421")
    tran0.writeAction("slorii X18 X18 12 3472")
    tran0.writeAction("slorii X18 X18 12 1619")
    tran0.writeAction("slorii X18 X18 12 163")
    tran0.writeAction("slorii X18 X18 12 2835")
    tran0.writeAction("movir X19 53568")
    tran0.writeAction("slorii X19 X19 12 1398")
    tran0.writeAction("slorii X19 X19 12 875")
    tran0.writeAction("slorii X19 X19 12 2631")
    tran0.writeAction("slorii X19 X19 12 2488")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
