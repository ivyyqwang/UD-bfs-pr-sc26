from EFA_v2 import *
def addi_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6890465865808654683, -16813]
    tran0.writeAction("movir X16 24479")
    tran0.writeAction("slorii X16 X16 12 3491")
    tran0.writeAction("slorii X16 X16 12 668")
    tran0.writeAction("slorii X16 X16 12 1963")
    tran0.writeAction("slorii X16 X16 12 347")
    tran0.writeAction("addi X16 X17 -16813")
    tran0.writeAction("yieldt")
    return efa
