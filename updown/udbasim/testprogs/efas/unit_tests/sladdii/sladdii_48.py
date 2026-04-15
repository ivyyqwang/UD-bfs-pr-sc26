from EFA_v2 import *
def sladdii_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-331376283303738208, 9, 460]
    tran0.writeAction("movir X16 64358")
    tran0.writeAction("slorii X16 X16 12 2928")
    tran0.writeAction("slorii X16 X16 12 1706")
    tran0.writeAction("slorii X16 X16 12 2832")
    tran0.writeAction("slorii X16 X16 12 1184")
    tran0.writeAction("sladdii X16 X17 9 460")
    tran0.writeAction("yieldt")
    return efa
