from EFA_v2 import *
def fcnvt_64_32_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2380377043316097271]
    tran0.writeAction("movir X16 8456")
    tran0.writeAction("slorii X16 X16 12 3268")
    tran0.writeAction("slorii X16 X16 12 3874")
    tran0.writeAction("slorii X16 X16 12 1436")
    tran0.writeAction("slorii X16 X16 12 247")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
