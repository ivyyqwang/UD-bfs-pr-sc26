from EFA_v2 import *
def add_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [162903953785851222, -5872403654552375380]
    tran0.writeAction("movir X16 578")
    tran0.writeAction("slorii X16 X16 12 3076")
    tran0.writeAction("slorii X16 X16 12 2153")
    tran0.writeAction("slorii X16 X16 12 3736")
    tran0.writeAction("slorii X16 X16 12 3414")
    tran0.writeAction("movir X17 44673")
    tran0.writeAction("slorii X17 X17 12 127")
    tran0.writeAction("slorii X17 X17 12 3408")
    tran0.writeAction("slorii X17 X17 12 2866")
    tran0.writeAction("slorii X17 X17 12 4012")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
