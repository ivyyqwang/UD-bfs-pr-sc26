from EFA_v2 import *
def hashl_33():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-5425760331925170001, 5943170538366445188, 2602972369198724365]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 46259")
    tran0.writeAction("slorii X17 X17 12 3387")
    tran0.writeAction("slorii X17 X17 12 2459")
    tran0.writeAction("slorii X17 X17 12 797")
    tran0.writeAction("slorii X17 X17 12 2223")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 21114")
    tran0.writeAction("slorii X17 X17 12 1569")
    tran0.writeAction("slorii X17 X17 12 3530")
    tran0.writeAction("slorii X17 X17 12 3682")
    tran0.writeAction("slorii X17 X17 12 1668")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 9247")
    tran0.writeAction("slorii X17 X17 12 2521")
    tran0.writeAction("slorii X17 X17 12 1058")
    tran0.writeAction("slorii X17 X17 12 1011")
    tran0.writeAction("slorii X17 X17 12 1293")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
