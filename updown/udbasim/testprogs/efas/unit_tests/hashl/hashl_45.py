from EFA_v2 import *
def hashl_45():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8310344743949488338, 8133615022294654739, 3650686452268226277]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 36011")
    tran0.writeAction("slorii X17 X17 12 2967")
    tran0.writeAction("slorii X17 X17 12 3143")
    tran0.writeAction("slorii X17 X17 12 3506")
    tran0.writeAction("slorii X17 X17 12 3886")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 28896")
    tran0.writeAction("slorii X17 X17 12 1660")
    tran0.writeAction("slorii X17 X17 12 1247")
    tran0.writeAction("slorii X17 X17 12 2677")
    tran0.writeAction("slorii X17 X17 12 3859")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 12969")
    tran0.writeAction("slorii X17 X17 12 3455")
    tran0.writeAction("slorii X17 X17 12 3189")
    tran0.writeAction("slorii X17 X17 12 3189")
    tran0.writeAction("slorii X17 X17 12 1765")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
