from EFA_v2 import *
def hash_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7382477476275807089, 6863364111890296110]
    tran0.writeAction("movir X16 39308")
    tran0.writeAction("slorii X16 X16 12 701")
    tran0.writeAction("slorii X16 X16 12 2416")
    tran0.writeAction("slorii X16 X16 12 1057")
    tran0.writeAction("slorii X16 X16 12 3215")
    tran0.writeAction("movir X17 24383")
    tran0.writeAction("slorii X17 X17 12 2324")
    tran0.writeAction("slorii X17 X17 12 3021")
    tran0.writeAction("slorii X17 X17 12 1578")
    tran0.writeAction("slorii X17 X17 12 3374")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
