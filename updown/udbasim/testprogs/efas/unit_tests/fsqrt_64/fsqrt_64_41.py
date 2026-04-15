from EFA_v2 import *
def fsqrt_64_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7142132523865720017]
    tran0.writeAction("movir X16 25373")
    tran0.writeAction("slorii X16 X16 12 3899")
    tran0.writeAction("slorii X16 X16 12 151")
    tran0.writeAction("slorii X16 X16 12 3196")
    tran0.writeAction("slorii X16 X16 12 1233")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
