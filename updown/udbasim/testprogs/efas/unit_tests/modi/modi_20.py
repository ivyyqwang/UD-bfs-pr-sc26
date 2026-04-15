from EFA_v2 import *
def modi_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2487927781228105392, -18886]
    tran0.writeAction("movir X16 8838")
    tran0.writeAction("slorii X16 X16 12 3666")
    tran0.writeAction("slorii X16 X16 12 682")
    tran0.writeAction("slorii X16 X16 12 3796")
    tran0.writeAction("slorii X16 X16 12 3760")
    tran0.writeAction("modi X16 X17 -18886")
    tran0.writeAction("yieldt")
    return efa
