from EFA_v2 import *
def addi_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9181873072214395385, 15753]
    tran0.writeAction("movir X16 32620")
    tran0.writeAction("slorii X16 X16 12 2318")
    tran0.writeAction("slorii X16 X16 12 2394")
    tran0.writeAction("slorii X16 X16 12 260")
    tran0.writeAction("slorii X16 X16 12 2553")
    tran0.writeAction("addi X16 X17 15753")
    tran0.writeAction("yieldt")
    return efa
