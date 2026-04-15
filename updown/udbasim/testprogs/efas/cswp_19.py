from EFA_v2 import *
def cswp_19():
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
    tran0.writeAction("slorii X16 X16 12 7")
    tran0.writeAction("slorii X16 X16 12 1006")
    tran0.writeAction("movir X20 14656")
    tran0.writeAction("slorii X20 X20 12 1238")
    tran0.writeAction("slorii X20 X20 12 3655")
    tran0.writeAction("slorii X20 X20 12 415")
    tran0.writeAction("slorii X20 X20 12 3509")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 45727")
    tran0.writeAction("slorii X18 X18 12 340")
    tran0.writeAction("slorii X18 X18 12 1608")
    tran0.writeAction("slorii X18 X18 12 3201")
    tran0.writeAction("slorii X18 X18 12 3055")
    tran0.writeAction("movir X19 26645")
    tran0.writeAction("slorii X19 X19 12 2275")
    tran0.writeAction("slorii X19 X19 12 973")
    tran0.writeAction("slorii X19 X19 12 662")
    tran0.writeAction("slorii X19 X19 12 3059")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
