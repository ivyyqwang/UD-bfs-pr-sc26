from EFA_v2 import *
def sladdii_28():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1394236418793877032, 5, 1335]
    tran0.writeAction("movir X16 60582")
    tran0.writeAction("slorii X16 X16 12 2773")
    tran0.writeAction("slorii X16 X16 12 3380")
    tran0.writeAction("slorii X16 X16 12 3597")
    tran0.writeAction("slorii X16 X16 12 472")
    tran0.writeAction("sladdii X16 X17 5 1335")
    tran0.writeAction("yieldt")
    return efa
