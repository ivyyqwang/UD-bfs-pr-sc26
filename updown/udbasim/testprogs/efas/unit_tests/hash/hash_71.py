from EFA_v2 import *
def hash_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4643070118366747123, -8862848994825917660]
    tran0.writeAction("movir X16 16495")
    tran0.writeAction("slorii X16 X16 12 2042")
    tran0.writeAction("slorii X16 X16 12 3120")
    tran0.writeAction("slorii X16 X16 12 1969")
    tran0.writeAction("slorii X16 X16 12 2547")
    tran0.writeAction("movir X17 34048")
    tran0.writeAction("slorii X17 X17 12 3420")
    tran0.writeAction("slorii X17 X17 12 3053")
    tran0.writeAction("slorii X17 X17 12 1938")
    tran0.writeAction("slorii X17 X17 12 2852")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
