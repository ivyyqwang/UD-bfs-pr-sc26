from EFA_v2 import *
def sladdii_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3770641959907070507, 3, 999]
    tran0.writeAction("movir X16 52139")
    tran0.writeAction("slorii X16 X16 12 4049")
    tran0.writeAction("slorii X16 X16 12 3452")
    tran0.writeAction("slorii X16 X16 12 2278")
    tran0.writeAction("slorii X16 X16 12 3541")
    tran0.writeAction("sladdii X16 X17 3 999")
    tran0.writeAction("yieldt")
    return efa
