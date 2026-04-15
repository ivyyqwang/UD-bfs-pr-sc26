from EFA_v2 import *
def add_60():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [9019697342836068020, -8633656143672437687]
    tran0.writeAction("movir X16 32044")
    tran0.writeAction("slorii X16 X16 12 1647")
    tran0.writeAction("slorii X16 X16 12 485")
    tran0.writeAction("slorii X16 X16 12 1140")
    tran0.writeAction("slorii X16 X16 12 3764")
    tran0.writeAction("movir X17 34863")
    tran0.writeAction("slorii X17 X17 12 375")
    tran0.writeAction("slorii X17 X17 12 2811")
    tran0.writeAction("slorii X17 X17 12 2193")
    tran0.writeAction("slorii X17 X17 12 1097")
    tran0.writeAction("add X16 X17 X17 ")
    tran0.writeAction("yieldt")
    return efa
