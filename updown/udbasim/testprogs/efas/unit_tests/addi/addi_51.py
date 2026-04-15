from EFA_v2 import *
def addi_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7381957361762068407, 17003]
    tran0.writeAction("movir X16 26225")
    tran0.writeAction("slorii X16 X16 12 4017")
    tran0.writeAction("slorii X16 X16 12 3062")
    tran0.writeAction("slorii X16 X16 12 3718")
    tran0.writeAction("slorii X16 X16 12 1975")
    tran0.writeAction("addi X16 X17 17003")
    tran0.writeAction("yieldt")
    return efa
