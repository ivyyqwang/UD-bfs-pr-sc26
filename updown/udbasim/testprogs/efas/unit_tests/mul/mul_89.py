from EFA_v2 import *
def mul_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5446934323760187585, 5067390708913961565]
    tran0.writeAction("movir X16 46184")
    tran0.writeAction("slorii X16 X16 12 2465")
    tran0.writeAction("slorii X16 X16 12 1909")
    tran0.writeAction("slorii X16 X16 12 1603")
    tran0.writeAction("slorii X16 X16 12 1855")
    tran0.writeAction("movir X17 18002")
    tran0.writeAction("slorii X17 X17 12 4048")
    tran0.writeAction("slorii X17 X17 12 102")
    tran0.writeAction("slorii X17 X17 12 3815")
    tran0.writeAction("slorii X17 X17 12 2653")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
