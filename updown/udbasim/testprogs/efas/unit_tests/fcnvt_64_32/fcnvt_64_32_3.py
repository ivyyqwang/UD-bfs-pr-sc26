from EFA_v2 import *
def fcnvt_64_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7601854603420760033]
    tran0.writeAction("movir X16 27007")
    tran0.writeAction("slorii X16 X16 12 871")
    tran0.writeAction("slorii X16 X16 12 3143")
    tran0.writeAction("slorii X16 X16 12 255")
    tran0.writeAction("slorii X16 X16 12 2017")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
