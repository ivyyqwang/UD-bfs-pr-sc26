from EFA_v2 import *
def fcnvt_64_i64_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12307901368468070183]
    tran0.writeAction("movir X16 43726")
    tran0.writeAction("slorii X16 X16 12 1841")
    tran0.writeAction("slorii X16 X16 12 1446")
    tran0.writeAction("slorii X16 X16 12 341")
    tran0.writeAction("slorii X16 X16 12 3879")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
