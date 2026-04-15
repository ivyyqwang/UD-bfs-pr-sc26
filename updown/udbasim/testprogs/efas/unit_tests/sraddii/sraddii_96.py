from EFA_v2 import *
def sraddii_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8741553452353112031, 5, 1550]
    tran0.writeAction("movir X16 31056")
    tran0.writeAction("slorii X16 X16 12 968")
    tran0.writeAction("slorii X16 X16 12 3288")
    tran0.writeAction("slorii X16 X16 12 2444")
    tran0.writeAction("slorii X16 X16 12 2015")
    tran0.writeAction("sraddii X16 X17 5 1550")
    tran0.writeAction("yieldt")
    return efa
