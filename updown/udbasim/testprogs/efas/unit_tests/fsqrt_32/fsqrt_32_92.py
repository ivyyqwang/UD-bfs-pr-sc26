from EFA_v2 import *
def fsqrt_32_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [401275231]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 23")
    tran0.writeAction("slorii X16 X16 12 3759")
    tran0.writeAction("slorii X16 X16 12 2399")
    tran0.writeAction("fsqrt.32 X16 X17")
    tran0.writeAction("yieldt")
    return efa
