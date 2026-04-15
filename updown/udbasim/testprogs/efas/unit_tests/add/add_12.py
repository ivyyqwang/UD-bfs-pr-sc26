from EFA_v2 import *
def add_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7570741566645134891, -1558999944873064051]
    tran0.writeAction("movir X16 26896")
    tran0.writeAction("slorii X16 X16 12 2773")
    tran0.writeAction("slorii X16 X16 12 2022")
    tran0.writeAction("slorii X16 X16 12 686")
    tran0.writeAction("slorii X16 X16 12 1579")
    tran0.writeAction("movir X17 59997")
    tran0.writeAction("slorii X17 X17 12 1308")
    tran0.writeAction("slorii X17 X17 12 3936")
    tran0.writeAction("slorii X17 X17 12 4044")
    tran0.writeAction("slorii X17 X17 12 2445")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
