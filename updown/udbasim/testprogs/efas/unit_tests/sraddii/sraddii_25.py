from EFA_v2 import *
def sraddii_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3583176293274223417, 14, 1705]
    tran0.writeAction("movir X16 52806")
    tran0.writeAction("slorii X16 X16 12 2")
    tran0.writeAction("slorii X16 X16 12 1359")
    tran0.writeAction("slorii X16 X16 12 3231")
    tran0.writeAction("slorii X16 X16 12 3271")
    tran0.writeAction("sraddii X16 X17 14 1705")
    tran0.writeAction("yieldt")
    return efa
