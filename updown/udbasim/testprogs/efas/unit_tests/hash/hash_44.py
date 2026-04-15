from EFA_v2 import *
def hash_44():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4811998876550843480, 3622492292553981499]
    tran0.writeAction("movir X16 17095")
    tran0.writeAction("slorii X16 X16 12 2679")
    tran0.writeAction("slorii X16 X16 12 2992")
    tran0.writeAction("slorii X16 X16 12 1604")
    tran0.writeAction("slorii X16 X16 12 3160")
    tran0.writeAction("movir X17 12869")
    tran0.writeAction("slorii X17 X17 12 2776")
    tran0.writeAction("slorii X17 X17 12 3099")
    tran0.writeAction("slorii X17 X17 12 1107")
    tran0.writeAction("slorii X17 X17 12 3643")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
