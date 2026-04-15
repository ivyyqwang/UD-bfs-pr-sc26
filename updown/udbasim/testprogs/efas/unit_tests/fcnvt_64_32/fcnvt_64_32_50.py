from EFA_v2 import *
def fcnvt_64_32_50():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [450117777163293881]
    tran0.writeAction("movir X16 1599")
    tran0.writeAction("slorii X16 X16 12 571")
    tran0.writeAction("slorii X16 X16 12 3014")
    tran0.writeAction("slorii X16 X16 12 3713")
    tran0.writeAction("slorii X16 X16 12 1209")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
