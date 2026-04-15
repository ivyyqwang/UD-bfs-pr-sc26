from EFA_v2 import *
def add_88():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3230799864298043035, 3827886862004068940]
    tran0.writeAction("movir X16 11478")
    tran0.writeAction("slorii X16 X16 12 437")
    tran0.writeAction("slorii X16 X16 12 3051")
    tran0.writeAction("slorii X16 X16 12 3543")
    tran0.writeAction("slorii X16 X16 12 1691")
    tran0.writeAction("movir X17 13599")
    tran0.writeAction("slorii X17 X17 12 1581")
    tran0.writeAction("slorii X17 X17 12 490")
    tran0.writeAction("slorii X17 X17 12 562")
    tran0.writeAction("slorii X17 X17 12 588")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
