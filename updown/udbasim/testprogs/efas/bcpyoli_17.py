from EFA_v2 import *
def bcpyoli_17():
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
    tran0.writeAction("slorii X16 X16 12 8")
    tran0.writeAction("slorii X16 X16 12 1139")
    tran0.writeAction("add X7 X16 X16")
    tran0.writeAction("bcpyoli X14 X16 1")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
