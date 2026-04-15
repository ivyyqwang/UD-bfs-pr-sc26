from EFA_v2 import *
def fsqrt_64_58():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11208217159719922462]
    tran0.writeAction("movir X16 39819")
    tran0.writeAction("slorii X16 X16 12 2401")
    tran0.writeAction("slorii X16 X16 12 3970")
    tran0.writeAction("slorii X16 X16 12 2226")
    tran0.writeAction("slorii X16 X16 12 2846")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
