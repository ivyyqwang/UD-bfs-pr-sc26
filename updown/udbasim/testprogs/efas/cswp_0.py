from EFA_v2 import *
def cswp_0():
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
    tran0.writeAction("slorii X16 X16 12 14")
    tran0.writeAction("slorii X16 X16 12 1429")
    tran0.writeAction("movir X20 51958")
    tran0.writeAction("slorii X20 X20 12 3401")
    tran0.writeAction("slorii X20 X20 12 733")
    tran0.writeAction("slorii X20 X20 12 3860")
    tran0.writeAction("slorii X20 X20 12 1517")
    tran0.writeAction("add X16 X7 X16")
    tran0.writeAction("movrl X20 0(X16) 0 8")
    tran0.writeAction("movir X18 51958")
    tran0.writeAction("slorii X18 X18 12 3401")
    tran0.writeAction("slorii X18 X18 12 733")
    tran0.writeAction("slorii X18 X18 12 3860")
    tran0.writeAction("slorii X18 X18 12 1517")
    tran0.writeAction("movir X19 42713")
    tran0.writeAction("slorii X19 X19 12 1280")
    tran0.writeAction("slorii X19 X19 12 1058")
    tran0.writeAction("slorii X19 X19 12 1190")
    tran0.writeAction("slorii X19 X19 12 3918")
    tran0.writeAction("cswp X16 X17 X18 X19")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
