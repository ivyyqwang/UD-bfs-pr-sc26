from EFA_v2 import *
def fcnvt_i64_64_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4816234020511844235]
    tran0.writeAction("movir X16 17110")
    tran0.writeAction("slorii X16 X16 12 2869")
    tran0.writeAction("slorii X16 X16 12 763")
    tran0.writeAction("slorii X16 X16 12 3112")
    tran0.writeAction("slorii X16 X16 12 1931")
    tran0.writeAction("fcnvt.i64.64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
