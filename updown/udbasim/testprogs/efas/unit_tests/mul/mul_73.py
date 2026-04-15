from EFA_v2 import *
def mul_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [171914242732910989, -8629258127939226346]
    tran0.writeAction("movir X16 610")
    tran0.writeAction("slorii X16 X16 12 3121")
    tran0.writeAction("slorii X16 X16 12 1993")
    tran0.writeAction("slorii X16 X16 12 3790")
    tran0.writeAction("slorii X16 X16 12 2445")
    tran0.writeAction("movir X17 34878")
    tran0.writeAction("slorii X17 X17 12 2935")
    tran0.writeAction("slorii X17 X17 12 977")
    tran0.writeAction("slorii X17 X17 12 123")
    tran0.writeAction("slorii X17 X17 12 1302")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
