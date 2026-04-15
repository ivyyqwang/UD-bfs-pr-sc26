from EFA_v2 import *
def sub_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8078043982451639074, 921620864029534046]
    tran0.writeAction("movir X16 36837")
    tran0.writeAction("slorii X16 X16 12 92")
    tran0.writeAction("slorii X16 X16 12 3097")
    tran0.writeAction("slorii X16 X16 12 4047")
    tran0.writeAction("slorii X16 X16 12 3294")
    tran0.writeAction("movir X17 3274")
    tran0.writeAction("slorii X17 X17 12 1044")
    tran0.writeAction("slorii X17 X17 12 2810")
    tran0.writeAction("slorii X17 X17 12 282")
    tran0.writeAction("slorii X17 X17 12 1886")
    tran0.writeAction("sub X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
