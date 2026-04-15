from EFA_v2 import *
def fdiv_64_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4858482540338361270, 10430830306224472743]
    tran0.writeAction("movir X16 17260")
    tran0.writeAction("slorii X16 X16 12 3266")
    tran0.writeAction("slorii X16 X16 12 268")
    tran0.writeAction("slorii X16 X16 12 1251")
    tran0.writeAction("slorii X16 X16 12 950")
    tran0.writeAction("movir X17 37057")
    tran0.writeAction("slorii X17 X17 12 3086")
    tran0.writeAction("slorii X17 X17 12 1546")
    tran0.writeAction("slorii X17 X17 12 3640")
    tran0.writeAction("slorii X17 X17 12 679")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
