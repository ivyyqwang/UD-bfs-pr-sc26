from EFA_v2 import *
def hash_25():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-6264648145085765790, 3111834076085672063]
    tran0.writeAction("movir X16 43279")
    tran0.writeAction("slorii X16 X16 12 2043")
    tran0.writeAction("slorii X16 X16 12 1053")
    tran0.writeAction("slorii X16 X16 12 1446")
    tran0.writeAction("slorii X16 X16 12 1890")
    tran0.writeAction("movir X17 11055")
    tran0.writeAction("slorii X17 X17 12 1865")
    tran0.writeAction("slorii X17 X17 12 2785")
    tran0.writeAction("slorii X17 X17 12 173")
    tran0.writeAction("slorii X17 X17 12 2175")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
