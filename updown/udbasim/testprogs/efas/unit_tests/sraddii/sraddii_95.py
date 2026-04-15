from EFA_v2 import *
def sraddii_95():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6624722097171727178, 3, 1422]
    tran0.writeAction("movir X16 42000")
    tran0.writeAction("slorii X16 X16 12 1061")
    tran0.writeAction("slorii X16 X16 12 2582")
    tran0.writeAction("slorii X16 X16 12 1631")
    tran0.writeAction("slorii X16 X16 12 3254")
    tran0.writeAction("sraddii X16 X17 3 1422")
    tran0.writeAction("yieldt")
    return efa
