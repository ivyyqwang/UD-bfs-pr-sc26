from EFA_v2 import *
def fcnvt_64_32_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2142146537712166116]
    tran0.writeAction("movir X16 7610")
    tran0.writeAction("slorii X16 X16 12 1774")
    tran0.writeAction("slorii X16 X16 12 3373")
    tran0.writeAction("slorii X16 X16 12 682")
    tran0.writeAction("slorii X16 X16 12 1252")
    tran0.writeAction("fcnvt.64.32 X16 X16")
    tran0.writeAction("yieldt")
    return efa
