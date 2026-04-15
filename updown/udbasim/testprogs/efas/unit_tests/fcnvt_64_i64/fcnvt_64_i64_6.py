from EFA_v2 import *
def fcnvt_64_i64_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15597768238615896086]
    tran0.writeAction("movir X16 55414")
    tran0.writeAction("slorii X16 X16 12 1657")
    tran0.writeAction("slorii X16 X16 12 655")
    tran0.writeAction("slorii X16 X16 12 2338")
    tran0.writeAction("slorii X16 X16 12 22")
    tran0.writeAction("fcnvt.64.i64 X16 X16")
    tran0.writeAction("yieldt")
    return efa
