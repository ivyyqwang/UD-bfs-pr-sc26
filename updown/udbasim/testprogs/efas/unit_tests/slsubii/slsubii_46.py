from EFA_v2 import *
def slsubii_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [60258731701302677, 11, 1013]
    tran0.writeAction("movir X16 214")
    tran0.writeAction("slorii X16 X16 12 335")
    tran0.writeAction("slorii X16 X16 12 3913")
    tran0.writeAction("slorii X16 X16 12 2751")
    tran0.writeAction("slorii X16 X16 12 1429")
    tran0.writeAction("slsubii X16 X17 11 1013")
    tran0.writeAction("yieldt")
    return efa
