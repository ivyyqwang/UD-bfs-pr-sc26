from EFA_v2 import *
def sraddii_98():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8021747575052802285, 8, 1462]
    tran0.writeAction("movir X16 28498")
    tran0.writeAction("slorii X16 X16 12 3982")
    tran0.writeAction("slorii X16 X16 12 2848")
    tran0.writeAction("slorii X16 X16 12 3577")
    tran0.writeAction("slorii X16 X16 12 2285")
    tran0.writeAction("sraddii X16 X17 8 1462")
    tran0.writeAction("yieldt")
    return efa
