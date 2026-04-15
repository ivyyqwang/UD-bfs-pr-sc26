from EFA_v2 import *
def hashl_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8237574945262881214, -8093980396005623492]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 29265")
    tran0.writeAction("slorii X17 X17 12 3052")
    tran0.writeAction("slorii X17 X17 12 1191")
    tran0.writeAction("slorii X17 X17 12 212")
    tran0.writeAction("slorii X17 X17 12 2494")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 36780")
    tran0.writeAction("slorii X17 X17 12 1659")
    tran0.writeAction("slorii X17 X17 12 1709")
    tran0.writeAction("slorii X17 X17 12 447")
    tran0.writeAction("slorii X17 X17 12 2364")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
