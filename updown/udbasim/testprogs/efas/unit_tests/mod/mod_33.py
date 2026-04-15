from EFA_v2 import *
def mod_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2136878354126717977, 8695199817358276239]
    tran0.writeAction("movir X16 7591")
    tran0.writeAction("slorii X16 X16 12 2936")
    tran0.writeAction("slorii X16 X16 12 2713")
    tran0.writeAction("slorii X16 X16 12 3868")
    tran0.writeAction("slorii X16 X16 12 1049")
    tran0.writeAction("movir X17 30891")
    tran0.writeAction("slorii X17 X17 12 2274")
    tran0.writeAction("slorii X17 X17 12 2604")
    tran0.writeAction("slorii X17 X17 12 2791")
    tran0.writeAction("slorii X17 X17 12 1679")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
