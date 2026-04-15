from EFA_v2 import *
def cswp_2():
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
    tran0.writeAction("slorii X16 X16 12 3210")
    tran0.writeAction("movir X20 57485")
    tran0.writeAction("slorii X20 X20 12 1564")
    tran0.writeAction("slorii X20 X20 12 1848")
    tran0.writeAction("slorii X20 X20 12 2869")
    tran0.writeAction("slorii X20 X20 12 172")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 3738")
    tran0.writeAction("slorii X18 X18 12 2351")
    tran0.writeAction("slorii X18 X18 12 2355")
    tran0.writeAction("slorii X18 X18 12 2309")
    tran0.writeAction("slorii X18 X18 12 2376")
    tran0.writeAction("movir X19 16262")
    tran0.writeAction("slorii X19 X19 12 1147")
    tran0.writeAction("slorii X19 X19 12 109")
    tran0.writeAction("slorii X19 X19 12 1336")
    tran0.writeAction("slorii X19 X19 12 483")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
