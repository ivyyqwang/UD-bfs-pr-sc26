from EFA_v2 import *
def sraddii_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-63302294091105779, 6, 26]
    tran0.writeAction("movir X16 65311")
    tran0.writeAction("slorii X16 X16 12 430")
    tran0.writeAction("slorii X16 X16 12 1567")
    tran0.writeAction("slorii X16 X16 12 951")
    tran0.writeAction("slorii X16 X16 12 2573")
    tran0.writeAction("sraddii X16 X17 6 26")
    tran0.writeAction("yieldt")
    return efa
