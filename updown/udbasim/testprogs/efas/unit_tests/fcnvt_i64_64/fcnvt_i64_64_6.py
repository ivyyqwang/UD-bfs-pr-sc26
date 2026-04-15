from EFA_v2 import *
def fcnvt_i64_64_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7790725558643047847]
    tran0.writeAction("movir X16 37857")
    tran0.writeAction("slorii X16 X16 12 3206")
    tran0.writeAction("slorii X16 X16 12 422")
    tran0.writeAction("slorii X16 X16 12 2148")
    tran0.writeAction("slorii X16 X16 12 601")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
