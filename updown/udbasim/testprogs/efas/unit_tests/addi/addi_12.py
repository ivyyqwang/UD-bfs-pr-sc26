from EFA_v2 import *
def addi_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8926182100495755942, -29151]
    tran0.writeAction("movir X16 33823")
    tran0.writeAction("slorii X16 X16 12 3402")
    tran0.writeAction("slorii X16 X16 12 3115")
    tran0.writeAction("slorii X16 X16 12 2049")
    tran0.writeAction("slorii X16 X16 12 1370")
    tran0.writeAction("addi X16 X17 -29151")
    tran0.writeAction("yieldt")
    return efa
