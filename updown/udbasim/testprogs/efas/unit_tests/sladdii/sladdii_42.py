from EFA_v2 import *
def sladdii_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1544397808185361987, 13, 215]
    tran0.writeAction("movir X16 60049")
    tran0.writeAction("slorii X16 X16 12 806")
    tran0.writeAction("slorii X16 X16 12 67")
    tran0.writeAction("slorii X16 X16 12 899")
    tran0.writeAction("slorii X16 X16 12 2493")
    tran0.writeAction("sladdii X16 X17 13 215")
    tran0.writeAction("yieldt")
    return efa
