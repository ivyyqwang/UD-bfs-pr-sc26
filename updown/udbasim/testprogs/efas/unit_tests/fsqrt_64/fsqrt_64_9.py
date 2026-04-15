from EFA_v2 import *
def fsqrt_64_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16136661301414576708]
    tran0.writeAction("movir X16 57328")
    tran0.writeAction("slorii X16 X16 12 3839")
    tran0.writeAction("slorii X16 X16 12 1339")
    tran0.writeAction("slorii X16 X16 12 2492")
    tran0.writeAction("slorii X16 X16 12 580")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
