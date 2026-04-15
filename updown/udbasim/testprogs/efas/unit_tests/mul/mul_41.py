from EFA_v2 import *
def mul_41():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6136693535191636154, -4410808406871099306]
    tran0.writeAction("movir X16 21801")
    tran0.writeAction("slorii X16 X16 12 3748")
    tran0.writeAction("slorii X16 X16 12 436")
    tran0.writeAction("slorii X16 X16 12 2185")
    tran0.writeAction("slorii X16 X16 12 2234")
    tran0.writeAction("movir X17 49865")
    tran0.writeAction("slorii X17 X17 12 2705")
    tran0.writeAction("slorii X17 X17 12 3992")
    tran0.writeAction("slorii X17 X17 12 579")
    tran0.writeAction("slorii X17 X17 12 2134")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
