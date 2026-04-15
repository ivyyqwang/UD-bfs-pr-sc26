from EFA_v2 import *
def fcnvt_64_32_21():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [18246656013652984079]
    tran0.writeAction("movir X16 64825")
    tran0.writeAction("slorii X16 X16 12 591")
    tran0.writeAction("slorii X16 X16 12 2096")
    tran0.writeAction("slorii X16 X16 12 2176")
    tran0.writeAction("slorii X16 X16 12 271")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
