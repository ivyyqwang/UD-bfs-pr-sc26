from EFA_v2 import *
def bcpyoli_6():
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
    tran0.writeAction("slorii X16 X16 12 1949")
    tran0.writeAction("add X7 X16 X16")
    tran0.writeAction("bcpyoli X10 X16 1")
    tran0.writeAction("sub X16 X7 X16")
    tran0.writeAction("yieldt")
    return efa
