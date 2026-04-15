from EFA_v2 import *
def sub_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2108756563994222875, -5570483898400990029]
    tran0.writeAction("movir X16 7491")
    tran0.writeAction("slorii X16 X16 12 3310")
    tran0.writeAction("slorii X16 X16 12 3098")
    tran0.writeAction("slorii X16 X16 12 2658")
    tran0.writeAction("slorii X16 X16 12 283")
    tran0.writeAction("movir X17 45745")
    tran0.writeAction("slorii X17 X17 12 2726")
    tran0.writeAction("slorii X17 X17 12 2168")
    tran0.writeAction("slorii X17 X17 12 3177")
    tran0.writeAction("slorii X17 X17 12 3251")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
