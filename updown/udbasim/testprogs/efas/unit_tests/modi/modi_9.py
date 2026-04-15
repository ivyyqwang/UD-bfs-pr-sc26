from EFA_v2 import *
def modi_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6842327758431418650, -25325]
    tran0.writeAction("movir X16 24308")
    tran0.writeAction("slorii X16 X16 12 3405")
    tran0.writeAction("slorii X16 X16 12 2070")
    tran0.writeAction("slorii X16 X16 12 407")
    tran0.writeAction("slorii X16 X16 12 2330")
    tran0.writeAction("modi X16 X17 -25325")
    tran0.writeAction("yieldt")
    return efa
