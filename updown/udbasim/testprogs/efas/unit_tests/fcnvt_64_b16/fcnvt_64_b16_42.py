from EFA_v2 import *
def fcnvt_64_b16_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4076398161356238693]
    tran0.writeAction("movir X16 14482")
    tran0.writeAction("slorii X16 X16 12 1128")
    tran0.writeAction("slorii X16 X16 12 1970")
    tran0.writeAction("slorii X16 X16 12 2842")
    tran0.writeAction("slorii X16 X16 12 3941")
    tran0.writeAction("fcnvt.64.b16 X16 X16")
    tran0.writeAction("yieldt")
    return efa
