from EFA_v2 import *
def cswp_16():
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
    tran0.writeAction("slorii X16 X16 12 3")
    tran0.writeAction("slorii X16 X16 12 1557")
    tran0.writeAction("movir X20 36455")
    tran0.writeAction("slorii X20 X20 12 3298")
    tran0.writeAction("slorii X20 X20 12 3830")
    tran0.writeAction("slorii X20 X20 12 14")
    tran0.writeAction("slorii X20 X20 12 2836")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 23044")
    tran0.writeAction("slorii X18 X18 12 3013")
    tran0.writeAction("slorii X18 X18 12 1937")
    tran0.writeAction("slorii X18 X18 12 243")
    tran0.writeAction("slorii X18 X18 12 3763")
    tran0.writeAction("movir X19 6484")
    tran0.writeAction("slorii X19 X19 12 2841")
    tran0.writeAction("slorii X19 X19 12 718")
    tran0.writeAction("slorii X19 X19 12 1637")
    tran0.writeAction("slorii X19 X19 12 3844")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
