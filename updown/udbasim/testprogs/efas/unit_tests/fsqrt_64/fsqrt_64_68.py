from EFA_v2 import *
def fsqrt_64_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11401199716979237664]
    tran0.writeAction("movir X16 40505")
    tran0.writeAction("slorii X16 X16 12 811")
    tran0.writeAction("slorii X16 X16 12 3207")
    tran0.writeAction("slorii X16 X16 12 3406")
    tran0.writeAction("slorii X16 X16 12 800")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
