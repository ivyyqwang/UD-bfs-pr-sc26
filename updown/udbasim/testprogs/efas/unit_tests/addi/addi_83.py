from EFA_v2 import *
def addi_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3130089197851583871, 32611]
    tran0.writeAction("movir X16 54415")
    tran0.writeAction("slorii X16 X16 12 2823")
    tran0.writeAction("slorii X16 X16 12 1374")
    tran0.writeAction("slorii X16 X16 12 3149")
    tran0.writeAction("slorii X16 X16 12 2689")
    tran0.writeAction("addi X16 X17 32611")
    tran0.writeAction("yieldt")
    return efa
