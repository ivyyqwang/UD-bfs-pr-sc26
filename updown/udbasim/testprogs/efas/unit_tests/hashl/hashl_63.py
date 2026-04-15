from EFA_v2 import *
def hashl_63():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-186936391483233797, 2858657638405888060]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 64871")
    tran0.writeAction("slorii X17 X17 12 3557")
    tran0.writeAction("slorii X17 X17 12 1958")
    tran0.writeAction("slorii X17 X17 12 198")
    tran0.writeAction("slorii X17 X17 12 2555")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 10155")
    tran0.writeAction("slorii X17 X17 12 4063")
    tran0.writeAction("slorii X17 X17 12 2543")
    tran0.writeAction("slorii X17 X17 12 2621")
    tran0.writeAction("slorii X17 X17 12 2108")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
