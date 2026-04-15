from EFA_v2 import *
def fcnvt_i64_64_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3671782953439171314]
    tran0.writeAction("movir X16 52491")
    tran0.writeAction("slorii X16 X16 12 845")
    tran0.writeAction("slorii X16 X16 12 2967")
    tran0.writeAction("slorii X16 X16 12 3782")
    tran0.writeAction("slorii X16 X16 12 3342")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
