from EFA_v2 import *
def modi_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8052626820654806129, -2863]
    tran0.writeAction("movir X16 28608")
    tran0.writeAction("slorii X16 X16 12 2774")
    tran0.writeAction("slorii X16 X16 12 3521")
    tran0.writeAction("slorii X16 X16 12 3739")
    tran0.writeAction("slorii X16 X16 12 1137")
    tran0.writeAction("modi X16 X17 -2863")
    tran0.writeAction("yieldt")
    return efa
