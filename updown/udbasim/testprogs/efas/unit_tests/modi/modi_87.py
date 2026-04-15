from EFA_v2 import *
def modi_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-346390229429762502, 9417]
    tran0.writeAction("movir X16 64305")
    tran0.writeAction("slorii X16 X16 12 1534")
    tran0.writeAction("slorii X16 X16 12 3053")
    tran0.writeAction("slorii X16 X16 12 708")
    tran0.writeAction("slorii X16 X16 12 1594")
    tran0.writeAction("modi X16 X17 9417")
    tran0.writeAction("yieldt")
    return efa
