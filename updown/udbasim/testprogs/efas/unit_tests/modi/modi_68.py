from EFA_v2 import *
def modi_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6626301729777083109, 4121]
    tran0.writeAction("movir X16 41994")
    tran0.writeAction("slorii X16 X16 12 2650")
    tran0.writeAction("slorii X16 X16 12 3894")
    tran0.writeAction("slorii X16 X16 12 329")
    tran0.writeAction("slorii X16 X16 12 3355")
    tran0.writeAction("modi X16 X17 4121")
    tran0.writeAction("yieldt")
    return efa
