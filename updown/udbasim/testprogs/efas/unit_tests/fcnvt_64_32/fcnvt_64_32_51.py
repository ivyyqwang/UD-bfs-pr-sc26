from EFA_v2 import *
def fcnvt_64_32_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [11765732263566148509]
    tran0.writeAction("movir X16 41800")
    tran0.writeAction("slorii X16 X16 12 1138")
    tran0.writeAction("slorii X16 X16 12 2044")
    tran0.writeAction("slorii X16 X16 12 872")
    tran0.writeAction("slorii X16 X16 12 925")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
