from EFA_v2 import *
def slsubii_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7316091503902320147, 0, 1377]
    tran0.writeAction("movir X16 39544")
    tran0.writeAction("slorii X16 X16 12 88")
    tran0.writeAction("slorii X16 X16 12 2589")
    tran0.writeAction("slorii X16 X16 12 2657")
    tran0.writeAction("slorii X16 X16 12 2541")
    tran0.writeAction("slsubii X16 X17 0 1377")
    tran0.writeAction("yieldt")
    return efa
