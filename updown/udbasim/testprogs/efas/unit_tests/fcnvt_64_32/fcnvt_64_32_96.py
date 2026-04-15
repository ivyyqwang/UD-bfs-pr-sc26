from EFA_v2 import *
def fcnvt_64_32_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3542603681030742163]
    tran0.writeAction("movir X16 12585")
    tran0.writeAction("slorii X16 X16 12 3508")
    tran0.writeAction("slorii X16 X16 12 1859")
    tran0.writeAction("slorii X16 X16 12 3394")
    tran0.writeAction("slorii X16 X16 12 147")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
