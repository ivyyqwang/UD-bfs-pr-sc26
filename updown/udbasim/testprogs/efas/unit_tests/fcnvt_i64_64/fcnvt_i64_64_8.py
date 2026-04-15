from EFA_v2 import *
def fcnvt_i64_64_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7433077871198848409]
    tran0.writeAction("movir X16 26407")
    tran0.writeAction("slorii X16 X16 12 2447")
    tran0.writeAction("slorii X16 X16 12 276")
    tran0.writeAction("slorii X16 X16 12 2556")
    tran0.writeAction("slorii X16 X16 12 1433")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
