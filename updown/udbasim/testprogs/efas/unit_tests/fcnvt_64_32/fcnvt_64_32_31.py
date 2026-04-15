from EFA_v2 import *
def fcnvt_64_32_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4378212431165869236]
    tran0.writeAction("movir X16 15554")
    tran0.writeAction("slorii X16 X16 12 2192")
    tran0.writeAction("slorii X16 X16 12 614")
    tran0.writeAction("slorii X16 X16 12 3444")
    tran0.writeAction("slorii X16 X16 12 3252")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
