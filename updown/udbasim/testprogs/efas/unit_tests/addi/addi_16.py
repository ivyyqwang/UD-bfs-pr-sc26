from EFA_v2 import *
def addi_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6808155713460831402, 8345]
    tran0.writeAction("movir X16 41348")
    tran0.writeAction("slorii X16 X16 12 2343")
    tran0.writeAction("slorii X16 X16 12 803")
    tran0.writeAction("slorii X16 X16 12 2543")
    tran0.writeAction("slorii X16 X16 12 2902")
    tran0.writeAction("addi X16 X17 8345")
    tran0.writeAction("yieldt")
    return efa
