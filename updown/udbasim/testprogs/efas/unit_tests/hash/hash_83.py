from EFA_v2 import *
def hash_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4987677338964741086, 6133720955710281089]
    tran0.writeAction("movir X16 17719")
    tran0.writeAction("slorii X16 X16 12 3233")
    tran0.writeAction("slorii X16 X16 12 3371")
    tran0.writeAction("slorii X16 X16 12 1060")
    tran0.writeAction("slorii X16 X16 12 3038")
    tran0.writeAction("movir X17 21791")
    tran0.writeAction("slorii X17 X17 12 1451")
    tran0.writeAction("slorii X17 X17 12 1564")
    tran0.writeAction("slorii X17 X17 12 1969")
    tran0.writeAction("slorii X17 X17 12 1409")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
