from EFA_v2 import *
def fsqrt_64_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [360027569033479017]
    tran0.writeAction("movir X16 1279")
    tran0.writeAction("slorii X16 X16 12 306")
    tran0.writeAction("slorii X16 X16 12 2721")
    tran0.writeAction("slorii X16 X16 12 2408")
    tran0.writeAction("slorii X16 X16 12 873")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
