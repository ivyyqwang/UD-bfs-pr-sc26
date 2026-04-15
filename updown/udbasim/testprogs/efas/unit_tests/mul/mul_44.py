from EFA_v2 import *
def mul_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7246298811408503886, -2811270807223779613]
    tran0.writeAction("movir X16 25744")
    tran0.writeAction("slorii X16 X16 12 102")
    tran0.writeAction("slorii X16 X16 12 94")
    tran0.writeAction("slorii X16 X16 12 1389")
    tran0.writeAction("slorii X16 X16 12 1102")
    tran0.writeAction("movir X17 55548")
    tran0.writeAction("slorii X17 X17 12 1473")
    tran0.writeAction("slorii X17 X17 12 2168")
    tran0.writeAction("slorii X17 X17 12 3")
    tran0.writeAction("slorii X17 X17 12 3811")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
