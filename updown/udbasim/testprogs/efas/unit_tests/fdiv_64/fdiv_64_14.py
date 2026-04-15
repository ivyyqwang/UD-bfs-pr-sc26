from EFA_v2 import *
def fdiv_64_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14290815629542916617, 3617413440341952961]
    tran0.writeAction("movir X16 50771")
    tran0.writeAction("slorii X16 X16 12 721")
    tran0.writeAction("slorii X16 X16 12 2397")
    tran0.writeAction("slorii X16 X16 12 2072")
    tran0.writeAction("slorii X16 X16 12 521")
    tran0.writeAction("movir X17 12851")
    tran0.writeAction("slorii X17 X17 12 2597")
    tran0.writeAction("slorii X17 X17 12 2989")
    tran0.writeAction("slorii X17 X17 12 1252")
    tran0.writeAction("slorii X17 X17 12 2497")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
