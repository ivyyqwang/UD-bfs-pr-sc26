from EFA_v2 import *
def mul_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3908543290426598968, -6834369656291914400]
    tran0.writeAction("movir X16 13885")
    tran0.writeAction("slorii X16 X16 12 3830")
    tran0.writeAction("slorii X16 X16 12 2575")
    tran0.writeAction("slorii X16 X16 12 466")
    tran0.writeAction("slorii X16 X16 12 1592")
    tran0.writeAction("movir X17 41255")
    tran0.writeAction("slorii X17 X17 12 1808")
    tran0.writeAction("slorii X17 X17 12 501")
    tran0.writeAction("slorii X17 X17 12 48")
    tran0.writeAction("slorii X17 X17 12 3424")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
