from EFA_v2 import *
def fsqrt_64_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12249159179879222723]
    tran0.writeAction("movir X16 43517")
    tran0.writeAction("slorii X16 X16 12 3094")
    tran0.writeAction("slorii X16 X16 12 17")
    tran0.writeAction("slorii X16 X16 12 3752")
    tran0.writeAction("slorii X16 X16 12 3523")
    tran0.writeAction("fsqrt.64 X16 X17")
    tran0.writeAction("yieldt")
    return efa
