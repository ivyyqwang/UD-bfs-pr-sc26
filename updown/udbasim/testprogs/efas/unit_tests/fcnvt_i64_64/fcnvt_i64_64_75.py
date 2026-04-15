from EFA_v2 import *
def fcnvt_i64_64_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5471591684049908038]
    tran0.writeAction("movir X16 46097")
    tran0.writeAction("slorii X16 X16 12 5")
    tran0.writeAction("slorii X16 X16 12 2660")
    tran0.writeAction("slorii X16 X16 12 916")
    tran0.writeAction("slorii X16 X16 12 3770")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
