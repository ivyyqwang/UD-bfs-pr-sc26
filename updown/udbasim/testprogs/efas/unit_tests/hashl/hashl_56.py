from EFA_v2 import *
def hashl_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1944156078716705680, -5804285184013112485, 870534202409952266, -5647425032393501541]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 6907")
    tran0.writeAction("slorii X17 X17 12 122")
    tran0.writeAction("slorii X17 X17 12 1835")
    tran0.writeAction("slorii X17 X17 12 3381")
    tran0.writeAction("slorii X17 X17 12 2960")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 44915")
    tran0.writeAction("slorii X17 X17 12 150")
    tran0.writeAction("slorii X17 X17 12 167")
    tran0.writeAction("slorii X17 X17 12 3422")
    tran0.writeAction("slorii X17 X17 12 2907")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 3092")
    tran0.writeAction("slorii X17 X17 12 3107")
    tran0.writeAction("slorii X17 X17 12 3755")
    tran0.writeAction("slorii X17 X17 12 1938")
    tran0.writeAction("slorii X17 X17 12 1034")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 45472")
    tran0.writeAction("slorii X17 X17 12 1293")
    tran0.writeAction("slorii X17 X17 12 2744")
    tran0.writeAction("slorii X17 X17 12 2197")
    tran0.writeAction("slorii X17 X17 12 1179")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
