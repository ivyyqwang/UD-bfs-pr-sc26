from EFA_v2 import *
def hashl_78():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-536172335382399134, -1968319164534640098, -6048682248832452039]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 63631")
    tran0.writeAction("slorii X17 X17 12 545")
    tran0.writeAction("slorii X17 X17 12 2571")
    tran0.writeAction("slorii X17 X17 12 575")
    tran0.writeAction("slorii X17 X17 12 1890")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 58543")
    tran0.writeAction("slorii X17 X17 12 514")
    tran0.writeAction("slorii X17 X17 12 1537")
    tran0.writeAction("slorii X17 X17 12 1307")
    tran0.writeAction("slorii X17 X17 12 542")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 44046")
    tran0.writeAction("slorii X17 X17 12 3128")
    tran0.writeAction("slorii X17 X17 12 2751")
    tran0.writeAction("slorii X17 X17 12 535")
    tran0.writeAction("slorii X17 X17 12 2617")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
