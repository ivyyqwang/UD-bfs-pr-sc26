from EFA_v2 import *
def modi_69():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4969281723325159517, 5670]
    tran0.writeAction("movir X16 17654")
    tran0.writeAction("slorii X16 X16 12 1782")
    tran0.writeAction("slorii X16 X16 12 1571")
    tran0.writeAction("slorii X16 X16 12 2609")
    tran0.writeAction("slorii X16 X16 12 2141")
    tran0.writeAction("modi X16 X17 5670")
    tran0.writeAction("yieldt")
    return efa
