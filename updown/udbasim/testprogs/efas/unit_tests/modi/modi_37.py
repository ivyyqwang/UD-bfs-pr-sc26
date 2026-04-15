from EFA_v2 import *
def modi_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4508083379104160759, 24393]
    tran0.writeAction("movir X16 16015")
    tran0.writeAction("slorii X16 X16 12 3807")
    tran0.writeAction("slorii X16 X16 12 717")
    tran0.writeAction("slorii X16 X16 12 1417")
    tran0.writeAction("slorii X16 X16 12 3063")
    tran0.writeAction("modi X16 X17 24393")
    tran0.writeAction("yieldt")
    return efa
