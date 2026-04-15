from EFA_v2 import *
def modi_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6959209305085239839, -17462]
    tran0.writeAction("movir X16 40811")
    tran0.writeAction("slorii X16 X16 12 3776")
    tran0.writeAction("slorii X16 X16 12 556")
    tran0.writeAction("slorii X16 X16 12 3281")
    tran0.writeAction("slorii X16 X16 12 3553")
    tran0.writeAction("modi X16 X17 -17462")
    tran0.writeAction("yieldt")
    return efa
