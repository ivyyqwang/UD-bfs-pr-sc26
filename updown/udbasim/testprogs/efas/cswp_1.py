from EFA_v2 import *
def cswp_1():
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
    tran0.writeAction("slorii X16 X16 12 2")
    tran0.writeAction("slorii X16 X16 12 2888")
    tran0.writeAction("movir X20 49463")
    tran0.writeAction("slorii X20 X20 12 1212")
    tran0.writeAction("slorii X20 X20 12 1350")
    tran0.writeAction("slorii X20 X20 12 1134")
    tran0.writeAction("slorii X20 X20 12 588")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 19948")
    tran0.writeAction("slorii X18 X18 12 2219")
    tran0.writeAction("slorii X18 X18 12 3910")
    tran0.writeAction("slorii X18 X18 12 1916")
    tran0.writeAction("slorii X18 X18 12 2689")
    tran0.writeAction("movir X19 9923")
    tran0.writeAction("slorii X19 X19 12 762")
    tran0.writeAction("slorii X19 X19 12 155")
    tran0.writeAction("slorii X19 X19 12 159")
    tran0.writeAction("slorii X19 X19 12 2432")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
