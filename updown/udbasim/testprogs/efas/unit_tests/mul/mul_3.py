from EFA_v2 import *
def mul_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8642963993667413356, 9184153845238752950]
    tran0.writeAction("movir X16 30705")
    tran0.writeAction("slorii X16 X16 12 3999")
    tran0.writeAction("slorii X16 X16 12 1465")
    tran0.writeAction("slorii X16 X16 12 154")
    tran0.writeAction("slorii X16 X16 12 1388")
    tran0.writeAction("movir X17 32628")
    tran0.writeAction("slorii X17 X17 12 2740")
    tran0.writeAction("slorii X17 X17 12 819")
    tran0.writeAction("slorii X17 X17 12 4070")
    tran0.writeAction("slorii X17 X17 12 1718")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
