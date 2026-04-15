from EFA_v2 import *
def modi_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4495003411100613739, -30047]
    tran0.writeAction("movir X16 15969")
    tran0.writeAction("slorii X16 X16 12 1884")
    tran0.writeAction("slorii X16 X16 12 2414")
    tran0.writeAction("slorii X16 X16 12 3363")
    tran0.writeAction("slorii X16 X16 12 3179")
    tran0.writeAction("modi X16 X17 -30047")
    tran0.writeAction("yieldt")
    return efa
