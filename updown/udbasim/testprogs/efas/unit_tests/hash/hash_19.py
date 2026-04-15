from EFA_v2 import *
def hash_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [32357798244211954, 498714382266821595]
    tran0.writeAction("movir X16 114")
    tran0.writeAction("slorii X16 X16 12 3923")
    tran0.writeAction("slorii X16 X16 12 3838")
    tran0.writeAction("slorii X16 X16 12 245")
    tran0.writeAction("slorii X16 X16 12 3314")
    tran0.writeAction("movir X17 1771")
    tran0.writeAction("slorii X17 X17 12 3233")
    tran0.writeAction("slorii X17 X17 12 1695")
    tran0.writeAction("slorii X17 X17 12 1606")
    tran0.writeAction("slorii X17 X17 12 3035")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
