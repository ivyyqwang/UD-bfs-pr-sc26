from EFA_v2 import *
def hashl_59():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5201371033320909476, -7492410825228940293, -9064531579167632190]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 18478")
    tran0.writeAction("slorii X17 X17 12 4022")
    tran0.writeAction("slorii X17 X17 12 1426")
    tran0.writeAction("slorii X17 X17 12 406")
    tran0.writeAction("slorii X17 X17 12 2724")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 38917")
    tran0.writeAction("slorii X17 X17 12 2496")
    tran0.writeAction("slorii X17 X17 12 3338")
    tran0.writeAction("slorii X17 X17 12 3840")
    tran0.writeAction("slorii X17 X17 12 3067")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 33332")
    tran0.writeAction("slorii X17 X17 12 1288")
    tran0.writeAction("slorii X17 X17 12 3584")
    tran0.writeAction("slorii X17 X17 12 1649")
    tran0.writeAction("slorii X17 X17 12 1218")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
