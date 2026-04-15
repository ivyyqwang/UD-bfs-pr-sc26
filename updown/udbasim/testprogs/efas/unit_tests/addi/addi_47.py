from EFA_v2 import *
def addi_47():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1135370209162607705, 8756]
    tran0.writeAction("movir X16 4033")
    tran0.writeAction("slorii X16 X16 12 2643")
    tran0.writeAction("slorii X16 X16 12 149")
    tran0.writeAction("slorii X16 X16 12 2859")
    tran0.writeAction("slorii X16 X16 12 3161")
    tran0.writeAction("addi X16 X17 8756")
    tran0.writeAction("yieldt")
    return efa
