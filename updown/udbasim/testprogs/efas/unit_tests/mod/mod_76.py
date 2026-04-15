from EFA_v2 import *
def mod_76():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3176039113382730259, 7430041837389688119]
    tran0.writeAction("movir X16 11283")
    tran0.writeAction("slorii X16 X16 12 2283")
    tran0.writeAction("slorii X16 X16 12 3849")
    tran0.writeAction("slorii X16 X16 12 3785")
    tran0.writeAction("slorii X16 X16 12 2579")
    tran0.writeAction("movir X17 26396")
    tran0.writeAction("slorii X17 X17 12 3322")
    tran0.writeAction("slorii X17 X17 12 3935")
    tran0.writeAction("slorii X17 X17 12 3698")
    tran0.writeAction("slorii X17 X17 12 3383")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
