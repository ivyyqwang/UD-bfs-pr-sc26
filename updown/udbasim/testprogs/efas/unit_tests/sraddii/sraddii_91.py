from EFA_v2 import *
def sraddii_91():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-567944106611882852, 10, 739]
    tran0.writeAction("movir X16 63518")
    tran0.writeAction("slorii X16 X16 12 1053")
    tran0.writeAction("slorii X16 X16 12 2073")
    tran0.writeAction("slorii X16 X16 12 500")
    tran0.writeAction("slorii X16 X16 12 1180")
    tran0.writeAction("sraddii X16 X17 10 739")
    tran0.writeAction("yieldt")
    return efa
