from EFA_v2 import *
def muli_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6988931968290119869, 32189]
    tran0.writeAction("movir X16 24829")
    tran0.writeAction("slorii X16 X16 12 2761")
    tran0.writeAction("slorii X16 X16 12 2209")
    tran0.writeAction("slorii X16 X16 12 1246")
    tran0.writeAction("slorii X16 X16 12 189")
    tran0.writeAction("muli X16 X17 32189")
    tran0.writeAction("yieldt")
    return efa
