from EFA_v2 import *
def modi_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4910333248833955920, -12316]
    tran0.writeAction("movir X16 17445")
    tran0.writeAction("slorii X16 X16 12 33")
    tran0.writeAction("slorii X16 X16 12 737")
    tran0.writeAction("slorii X16 X16 12 2202")
    tran0.writeAction("slorii X16 X16 12 2128")
    tran0.writeAction("modi X16 X17 -12316")
    tran0.writeAction("yieldt")
    return efa
