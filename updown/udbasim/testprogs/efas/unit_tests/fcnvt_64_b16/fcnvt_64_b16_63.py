from EFA_v2 import *
def fcnvt_64_b16_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18185515439806057189]
    tran0.writeAction("movir X16 64607")
    tran0.writeAction("slorii X16 X16 12 3807")
    tran0.writeAction("slorii X16 X16 12 263")
    tran0.writeAction("slorii X16 X16 12 88")
    tran0.writeAction("slorii X16 X16 12 2789")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
