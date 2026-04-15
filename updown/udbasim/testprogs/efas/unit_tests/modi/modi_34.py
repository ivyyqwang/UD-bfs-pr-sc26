from EFA_v2 import *
def modi_34():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5395361273880321825, -3163]
    tran0.writeAction("movir X16 19168")
    tran0.writeAction("slorii X16 X16 12 711")
    tran0.writeAction("slorii X16 X16 12 3620")
    tran0.writeAction("slorii X16 X16 12 2193")
    tran0.writeAction("slorii X16 X16 12 3873")
    tran0.writeAction("modi X16 X17 -3163")
    tran0.writeAction("yieldt")
    return efa
