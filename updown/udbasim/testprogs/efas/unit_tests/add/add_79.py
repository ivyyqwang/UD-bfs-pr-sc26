from EFA_v2 import *
def add_79():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1301248857277158093, -7720734754644196551]
    tran0.writeAction("movir X16 60913")
    tran0.writeAction("slorii X16 X16 12 144")
    tran0.writeAction("slorii X16 X16 12 3841")
    tran0.writeAction("slorii X16 X16 12 2506")
    tran0.writeAction("slorii X16 X16 12 3379")
    tran0.writeAction("movir X17 38106")
    tran0.writeAction("slorii X17 X17 12 1802")
    tran0.writeAction("slorii X17 X17 12 1432")
    tran0.writeAction("slorii X17 X17 12 1720")
    tran0.writeAction("slorii X17 X17 12 825")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
