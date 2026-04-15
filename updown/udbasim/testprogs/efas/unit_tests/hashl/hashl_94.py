from EFA_v2 import *
def hashl_94():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8122976256701322532, -6877724574532290633, 4970650762502842867, -8524697395948439844]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 36677")
    tran0.writeAction("slorii X17 X17 12 1602")
    tran0.writeAction("slorii X17 X17 12 452")
    tran0.writeAction("slorii X17 X17 12 1578")
    tran0.writeAction("slorii X17 X17 12 2780")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 41101")
    tran0.writeAction("slorii X17 X17 12 1695")
    tran0.writeAction("slorii X17 X17 12 112")
    tran0.writeAction("slorii X17 X17 12 115")
    tran0.writeAction("slorii X17 X17 12 1975")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 17659")
    tran0.writeAction("slorii X17 X17 12 1224")
    tran0.writeAction("slorii X17 X17 12 2153")
    tran0.writeAction("slorii X17 X17 12 2074")
    tran0.writeAction("slorii X17 X17 12 2547")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 35250")
    tran0.writeAction("slorii X17 X17 12 782")
    tran0.writeAction("slorii X17 X17 12 600")
    tran0.writeAction("slorii X17 X17 12 3259")
    tran0.writeAction("slorii X17 X17 12 1756")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
