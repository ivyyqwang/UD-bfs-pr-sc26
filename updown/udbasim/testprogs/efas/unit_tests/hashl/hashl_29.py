from EFA_v2 import *
def hashl_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [832483424749975063, 4391155688417817755, -942928115743808343, 1267987990344621922]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 2957")
    tran0.writeAction("slorii X17 X17 12 2356")
    tran0.writeAction("slorii X17 X17 12 925")
    tran0.writeAction("slorii X17 X17 12 2551")
    tran0.writeAction("slorii X17 X17 12 1559")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 15600")
    tran0.writeAction("slorii X17 X17 12 2125")
    tran0.writeAction("slorii X17 X17 12 1361")
    tran0.writeAction("slorii X17 X17 12 2375")
    tran0.writeAction("slorii X17 X17 12 1179")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 62186")
    tran0.writeAction("slorii X17 X17 12 189")
    tran0.writeAction("slorii X17 X17 12 4068")
    tran0.writeAction("slorii X17 X17 12 1482")
    tran0.writeAction("slorii X17 X17 12 1193")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 4504")
    tran0.writeAction("slorii X17 X17 12 3269")
    tran0.writeAction("slorii X17 X17 12 3055")
    tran0.writeAction("slorii X17 X17 12 3901")
    tran0.writeAction("slorii X17 X17 12 3938")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
