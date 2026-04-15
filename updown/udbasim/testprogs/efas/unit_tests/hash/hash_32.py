from EFA_v2 import *
def hash_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1039834690724345091, 4475495721079058844]
    tran0.writeAction("movir X16 61841")
    tran0.writeAction("slorii X16 X16 12 3133")
    tran0.writeAction("slorii X16 X16 12 2986")
    tran0.writeAction("slorii X16 X16 12 1012")
    tran0.writeAction("slorii X16 X16 12 2813")
    tran0.writeAction("movir X17 15900")
    tran0.writeAction("slorii X17 X17 12 634")
    tran0.writeAction("slorii X17 X17 12 1384")
    tran0.writeAction("slorii X17 X17 12 2859")
    tran0.writeAction("slorii X17 X17 12 412")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
