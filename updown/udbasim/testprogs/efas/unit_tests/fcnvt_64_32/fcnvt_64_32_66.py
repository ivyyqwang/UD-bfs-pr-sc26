from EFA_v2 import *
def fcnvt_64_32_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1176969833309765802]
    tran0.writeAction("movir X16 4181")
    tran0.writeAction("slorii X16 X16 12 1789")
    tran0.writeAction("slorii X16 X16 12 985")
    tran0.writeAction("slorii X16 X16 12 3192")
    tran0.writeAction("slorii X16 X16 12 170")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
