from EFA_v2 import *
def fdiv_64_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6650417044236217649, 18092508819710858949]
    tran0.writeAction("movir X16 23627")
    tran0.writeAction("slorii X16 X16 12 113")
    tran0.writeAction("slorii X16 X16 12 249")
    tran0.writeAction("slorii X16 X16 12 3698")
    tran0.writeAction("slorii X16 X16 12 3377")
    tran0.writeAction("movir X17 64277")
    tran0.writeAction("slorii X17 X17 12 2062")
    tran0.writeAction("slorii X17 X17 12 2510")
    tran0.writeAction("slorii X17 X17 12 1997")
    tran0.writeAction("slorii X17 X17 12 1733")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
