from EFA_v2 import *
def modi_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7270140350238194879, -1887]
    tran0.writeAction("movir X16 39707")
    tran0.writeAction("slorii X16 X16 12 1117")
    tran0.writeAction("slorii X16 X16 12 3788")
    tran0.writeAction("slorii X16 X16 12 3352")
    tran0.writeAction("slorii X16 X16 12 833")
    tran0.writeAction("modi X16 X17 -1887")
    tran0.writeAction("yieldt")
    return efa
