from EFA_v2 import *
def add_32():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3414340379715464383, 3888180167431650413]
    tran0.writeAction("movir X16 53405")
    tran0.writeAction("slorii X16 X16 12 3384")
    tran0.writeAction("slorii X16 X16 12 956")
    tran0.writeAction("slorii X16 X16 12 3225")
    tran0.writeAction("slorii X16 X16 12 833")
    tran0.writeAction("movir X17 13813")
    tran0.writeAction("slorii X17 X17 12 2420")
    tran0.writeAction("slorii X17 X17 12 774")
    tran0.writeAction("slorii X17 X17 12 1975")
    tran0.writeAction("slorii X17 X17 12 3181")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
