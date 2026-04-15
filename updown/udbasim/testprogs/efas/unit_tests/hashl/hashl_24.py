from EFA_v2 import *
def hashl_24():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8844918754933189620, 4663546395575826151, 3920056493557504392, -4037997722149883326]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 31423")
    tran0.writeAction("slorii X17 X17 12 1899")
    tran0.writeAction("slorii X17 X17 12 3782")
    tran0.writeAction("slorii X17 X17 12 4026")
    tran0.writeAction("slorii X17 X17 12 3060")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 16568")
    tran0.writeAction("slorii X17 X17 12 1003")
    tran0.writeAction("slorii X17 X17 12 3325")
    tran0.writeAction("slorii X17 X17 12 3483")
    tran0.writeAction("slorii X17 X17 12 1767")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 13926")
    tran0.writeAction("slorii X17 X17 12 3433")
    tran0.writeAction("slorii X17 X17 12 3213")
    tran0.writeAction("slorii X17 X17 12 3925")
    tran0.writeAction("slorii X17 X17 12 2440")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 51190")
    tran0.writeAction("slorii X17 X17 12 615")
    tran0.writeAction("slorii X17 X17 12 1863")
    tran0.writeAction("slorii X17 X17 12 1719")
    tran0.writeAction("slorii X17 X17 12 578")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
