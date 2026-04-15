from EFA_v2 import *
def hashl_27():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6652756069938950983, -7544685730104930008]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 23635")
    tran0.writeAction("slorii X17 X17 12 1382")
    tran0.writeAction("slorii X17 X17 12 1494")
    tran0.writeAction("slorii X17 X17 12 143")
    tran0.writeAction("slorii X17 X17 12 839")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 38731")
    tran0.writeAction("slorii X17 X17 12 3652")
    tran0.writeAction("slorii X17 X17 12 3403")
    tran0.writeAction("slorii X17 X17 12 561")
    tran0.writeAction("slorii X17 X17 12 296")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
