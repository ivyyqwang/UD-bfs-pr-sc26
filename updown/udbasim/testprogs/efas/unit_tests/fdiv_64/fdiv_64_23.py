from EFA_v2 import *
def fdiv_64_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9619460088649890474, 11211743452698063796]
    tran0.writeAction("movir X16 34175")
    tran0.writeAction("slorii X16 X16 12 767")
    tran0.writeAction("slorii X16 X16 12 3083")
    tran0.writeAction("slorii X16 X16 12 99")
    tran0.writeAction("slorii X16 X16 12 2730")
    tran0.writeAction("movir X17 39832")
    tran0.writeAction("slorii X17 X17 12 468")
    tran0.writeAction("slorii X17 X17 12 1170")
    tran0.writeAction("slorii X17 X17 12 3603")
    tran0.writeAction("slorii X17 X17 12 948")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
