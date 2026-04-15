from EFA_v2 import *
def div_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-563302807575807137, -1511699853197094749]
    tran0.writeAction("movir X16 63534")
    tran0.writeAction("slorii X16 X16 12 3057")
    tran0.writeAction("slorii X16 X16 12 1213")
    tran0.writeAction("slorii X16 X16 12 1899")
    tran0.writeAction("slorii X16 X16 12 2911")
    tran0.writeAction("movir X17 60165")
    tran0.writeAction("slorii X17 X17 12 1487")
    tran0.writeAction("slorii X17 X17 12 3627")
    tran0.writeAction("slorii X17 X17 12 725")
    tran0.writeAction("slorii X17 X17 12 163")
    tran0.writeAction("div X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
