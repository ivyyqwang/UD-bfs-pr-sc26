from EFA_v2 import *
def hash_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3706901652674915435, 2433451950268309690]
    tran0.writeAction("movir X16 52366")
    tran0.writeAction("slorii X16 X16 12 1801")
    tran0.writeAction("slorii X16 X16 12 1599")
    tran0.writeAction("slorii X16 X16 12 13")
    tran0.writeAction("slorii X16 X16 12 917")
    tran0.writeAction("movir X17 8645")
    tran0.writeAction("slorii X17 X17 12 1466")
    tran0.writeAction("slorii X17 X17 12 2017")
    tran0.writeAction("slorii X17 X17 12 2966")
    tran0.writeAction("slorii X17 X17 12 186")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
