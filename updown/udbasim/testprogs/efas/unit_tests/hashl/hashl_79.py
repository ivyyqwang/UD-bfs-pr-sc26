from EFA_v2 import *
def hashl_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8473277231286364184, 5757684360946434360, 6705025644505793252, -374719012590949650]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 30103")
    tran0.writeAction("slorii X17 X17 12 523")
    tran0.writeAction("slorii X17 X17 12 3998")
    tran0.writeAction("slorii X17 X17 12 938")
    tran0.writeAction("slorii X17 X17 12 2072")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 20455")
    tran0.writeAction("slorii X17 X17 12 1654")
    tran0.writeAction("slorii X17 X17 12 2999")
    tran0.writeAction("slorii X17 X17 12 140")
    tran0.writeAction("slorii X17 X17 12 312")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 23821")
    tran0.writeAction("slorii X17 X17 12 148")
    tran0.writeAction("slorii X17 X17 12 3206")
    tran0.writeAction("slorii X17 X17 12 2672")
    tran0.writeAction("slorii X17 X17 12 740")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 64204")
    tran0.writeAction("slorii X17 X17 12 2992")
    tran0.writeAction("slorii X17 X17 12 2843")
    tran0.writeAction("slorii X17 X17 12 3814")
    tran0.writeAction("slorii X17 X17 12 2798")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
