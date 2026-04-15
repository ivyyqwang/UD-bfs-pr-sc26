from EFA_v2 import *
def addi_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6558845583526131018, -4851]
    tran0.writeAction("movir X16 23301")
    tran0.writeAction("slorii X16 X16 12 2868")
    tran0.writeAction("slorii X16 X16 12 3798")
    tran0.writeAction("slorii X16 X16 12 2927")
    tran0.writeAction("slorii X16 X16 12 1354")
    tran0.writeAction("addi X16 X17 -4851")
    tran0.writeAction("yieldt")
    return efa
