from EFA_v2 import *
def hash_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4662089726198810185, -3501912519514052536]
    tran0.writeAction("movir X16 48972")
    tran0.writeAction("slorii X16 X16 12 3809")
    tran0.writeAction("slorii X16 X16 12 2118")
    tran0.writeAction("slorii X16 X16 12 3775")
    tran0.writeAction("slorii X16 X16 12 2487")
    tran0.writeAction("movir X17 53094")
    tran0.writeAction("slorii X17 X17 12 2897")
    tran0.writeAction("slorii X17 X17 12 3599")
    tran0.writeAction("slorii X17 X17 12 3570")
    tran0.writeAction("slorii X17 X17 12 2120")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
