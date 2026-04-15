from EFA_v2 import *
def hash_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5192901034344879112, 2164713313743148164]
    tran0.writeAction("movir X16 47087")
    tran0.writeAction("slorii X16 X16 12 448")
    tran0.writeAction("slorii X16 X16 12 1470")
    tran0.writeAction("slorii X16 X16 12 470")
    tran0.writeAction("slorii X16 X16 12 3064")
    tran0.writeAction("movir X17 7690")
    tran0.writeAction("slorii X17 X17 12 2484")
    tran0.writeAction("slorii X17 X17 12 2602")
    tran0.writeAction("slorii X17 X17 12 897")
    tran0.writeAction("slorii X17 X17 12 1156")
    tran0.writeAction("hash X16 X17")
    tran0.writeAction("yieldt")
    return efa
