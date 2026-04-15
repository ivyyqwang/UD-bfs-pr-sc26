from EFA_v2 import *
def slsubii_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8029520974569982586, 1, 1677]
    tran0.writeAction("movir X16 37009")
    tran0.writeAction("slorii X16 X16 12 1683")
    tran0.writeAction("slorii X16 X16 12 1858")
    tran0.writeAction("slorii X16 X16 12 851")
    tran0.writeAction("slorii X16 X16 12 1414")
    tran0.writeAction("slsubii X16 X17 1 1677")
    tran0.writeAction("yieldt")
    return efa
