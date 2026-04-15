from EFA_v2 import *
def fcnvt_64_32_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4512309303430334729]
    tran0.writeAction("movir X16 16030")
    tran0.writeAction("slorii X16 X16 12 3862")
    tran0.writeAction("slorii X16 X16 12 1915")
    tran0.writeAction("slorii X16 X16 12 2684")
    tran0.writeAction("slorii X16 X16 12 2313")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
