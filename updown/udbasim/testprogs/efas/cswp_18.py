from EFA_v2 import *
def cswp_18():
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
    tran0.writeAction("slorii X16 X16 12 243")
    tran0.writeAction("movir X20 25959")
    tran0.writeAction("slorii X20 X20 12 103")
    tran0.writeAction("slorii X20 X20 12 1991")
    tran0.writeAction("slorii X20 X20 12 30")
    tran0.writeAction("slorii X20 X20 12 1509")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 63947")
    tran0.writeAction("slorii X18 X18 12 736")
    tran0.writeAction("slorii X18 X18 12 2733")
    tran0.writeAction("slorii X18 X18 12 2984")
    tran0.writeAction("slorii X18 X18 12 4015")
    tran0.writeAction("movir X19 43175")
    tran0.writeAction("slorii X19 X19 12 3286")
    tran0.writeAction("slorii X19 X19 12 61")
    tran0.writeAction("slorii X19 X19 12 3395")
    tran0.writeAction("slorii X19 X19 12 2582")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
