from EFA_v2 import *
def hashl_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6671412201329622482, 6625534736347046857, -8919761314139481381]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 23701")
    tran0.writeAction("slorii X17 X17 12 2528")
    tran0.writeAction("slorii X17 X17 12 3306")
    tran0.writeAction("slorii X17 X17 12 1879")
    tran0.writeAction("slorii X17 X17 12 3538")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 23538")
    tran0.writeAction("slorii X17 X17 12 2571")
    tran0.writeAction("slorii X17 X17 12 3382")
    tran0.writeAction("slorii X17 X17 12 4002")
    tran0.writeAction("slorii X17 X17 12 969")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 33846")
    tran0.writeAction("slorii X17 X17 12 2629")
    tran0.writeAction("slorii X17 X17 12 2045")
    tran0.writeAction("slorii X17 X17 12 1821")
    tran0.writeAction("slorii X17 X17 12 2779")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
