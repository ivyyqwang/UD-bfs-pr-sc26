from EFA_v2 import *
def divi_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7356830569392032950, -9305]
    tran0.writeAction("movir X16 26136")
    tran0.writeAction("slorii X16 X16 12 2918")
    tran0.writeAction("slorii X16 X16 12 3257")
    tran0.writeAction("slorii X16 X16 12 1420")
    tran0.writeAction("slorii X16 X16 12 3254")
    tran0.writeAction("divi X16 X17 -9305")
    tran0.writeAction("yieldt")
    return efa
