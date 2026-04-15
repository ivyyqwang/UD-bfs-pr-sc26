from EFA_v2 import *
def cswp_5():
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
    tran0.writeAction("slorii X16 X16 12 769")
    tran0.writeAction("movir X20 4901")
    tran0.writeAction("slorii X20 X20 12 4045")
    tran0.writeAction("slorii X20 X20 12 3386")
    tran0.writeAction("slorii X20 X20 12 176")
    tran0.writeAction("slorii X20 X20 12 1439")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 54556")
    tran0.writeAction("slorii X18 X18 12 3733")
    tran0.writeAction("slorii X18 X18 12 3766")
    tran0.writeAction("slorii X18 X18 12 2814")
    tran0.writeAction("slorii X18 X18 12 2669")
    tran0.writeAction("movir X19 42576")
    tran0.writeAction("slorii X19 X19 12 1581")
    tran0.writeAction("slorii X19 X19 12 2121")
    tran0.writeAction("slorii X19 X19 12 3340")
    tran0.writeAction("slorii X19 X19 12 505")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
