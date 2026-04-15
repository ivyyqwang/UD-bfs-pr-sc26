from EFA_v2 import *
def fcnvt_i64_64_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7736646317750177613]
    tran0.writeAction("movir X16 27486")
    tran0.writeAction("slorii X16 X16 12 365")
    tran0.writeAction("slorii X16 X16 12 1506")
    tran0.writeAction("slorii X16 X16 12 1364")
    tran0.writeAction("slorii X16 X16 12 3917")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
