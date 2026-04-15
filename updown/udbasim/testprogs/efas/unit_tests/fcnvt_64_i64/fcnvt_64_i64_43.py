from EFA_v2 import *
def fcnvt_64_i64_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7247456774608369173]
    tran0.writeAction("movir X16 25748")
    tran0.writeAction("slorii X16 X16 12 568")
    tran0.writeAction("slorii X16 X16 12 2479")
    tran0.writeAction("slorii X16 X16 12 2171")
    tran0.writeAction("slorii X16 X16 12 1557")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
