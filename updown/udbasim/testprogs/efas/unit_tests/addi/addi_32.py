from EFA_v2 import *
def addi_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7422232558086868148, -4777]
    tran0.writeAction("movir X16 26369")
    tran0.writeAction("slorii X16 X16 12 274")
    tran0.writeAction("slorii X16 X16 12 4057")
    tran0.writeAction("slorii X16 X16 12 436")
    tran0.writeAction("slorii X16 X16 12 3252")
    tran0.writeAction("addi X16 X17 -4777")
    tran0.writeAction("yieldt")
    return efa
