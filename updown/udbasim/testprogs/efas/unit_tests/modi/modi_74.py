from EFA_v2 import *
def modi_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8079400051666018617, -13515]
    tran0.writeAction("movir X16 28703")
    tran0.writeAction("slorii X16 X16 12 3256")
    tran0.writeAction("slorii X16 X16 12 2653")
    tran0.writeAction("slorii X16 X16 12 3382")
    tran0.writeAction("slorii X16 X16 12 313")
    tran0.writeAction("modi X16 X17 -13515")
    tran0.writeAction("yieldt")
    return efa
