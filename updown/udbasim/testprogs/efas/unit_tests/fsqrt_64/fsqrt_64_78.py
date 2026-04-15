from EFA_v2 import *
def fsqrt_64_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9674089883159292172]
    tran0.writeAction("movir X16 34369")
    tran0.writeAction("slorii X16 X16 12 1111")
    tran0.writeAction("slorii X16 X16 12 3650")
    tran0.writeAction("slorii X16 X16 12 3726")
    tran0.writeAction("slorii X16 X16 12 2316")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
