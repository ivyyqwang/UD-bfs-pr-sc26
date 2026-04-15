from EFA_v2 import *
def slsubii_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7241420766280121413, 6, 57]
    tran0.writeAction("movir X16 25726")
    tran0.writeAction("slorii X16 X16 12 2845")
    tran0.writeAction("slorii X16 X16 12 507")
    tran0.writeAction("slorii X16 X16 12 1079")
    tran0.writeAction("slorii X16 X16 12 3141")
    tran0.writeAction("slsubii X16 X17 6 57")
    tran0.writeAction("yieldt")
    return efa
