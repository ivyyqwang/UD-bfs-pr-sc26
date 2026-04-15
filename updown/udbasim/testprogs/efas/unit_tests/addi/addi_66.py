from EFA_v2 import *
def addi_66():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7148072557024724457, -20239]
    tran0.writeAction("movir X16 40140")
    tran0.writeAction("slorii X16 X16 12 3870")
    tran0.writeAction("slorii X16 X16 12 425")
    tran0.writeAction("slorii X16 X16 12 3371")
    tran0.writeAction("slorii X16 X16 12 2583")
    tran0.writeAction("addi X16 X17 -20239")
    tran0.writeAction("yieldt")
    return efa
