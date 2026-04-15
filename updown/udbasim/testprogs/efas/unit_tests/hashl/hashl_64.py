from EFA_v2 import *
def hashl_64():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-4922348601233640553, -1607091710446250371]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 48048")
    tran0.writeAction("slorii X17 X17 12 1248")
    tran0.writeAction("slorii X17 X17 12 1762")
    tran0.writeAction("slorii X17 X17 12 3391")
    tran0.writeAction("slorii X17 X17 12 919")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 59826")
    tran0.writeAction("slorii X17 X17 12 1897")
    tran0.writeAction("slorii X17 X17 12 2725")
    tran0.writeAction("slorii X17 X17 12 1541")
    tran0.writeAction("slorii X17 X17 12 1661")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
