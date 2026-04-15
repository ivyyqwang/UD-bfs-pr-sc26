from EFA_v2 import *
def sraddii_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1354292337488597668, 8, 1304]
    tran0.writeAction("movir X16 60724")
    tran0.writeAction("slorii X16 X16 12 2404")
    tran0.writeAction("slorii X16 X16 12 2909")
    tran0.writeAction("slorii X16 X16 12 3926")
    tran0.writeAction("slorii X16 X16 12 3420")
    tran0.writeAction("sraddii X16 X17 8 1304")
    tran0.writeAction("yieldt")
    return efa
