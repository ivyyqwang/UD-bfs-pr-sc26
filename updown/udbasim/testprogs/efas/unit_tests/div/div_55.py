from EFA_v2 import *
def div_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6325929683061489806, -1202520027513980276]
    tran0.writeAction("movir X16 22474")
    tran0.writeAction("slorii X16 X16 12 888")
    tran0.writeAction("slorii X16 X16 12 2000")
    tran0.writeAction("slorii X16 X16 12 4012")
    tran0.writeAction("slorii X16 X16 12 142")
    tran0.writeAction("movir X17 61263")
    tran0.writeAction("slorii X17 X17 12 3238")
    tran0.writeAction("slorii X17 X17 12 2044")
    tran0.writeAction("slorii X17 X17 12 3015")
    tran0.writeAction("slorii X17 X17 12 2700")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
