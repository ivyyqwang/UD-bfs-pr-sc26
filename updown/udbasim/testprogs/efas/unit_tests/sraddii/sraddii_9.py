from EFA_v2 import *
def sraddii_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4719070490994304012, 15, 1819]
    tran0.writeAction("movir X16 16765")
    tran0.writeAction("slorii X16 X16 12 2073")
    tran0.writeAction("slorii X16 X16 12 3037")
    tran0.writeAction("slorii X16 X16 12 3046")
    tran0.writeAction("slorii X16 X16 12 1036")
    tran0.writeAction("sraddii X16 X17 15 1819")
    tran0.writeAction("yieldt")
    return efa
