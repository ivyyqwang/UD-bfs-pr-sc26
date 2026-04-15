from EFA_v2 import *
def slsubii_52():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2143738106830142219, 14, 1176]
    tran0.writeAction("movir X16 57919")
    tran0.writeAction("slorii X16 X16 12 3736")
    tran0.writeAction("slorii X16 X16 12 3266")
    tran0.writeAction("slorii X16 X16 12 3772")
    tran0.writeAction("slorii X16 X16 12 1269")
    tran0.writeAction("slsubii X16 X17 14 1176")
    tran0.writeAction("yieldt")
    return efa
