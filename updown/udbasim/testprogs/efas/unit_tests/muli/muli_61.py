from EFA_v2 import *
def muli_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6365386202975625787, 1655]
    tran0.writeAction("movir X16 22614")
    tran0.writeAction("slorii X16 X16 12 1616")
    tran0.writeAction("slorii X16 X16 12 1726")
    tran0.writeAction("slorii X16 X16 12 2190")
    tran0.writeAction("slorii X16 X16 12 571")
    tran0.writeAction("muli X16 X17 1655")
    tran0.writeAction("yieldt")
    return efa
