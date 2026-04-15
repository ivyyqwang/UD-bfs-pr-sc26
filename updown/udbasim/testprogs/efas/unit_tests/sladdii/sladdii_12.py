from EFA_v2 import *
def sladdii_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1765647745283676521, 7, 1682]
    tran0.writeAction("movir X16 6272")
    tran0.writeAction("slorii X16 X16 12 3444")
    tran0.writeAction("slorii X16 X16 12 1280")
    tran0.writeAction("slorii X16 X16 12 421")
    tran0.writeAction("slorii X16 X16 12 2409")
    tran0.writeAction("sladdii X16 X17 7 1682")
    tran0.writeAction("yieldt")
    return efa
