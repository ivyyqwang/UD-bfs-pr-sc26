from EFA_v2 import *
def slsubii_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5451949049686623779, 14, 47]
    tran0.writeAction("movir X16 19369")
    tran0.writeAction("slorii X16 X16 12 876")
    tran0.writeAction("slorii X16 X16 12 1640")
    tran0.writeAction("slorii X16 X16 12 408")
    tran0.writeAction("slorii X16 X16 12 1571")
    tran0.writeAction("slsubii X16 X17 14 47")
    tran0.writeAction("yieldt")
    return efa
