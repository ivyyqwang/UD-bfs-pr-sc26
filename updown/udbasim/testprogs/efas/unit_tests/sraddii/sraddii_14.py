from EFA_v2 import *
def sraddii_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-825170949429409301, 1, 1057]
    tran0.writeAction("movir X16 62604")
    tran0.writeAction("slorii X16 X16 12 1654")
    tran0.writeAction("slorii X16 X16 12 1208")
    tran0.writeAction("slorii X16 X16 12 1180")
    tran0.writeAction("slorii X16 X16 12 2539")
    tran0.writeAction("sraddii X16 X17 1 1057")
    tran0.writeAction("yieldt")
    return efa
