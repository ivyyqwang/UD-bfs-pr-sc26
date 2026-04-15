from EFA_v2 import *
def addi_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8647893913705672929, -9684]
    tran0.writeAction("movir X16 30723")
    tran0.writeAction("slorii X16 X16 12 2011")
    tran0.writeAction("slorii X16 X16 12 557")
    tran0.writeAction("slorii X16 X16 12 2823")
    tran0.writeAction("slorii X16 X16 12 225")
    tran0.writeAction("addi X16 X17 -9684")
    tran0.writeAction("yieldt")
    return efa
