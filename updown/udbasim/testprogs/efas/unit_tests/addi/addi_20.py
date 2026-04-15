from EFA_v2 import *
def addi_20():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4538915310535281677, -25403]
    tran0.writeAction("movir X16 16125")
    tran0.writeAction("slorii X16 X16 12 1910")
    tran0.writeAction("slorii X16 X16 12 3390")
    tran0.writeAction("slorii X16 X16 12 152")
    tran0.writeAction("slorii X16 X16 12 3085")
    tran0.writeAction("addi X16 X17 -25403")
    tran0.writeAction("yieldt")
    return efa
