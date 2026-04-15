from EFA_v2 import *
def add_93():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8818022739739877494, 7539856706645067490]
    tran0.writeAction("movir X16 34208")
    tran0.writeAction("slorii X16 X16 12 368")
    tran0.writeAction("slorii X16 X16 12 2496")
    tran0.writeAction("slorii X16 X16 12 1997")
    tran0.writeAction("slorii X16 X16 12 3978")
    tran0.writeAction("movir X17 26786")
    tran0.writeAction("slorii X17 X17 12 3899")
    tran0.writeAction("slorii X17 X17 12 2576")
    tran0.writeAction("slorii X17 X17 12 3792")
    tran0.writeAction("slorii X17 X17 12 1762")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
