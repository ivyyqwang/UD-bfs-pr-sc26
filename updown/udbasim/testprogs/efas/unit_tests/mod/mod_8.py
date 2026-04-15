from EFA_v2 import *
def mod_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [731503388667507538, -1629243054170070648]
    tran0.writeAction("movir X16 2598")
    tran0.writeAction("slorii X16 X16 12 3367")
    tran0.writeAction("slorii X16 X16 12 1233")
    tran0.writeAction("slorii X16 X16 12 2135")
    tran0.writeAction("slorii X16 X16 12 850")
    tran0.writeAction("movir X17 59747")
    tran0.writeAction("slorii X17 X17 12 3137")
    tran0.writeAction("slorii X17 X17 12 775")
    tran0.writeAction("slorii X17 X17 12 1722")
    tran0.writeAction("slorii X17 X17 12 392")
    tran0.writeAction("mod X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
