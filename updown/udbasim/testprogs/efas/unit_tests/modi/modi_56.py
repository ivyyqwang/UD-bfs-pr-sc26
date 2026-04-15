from EFA_v2 import *
def modi_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4802093373363811773, -30769]
    tran0.writeAction("movir X16 17060")
    tran0.writeAction("slorii X16 X16 12 1895")
    tran0.writeAction("slorii X16 X16 12 2817")
    tran0.writeAction("slorii X16 X16 12 2487")
    tran0.writeAction("slorii X16 X16 12 1469")
    tran0.writeAction("modi X16 X17 -30769")
    tran0.writeAction("yieldt")
    return efa
