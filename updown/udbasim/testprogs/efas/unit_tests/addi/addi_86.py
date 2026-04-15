from EFA_v2 import *
def addi_86():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1426661920149838778, -16827]
    tran0.writeAction("movir X16 60467")
    tran0.writeAction("slorii X16 X16 12 1960")
    tran0.writeAction("slorii X16 X16 12 2778")
    tran0.writeAction("slorii X16 X16 12 3654")
    tran0.writeAction("slorii X16 X16 12 1094")
    tran0.writeAction("addi X16 X17 -16827")
    tran0.writeAction("yieldt")
    return efa
