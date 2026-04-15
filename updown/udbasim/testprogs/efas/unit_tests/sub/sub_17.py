from EFA_v2 import *
def sub_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [475529581212474231, -3696718456839605611]
    tran0.writeAction("movir X16 1689")
    tran0.writeAction("slorii X16 X16 12 1722")
    tran0.writeAction("slorii X16 X16 12 632")
    tran0.writeAction("slorii X16 X16 12 1473")
    tran0.writeAction("slorii X16 X16 12 2935")
    tran0.writeAction("movir X17 52402")
    tran0.writeAction("slorii X17 X17 12 2530")
    tran0.writeAction("slorii X17 X17 12 1609")
    tran0.writeAction("slorii X17 X17 12 1823")
    tran0.writeAction("slorii X17 X17 12 661")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
