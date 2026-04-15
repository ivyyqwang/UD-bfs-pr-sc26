from EFA_v2 import *
def addi_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7259082333041209116, 9486]
    tran0.writeAction("movir X16 25789")
    tran0.writeAction("slorii X16 X16 12 1806")
    tran0.writeAction("slorii X16 X16 12 3056")
    tran0.writeAction("slorii X16 X16 12 962")
    tran0.writeAction("slorii X16 X16 12 3868")
    tran0.writeAction("addi X16 X17 9486")
    tran0.writeAction("yieldt")
    return efa
