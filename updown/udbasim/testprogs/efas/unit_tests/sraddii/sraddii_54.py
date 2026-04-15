from EFA_v2 import *
def sraddii_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2409500945032486699, 1, 466]
    tran0.writeAction("movir X16 8560")
    tran0.writeAction("slorii X16 X16 12 1093")
    tran0.writeAction("slorii X16 X16 12 2026")
    tran0.writeAction("slorii X16 X16 12 2577")
    tran0.writeAction("slorii X16 X16 12 3883")
    tran0.writeAction("sraddii X16 X17 1 466")
    tran0.writeAction("yieldt")
    return efa
