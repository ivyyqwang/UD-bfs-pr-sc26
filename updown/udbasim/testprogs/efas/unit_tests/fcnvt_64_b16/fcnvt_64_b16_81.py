from EFA_v2 import *
def fcnvt_64_b16_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2615059298797629867]
    tran0.writeAction("movir X16 9290")
    tran0.writeAction("slorii X16 X16 12 2281")
    tran0.writeAction("slorii X16 X16 12 955")
    tran0.writeAction("slorii X16 X16 12 1699")
    tran0.writeAction("slorii X16 X16 12 427")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
