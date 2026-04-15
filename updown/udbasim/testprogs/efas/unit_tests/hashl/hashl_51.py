from EFA_v2 import *
def hashl_51():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4217159093361180982, -6973251966290250858, 1599669107041454512]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 14982")
    tran0.writeAction("slorii X17 X17 12 1469")
    tran0.writeAction("slorii X17 X17 12 2585")
    tran0.writeAction("slorii X17 X17 12 416")
    tran0.writeAction("slorii X17 X17 12 310")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 40762")
    tran0.writeAction("slorii X17 X17 12 132")
    tran0.writeAction("slorii X17 X17 12 2131")
    tran0.writeAction("slorii X17 X17 12 3995")
    tran0.writeAction("slorii X17 X17 12 918")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 5683")
    tran0.writeAction("slorii X17 X17 12 681")
    tran0.writeAction("slorii X17 X17 12 979")
    tran0.writeAction("slorii X17 X17 12 1524")
    tran0.writeAction("slorii X17 X17 12 2480")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
