from EFA_v2 import *
def sraddii_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1774559052195716588, 3, 271]
    tran0.writeAction("movir X16 59231")
    tran0.writeAction("slorii X16 X16 12 2047")
    tran0.writeAction("slorii X16 X16 12 428")
    tran0.writeAction("slorii X16 X16 12 3770")
    tran0.writeAction("slorii X16 X16 12 532")
    tran0.writeAction("sraddii X16 X17 3 271")
    tran0.writeAction("yieldt")
    return efa
