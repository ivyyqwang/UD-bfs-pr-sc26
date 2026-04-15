from EFA_v2 import *
def fcnvt_i64_64_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1890019927656577260]
    tran0.writeAction("movir X16 6714")
    tran0.writeAction("slorii X16 X16 12 2865")
    tran0.writeAction("slorii X16 X16 12 3142")
    tran0.writeAction("slorii X16 X16 12 1555")
    tran0.writeAction("slorii X16 X16 12 2284")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
