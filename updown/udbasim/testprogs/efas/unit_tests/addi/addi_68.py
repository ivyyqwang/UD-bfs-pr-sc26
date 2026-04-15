from EFA_v2 import *
def addi_68():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3228273551619088423, 19827]
    tran0.writeAction("movir X16 11469")
    tran0.writeAction("slorii X16 X16 12 539")
    tran0.writeAction("slorii X16 X16 12 234")
    tran0.writeAction("slorii X16 X16 12 182")
    tran0.writeAction("slorii X16 X16 12 39")
    tran0.writeAction("addi X16 X17 19827")
    tran0.writeAction("yieldt")
    return efa
