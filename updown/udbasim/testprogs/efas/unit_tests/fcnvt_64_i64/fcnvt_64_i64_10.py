from EFA_v2 import *
def fcnvt_64_i64_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16171451581184476377]
    tran0.writeAction("movir X16 57452")
    tran0.writeAction("slorii X16 X16 12 2200")
    tran0.writeAction("slorii X16 X16 12 2166")
    tran0.writeAction("slorii X16 X16 12 3808")
    tran0.writeAction("slorii X16 X16 12 1241")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
