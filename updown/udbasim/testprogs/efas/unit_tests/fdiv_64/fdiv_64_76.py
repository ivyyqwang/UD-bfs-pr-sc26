from EFA_v2 import *
def fdiv_64_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6930865334667518600, 17205973987446761490]
    tran0.writeAction("movir X16 24623")
    tran0.writeAction("slorii X16 X16 12 1556")
    tran0.writeAction("slorii X16 X16 12 3314")
    tran0.writeAction("slorii X16 X16 12 3794")
    tran0.writeAction("slorii X16 X16 12 648")
    tran0.writeAction("movir X17 61127")
    tran0.writeAction("slorii X17 X17 12 3682")
    tran0.writeAction("slorii X17 X17 12 3632")
    tran0.writeAction("slorii X17 X17 12 1538")
    tran0.writeAction("slorii X17 X17 12 2066")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
