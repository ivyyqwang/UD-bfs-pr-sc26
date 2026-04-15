from EFA_v2 import *
def sraddii_65():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [409284380843039438, 12, 175]
    tran0.writeAction("movir X16 1454")
    tran0.writeAction("slorii X16 X16 12 287")
    tran0.writeAction("slorii X16 X16 12 2516")
    tran0.writeAction("slorii X16 X16 12 1085")
    tran0.writeAction("slorii X16 X16 12 2766")
    tran0.writeAction("sraddii X16 X17 12 175")
    tran0.writeAction("yieldt")
    return efa
