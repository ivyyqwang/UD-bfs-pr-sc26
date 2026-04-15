from EFA_v2 import *
def addi_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6021212244958293413, 21382]
    tran0.writeAction("movir X16 21391")
    tran0.writeAction("slorii X16 X16 12 2634")
    tran0.writeAction("slorii X16 X16 12 657")
    tran0.writeAction("slorii X16 X16 12 3978")
    tran0.writeAction("slorii X16 X16 12 3493")
    tran0.writeAction("addi X16 X17 21382")
    tran0.writeAction("yieldt")
    return efa
