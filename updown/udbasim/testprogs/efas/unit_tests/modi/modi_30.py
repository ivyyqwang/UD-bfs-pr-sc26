from EFA_v2 import *
def modi_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2318217341786278466, -10444]
    tran0.writeAction("movir X16 8235")
    tran0.writeAction("slorii X16 X16 12 3942")
    tran0.writeAction("slorii X16 X16 12 977")
    tran0.writeAction("slorii X16 X16 12 1316")
    tran0.writeAction("slorii X16 X16 12 2626")
    tran0.writeAction("modi X16 X17 -10444")
    tran0.writeAction("yieldt")
    return efa
