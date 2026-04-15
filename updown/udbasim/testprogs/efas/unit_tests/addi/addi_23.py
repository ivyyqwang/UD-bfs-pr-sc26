from EFA_v2 import *
def addi_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4737337553568311272, -7939]
    tran0.writeAction("movir X16 16830")
    tran0.writeAction("slorii X16 X16 12 1654")
    tran0.writeAction("slorii X16 X16 12 1997")
    tran0.writeAction("slorii X16 X16 12 2282")
    tran0.writeAction("slorii X16 X16 12 2024")
    tran0.writeAction("addi X16 X17 -7939")
    tran0.writeAction("yieldt")
    return efa
