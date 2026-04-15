from EFA_v2 import *
def fsqrt_64_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5207944867927310650]
    tran0.writeAction("movir X16 18502")
    tran0.writeAction("slorii X16 X16 12 1380")
    tran0.writeAction("slorii X16 X16 12 950")
    tran0.writeAction("slorii X16 X16 12 2564")
    tran0.writeAction("slorii X16 X16 12 314")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
