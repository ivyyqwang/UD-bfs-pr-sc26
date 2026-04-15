from EFA_v2 import *
def sraddii_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2045678635307300401, 7, 764]
    tran0.writeAction("movir X16 7267")
    tran0.writeAction("slorii X16 X16 12 2910")
    tran0.writeAction("slorii X16 X16 12 350")
    tran0.writeAction("slorii X16 X16 12 399")
    tran0.writeAction("slorii X16 X16 12 1585")
    tran0.writeAction("sraddii X16 X17 7 764")
    tran0.writeAction("yieldt")
    return efa
