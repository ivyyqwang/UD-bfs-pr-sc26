from EFA_v2 import *
def cswp_12():
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
    tran0.writeAction("slorii X16 X16 12 4")
    tran0.writeAction("slorii X16 X16 12 1394")
    tran0.writeAction("movir X20 4434")
    tran0.writeAction("slorii X20 X20 12 2390")
    tran0.writeAction("slorii X20 X20 12 3901")
    tran0.writeAction("slorii X20 X20 12 2258")
    tran0.writeAction("slorii X20 X20 12 1939")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 17523")
    tran0.writeAction("slorii X18 X18 12 2362")
    tran0.writeAction("slorii X18 X18 12 3430")
    tran0.writeAction("slorii X18 X18 12 4077")
    tran0.writeAction("slorii X18 X18 12 2385")
    tran0.writeAction("movir X19 13065")
    tran0.writeAction("slorii X19 X19 12 762")
    tran0.writeAction("slorii X19 X19 12 1294")
    tran0.writeAction("slorii X19 X19 12 993")
    tran0.writeAction("slorii X19 X19 12 1449")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
