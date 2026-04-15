from EFA_v2 import *
def hashl_38():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6496251031509819314, 4523134431830220082, 3488479169502999694]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 23079")
    tran0.writeAction("slorii X17 X17 12 1310")
    tran0.writeAction("slorii X17 X17 12 1280")
    tran0.writeAction("slorii X17 X17 12 3717")
    tran0.writeAction("slorii X17 X17 12 4018")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 16069")
    tran0.writeAction("slorii X17 X17 12 1644")
    tran0.writeAction("slorii X17 X17 12 3352")
    tran0.writeAction("slorii X17 X17 12 2369")
    tran0.writeAction("slorii X17 X17 12 3378")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 12393")
    tran0.writeAction("slorii X17 X17 12 2325")
    tran0.writeAction("slorii X17 X17 12 616")
    tran0.writeAction("slorii X17 X17 12 2359")
    tran0.writeAction("slorii X17 X17 12 1166")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
