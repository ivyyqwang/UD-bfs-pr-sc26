from EFA_v2 import *
def sub_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1777587069115395397, 5317170394009407132]
    tran0.writeAction("movir X16 59220")
    tran0.writeAction("slorii X16 X16 12 3039")
    tran0.writeAction("slorii X16 X16 12 2700")
    tran0.writeAction("slorii X16 X16 12 201")
    tran0.writeAction("slorii X16 X16 12 699")
    tran0.writeAction("movir X17 18890")
    tran0.writeAction("slorii X17 X17 12 1572")
    tran0.writeAction("slorii X17 X17 12 3393")
    tran0.writeAction("slorii X17 X17 12 632")
    tran0.writeAction("slorii X17 X17 12 3740")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
