from EFA_v2 import *
def fcnvt_64_i64_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17040938390739478546]
    tran0.writeAction("movir X16 60541")
    tran0.writeAction("slorii X16 X16 12 2354")
    tran0.writeAction("slorii X16 X16 12 3579")
    tran0.writeAction("slorii X16 X16 12 1406")
    tran0.writeAction("slorii X16 X16 12 2066")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
