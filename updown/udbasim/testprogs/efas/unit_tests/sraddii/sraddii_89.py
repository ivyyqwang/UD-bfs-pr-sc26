from EFA_v2 import *
def sraddii_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8615893543156894346, 15, 511]
    tran0.writeAction("movir X16 34926")
    tran0.writeAction("slorii X16 X16 12 807")
    tran0.writeAction("slorii X16 X16 12 2225")
    tran0.writeAction("slorii X16 X16 12 2259")
    tran0.writeAction("slorii X16 X16 12 1398")
    tran0.writeAction("sraddii X16 X17 15 511")
    tran0.writeAction("yieldt")
    return efa
