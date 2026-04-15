from EFA_v2 import *
def modi_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1129143478167086638, -30313]
    tran0.writeAction("movir X16 4011")
    tran0.writeAction("slorii X16 X16 12 2144")
    tran0.writeAction("slorii X16 X16 12 716")
    tran0.writeAction("slorii X16 X16 12 2450")
    tran0.writeAction("slorii X16 X16 12 1582")
    tran0.writeAction("modi X16 X17 -30313")
    tran0.writeAction("yieldt")
    return efa
