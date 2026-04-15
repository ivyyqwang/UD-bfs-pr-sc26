from EFA_v2 import *
def fcnvt_i64_64_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1323307490033802814]
    tran0.writeAction("movir X16 60834")
    tran0.writeAction("slorii X16 X16 12 2733")
    tran0.writeAction("slorii X16 X16 12 2391")
    tran0.writeAction("slorii X16 X16 12 3774")
    tran0.writeAction("slorii X16 X16 12 450")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
