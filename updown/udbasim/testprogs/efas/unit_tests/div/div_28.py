from EFA_v2 import *
def div_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1066771126407264838, 1422014509850435039]
    tran0.writeAction("movir X16 3789")
    tran0.writeAction("slorii X16 X16 12 3818")
    tran0.writeAction("slorii X16 X16 12 4094")
    tran0.writeAction("slorii X16 X16 12 607")
    tran0.writeAction("slorii X16 X16 12 2630")
    tran0.writeAction("movir X17 5052")
    tran0.writeAction("slorii X17 X17 12 42")
    tran0.writeAction("slorii X17 X17 12 2461")
    tran0.writeAction("slorii X17 X17 12 353")
    tran0.writeAction("slorii X17 X17 12 3551")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
