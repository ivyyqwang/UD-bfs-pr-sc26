from EFA_v2 import *
def sladdii_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [57539033014203149, 8, 134]
    tran0.writeAction("movir X16 204")
    tran0.writeAction("slorii X16 X16 12 1719")
    tran0.writeAction("slorii X16 X16 12 535")
    tran0.writeAction("slorii X16 X16 12 2175")
    tran0.writeAction("slorii X16 X16 12 781")
    tran0.writeAction("sladdii X16 X17 8 134")
    tran0.writeAction("yieldt")
    return efa
