from EFA_v2 import *
def sraddii_87():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4623312421351051853, 8, 1997]
    tran0.writeAction("movir X16 49110")
    tran0.writeAction("slorii X16 X16 12 2845")
    tran0.writeAction("slorii X16 X16 12 2335")
    tran0.writeAction("slorii X16 X16 12 2946")
    tran0.writeAction("slorii X16 X16 12 3507")
    tran0.writeAction("sraddii X16 X17 8 1997")
    tran0.writeAction("yieldt")
    return efa
