from EFA_v2 import *
def divi_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [182495008703407782, 16943]
    tran0.writeAction("movir X16 648")
    tran0.writeAction("slorii X16 X16 12 1443")
    tran0.writeAction("slorii X16 X16 12 3671")
    tran0.writeAction("slorii X16 X16 12 198")
    tran0.writeAction("slorii X16 X16 12 1702")
    tran0.writeAction("divi X16 X17 16943")
    tran0.writeAction("yieldt")
    return efa
