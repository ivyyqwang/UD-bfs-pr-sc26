from EFA_v2 import *
def fcnvt_i64_64_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2424940761673094641]
    tran0.writeAction("movir X16 56920")
    tran0.writeAction("slorii X16 X16 12 3603")
    tran0.writeAction("slorii X16 X16 12 2467")
    tran0.writeAction("slorii X16 X16 12 450")
    tran0.writeAction("slorii X16 X16 12 2575")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
