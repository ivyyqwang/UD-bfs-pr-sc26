from EFA_v2 import *
def sub_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7054164101029761211, 7997895566926013872]
    tran0.writeAction("movir X16 40474")
    tran0.writeAction("slorii X16 X16 12 2353")
    tran0.writeAction("slorii X16 X16 12 4074")
    tran0.writeAction("slorii X16 X16 12 3310")
    tran0.writeAction("slorii X16 X16 12 3909")
    tran0.writeAction("movir X17 28414")
    tran0.writeAction("slorii X17 X17 12 954")
    tran0.writeAction("slorii X17 X17 12 1209")
    tran0.writeAction("slorii X17 X17 12 1214")
    tran0.writeAction("slorii X17 X17 12 1456")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
