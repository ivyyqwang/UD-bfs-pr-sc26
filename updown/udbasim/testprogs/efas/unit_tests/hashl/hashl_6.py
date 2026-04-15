from EFA_v2 import *
def hashl_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5704643697098993471, -4082785280118472119, -749898106595876698, 4663623923673331424]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 20266")
    tran0.writeAction("slorii X17 X17 12 3955")
    tran0.writeAction("slorii X17 X17 12 1999")
    tran0.writeAction("slorii X17 X17 12 3098")
    tran0.writeAction("slorii X17 X17 12 3903")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 51031")
    tran0.writeAction("slorii X17 X17 12 134")
    tran0.writeAction("slorii X17 X17 12 2900")
    tran0.writeAction("slorii X17 X17 12 1412")
    tran0.writeAction("slorii X17 X17 12 585")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 62871")
    tran0.writeAction("slorii X17 X17 12 3386")
    tran0.writeAction("slorii X17 X17 12 1322")
    tran0.writeAction("slorii X17 X17 12 2518")
    tran0.writeAction("slorii X17 X17 12 166")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 16568")
    tran0.writeAction("slorii X17 X17 12 2131")
    tran0.writeAction("slorii X17 X17 12 4072")
    tran0.writeAction("slorii X17 X17 12 2303")
    tran0.writeAction("slorii X17 X17 12 1760")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
