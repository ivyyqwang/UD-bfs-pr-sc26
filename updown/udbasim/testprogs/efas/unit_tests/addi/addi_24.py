from EFA_v2 import *
def addi_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2316509573040176399, -15439]
    tran0.writeAction("movir X16 57306")
    tran0.writeAction("slorii X16 X16 12 429")
    tran0.writeAction("slorii X16 X16 12 276")
    tran0.writeAction("slorii X16 X16 12 608")
    tran0.writeAction("slorii X16 X16 12 753")
    tran0.writeAction("addi X16 X17 -15439")
    tran0.writeAction("yieldt")
    return efa
