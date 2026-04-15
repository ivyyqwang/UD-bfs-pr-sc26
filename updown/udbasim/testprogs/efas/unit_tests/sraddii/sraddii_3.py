from EFA_v2 import *
def sraddii_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3293547119186006849, 1, 434]
    tran0.writeAction("movir X16 11701")
    tran0.writeAction("slorii X16 X16 12 122")
    tran0.writeAction("slorii X16 X16 12 1962")
    tran0.writeAction("slorii X16 X16 12 381")
    tran0.writeAction("slorii X16 X16 12 833")
    tran0.writeAction("sraddii X16 X17 1 434")
    tran0.writeAction("yieldt")
    return efa
