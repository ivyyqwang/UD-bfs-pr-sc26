from EFA_v2 import *
def hashl_43():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-8079976460649934508, 8038242502596871964, -6849442770270512443]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 36830")
    tran0.writeAction("slorii X17 X17 12 643")
    tran0.writeAction("slorii X17 X17 12 2037")
    tran0.writeAction("slorii X17 X17 12 1813")
    tran0.writeAction("slorii X17 X17 12 340")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 28557")
    tran0.writeAction("slorii X17 X17 12 2351")
    tran0.writeAction("slorii X17 X17 12 1977")
    tran0.writeAction("slorii X17 X17 12 3004")
    tran0.writeAction("slorii X17 X17 12 1820")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 41201")
    tran0.writeAction("slorii X17 X17 12 3649")
    tran0.writeAction("slorii X17 X17 12 1824")
    tran0.writeAction("slorii X17 X17 12 2697")
    tran0.writeAction("slorii X17 X17 12 2757")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
