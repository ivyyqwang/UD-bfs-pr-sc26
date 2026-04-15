from EFA_v2 import *
def mul_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8462863950984991090, -4950650382708231303]
    tran0.writeAction("movir X16 35469")
    tran0.writeAction("slorii X16 X16 12 3553")
    tran0.writeAction("slorii X16 X16 12 803")
    tran0.writeAction("slorii X16 X16 12 330")
    tran0.writeAction("slorii X16 X16 12 3726")
    tran0.writeAction("movir X17 47947")
    tran0.writeAction("slorii X17 X17 12 3099")
    tran0.writeAction("slorii X17 X17 12 1251")
    tran0.writeAction("slorii X17 X17 12 2147")
    tran0.writeAction("slorii X17 X17 12 889")
    tran0.writeAction("mul X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
