from EFA_v2 import *
def divi_81():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9046146570715543132, -15182]
    tran0.writeAction("movir X16 32138")
    tran0.writeAction("slorii X16 X16 12 1510")
    tran0.writeAction("slorii X16 X16 12 165")
    tran0.writeAction("slorii X16 X16 12 2531")
    tran0.writeAction("slorii X16 X16 12 1628")
    tran0.writeAction("divi X16 X17 -15182")
    tran0.writeAction("yieldt")
    return efa
