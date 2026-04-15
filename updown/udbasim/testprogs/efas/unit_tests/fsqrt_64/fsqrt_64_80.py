from EFA_v2 import *
def fsqrt_64_80():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15762181590054892428]
    tran0.writeAction("movir X16 55998")
    tran0.writeAction("slorii X16 X16 12 2122")
    tran0.writeAction("slorii X16 X16 12 1280")
    tran0.writeAction("slorii X16 X16 12 1735")
    tran0.writeAction("slorii X16 X16 12 908")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
