from EFA_v2 import *
def sraddii_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2312612383149625049, 10, 1314]
    tran0.writeAction("movir X16 8216")
    tran0.writeAction("slorii X16 X16 12 203")
    tran0.writeAction("slorii X16 X16 12 1456")
    tran0.writeAction("slorii X16 X16 12 3288")
    tran0.writeAction("slorii X16 X16 12 3801")
    tran0.writeAction("sraddii X16 X17 10 1314")
    tran0.writeAction("yieldt")
    return efa
