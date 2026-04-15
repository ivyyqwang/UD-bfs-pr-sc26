from EFA_v2 import *
def fcnvt_64_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [423355306737253069]
    tran0.writeAction("movir X16 1504")
    tran0.writeAction("slorii X16 X16 12 246")
    tran0.writeAction("slorii X16 X16 12 2191")
    tran0.writeAction("slorii X16 X16 12 3483")
    tran0.writeAction("slorii X16 X16 12 2765")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
