from EFA_v2 import *
def fsqrt_64_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11301256159624885589]
    tran0.writeAction("movir X16 40150")
    tran0.writeAction("slorii X16 X16 12 521")
    tran0.writeAction("slorii X16 X16 12 2494")
    tran0.writeAction("slorii X16 X16 12 559")
    tran0.writeAction("slorii X16 X16 12 1365")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
