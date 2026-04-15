from EFA_v2 import *
def addi_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [389696498999502266, 32215]
    tran0.writeAction("movir X16 1384")
    tran0.writeAction("slorii X16 X16 12 1966")
    tran0.writeAction("slorii X16 X16 12 1713")
    tran0.writeAction("slorii X16 X16 12 322")
    tran0.writeAction("slorii X16 X16 12 1466")
    tran0.writeAction("addi X16 X17 32215")
    tran0.writeAction("yieldt")
    return efa
