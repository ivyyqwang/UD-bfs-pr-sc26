from EFA_v2 import *
def mul_61():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1849103481326011779, 4168332716988520698]
    tran0.writeAction("movir X16 58966")
    tran0.writeAction("slorii X16 X16 12 2722")
    tran0.writeAction("slorii X16 X16 12 3650")
    tran0.writeAction("slorii X16 X16 12 2559")
    tran0.writeAction("slorii X16 X16 12 2685")
    tran0.writeAction("movir X17 14808")
    tran0.writeAction("slorii X17 X17 12 3656")
    tran0.writeAction("slorii X17 X17 12 1397")
    tran0.writeAction("slorii X17 X17 12 3029")
    tran0.writeAction("slorii X17 X17 12 2298")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
