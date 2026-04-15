from EFA_v2 import *
def fcnvt_64_32_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17015789650631235244]
    tran0.writeAction("movir X16 60452")
    tran0.writeAction("slorii X16 X16 12 936")
    tran0.writeAction("slorii X16 X16 12 2210")
    tran0.writeAction("slorii X16 X16 12 2633")
    tran0.writeAction("slorii X16 X16 12 1708")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
