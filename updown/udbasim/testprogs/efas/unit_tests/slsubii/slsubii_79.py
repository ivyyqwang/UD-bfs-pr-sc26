from EFA_v2 import *
def slsubii_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6615381794925833201, 9, 689]
    tran0.writeAction("movir X16 42033")
    tran0.writeAction("slorii X16 X16 12 1812")
    tran0.writeAction("slorii X16 X16 12 3755")
    tran0.writeAction("slorii X16 X16 12 3521")
    tran0.writeAction("slorii X16 X16 12 1039")
    tran0.writeAction("slsubii X16 X17 9 689")
    tran0.writeAction("yieldt")
    return efa
