from EFA_v2 import *
def hashl_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4190976726259965640, -5599918561033502135, -69054447662009365, 8833016030865182124]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 14889")
    tran0.writeAction("slorii X17 X17 12 1394")
    tran0.writeAction("slorii X17 X17 12 182")
    tran0.writeAction("slorii X17 X17 12 2681")
    tran0.writeAction("slorii X17 X17 12 3784")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 45641")
    tran0.writeAction("slorii X17 X17 12 379")
    tran0.writeAction("slorii X17 X17 12 3334")
    tran0.writeAction("slorii X17 X17 12 1972")
    tran0.writeAction("slorii X17 X17 12 585")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 65290")
    tran0.writeAction("slorii X17 X17 12 2741")
    tran0.writeAction("slorii X17 X17 12 2176")
    tran0.writeAction("slorii X17 X17 12 3871")
    tran0.writeAction("slorii X17 X17 12 1003")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 31381")
    tran0.writeAction("slorii X17 X17 12 724")
    tran0.writeAction("slorii X17 X17 12 2015")
    tran0.writeAction("slorii X17 X17 12 204")
    tran0.writeAction("slorii X17 X17 12 3500")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
