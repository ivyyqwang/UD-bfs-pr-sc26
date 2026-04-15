from EFA_v2 import *
def fdiv_64_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6479933698015811862, 4684022632688223578]
    tran0.writeAction("movir X16 23021")
    tran0.writeAction("slorii X16 X16 12 1429")
    tran0.writeAction("slorii X16 X16 12 3518")
    tran0.writeAction("slorii X16 X16 12 1293")
    tran0.writeAction("slorii X16 X16 12 2326")
    tran0.writeAction("movir X17 16640")
    tran0.writeAction("slorii X17 X17 12 4060")
    tran0.writeAction("slorii X17 X17 12 1141")
    tran0.writeAction("slorii X17 X17 12 1112")
    tran0.writeAction("slorii X17 X17 12 1370")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
