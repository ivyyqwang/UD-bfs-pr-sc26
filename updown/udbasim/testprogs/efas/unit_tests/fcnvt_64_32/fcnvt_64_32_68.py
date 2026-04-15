from EFA_v2 import *
def fcnvt_64_32_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18162259180138671911]
    tran0.writeAction("movir X16 64525")
    tran0.writeAction("slorii X16 X16 12 1255")
    tran0.writeAction("slorii X16 X16 12 3870")
    tran0.writeAction("slorii X16 X16 12 3042")
    tran0.writeAction("slorii X16 X16 12 3879")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
