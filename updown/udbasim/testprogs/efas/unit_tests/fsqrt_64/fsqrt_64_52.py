from EFA_v2 import *
def fsqrt_64_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16271199889792815969]
    tran0.writeAction("movir X16 57806")
    tran0.writeAction("slorii X16 X16 12 3745")
    tran0.writeAction("slorii X16 X16 12 1884")
    tran0.writeAction("slorii X16 X16 12 1949")
    tran0.writeAction("slorii X16 X16 12 865")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
