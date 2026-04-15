from EFA_v2 import *
def hashl_67():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1947605932972382, -1203850236068646807, -9025265985428493647]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 65529")
    tran0.writeAction("slorii X17 X17 12 330")
    tran0.writeAction("slorii X17 X17 12 2472")
    tran0.writeAction("slorii X17 X17 12 830")
    tran0.writeAction("slorii X17 X17 12 1698")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 61259")
    tran0.writeAction("slorii X17 X17 12 265")
    tran0.writeAction("slorii X17 X17 12 1708")
    tran0.writeAction("slorii X17 X17 12 1467")
    tran0.writeAction("slorii X17 X17 12 105")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 33471")
    tran0.writeAction("slorii X17 X17 12 3334")
    tran0.writeAction("slorii X17 X17 12 1911")
    tran0.writeAction("slorii X17 X17 12 486")
    tran0.writeAction("slorii X17 X17 12 2737")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
