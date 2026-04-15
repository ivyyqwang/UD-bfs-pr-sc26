from EFA_v2 import *
def hashl_46():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2687504468016357255, -3707105619654964005, 6891045187977924549, 8188117732323787738]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 55988")
    tran0.writeAction("slorii X17 X17 12 270")
    tran0.writeAction("slorii X17 X17 12 3299")
    tran0.writeAction("slorii X17 X17 12 2498")
    tran0.writeAction("slorii X17 X17 12 121")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 52365")
    tran0.writeAction("slorii X17 X17 12 2929")
    tran0.writeAction("slorii X17 X17 12 1147")
    tran0.writeAction("slorii X17 X17 12 2504")
    tran0.writeAction("slorii X17 X17 12 3291")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 24481")
    tran0.writeAction("slorii X17 X17 12 3729")
    tran0.writeAction("slorii X17 X17 12 1680")
    tran0.writeAction("slorii X17 X17 12 2412")
    tran0.writeAction("slorii X17 X17 12 4037")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 29090")
    tran0.writeAction("slorii X17 X17 12 155")
    tran0.writeAction("slorii X17 X17 12 494")
    tran0.writeAction("slorii X17 X17 12 968")
    tran0.writeAction("slorii X17 X17 12 986")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
