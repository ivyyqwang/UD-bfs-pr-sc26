from EFA_v2 import *
def fsqrt_64_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [15667515056488764115]
    tran0.writeAction("movir X16 55662")
    tran0.writeAction("slorii X16 X16 12 798")
    tran0.writeAction("slorii X16 X16 12 3855")
    tran0.writeAction("slorii X16 X16 12 397")
    tran0.writeAction("slorii X16 X16 12 723")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
