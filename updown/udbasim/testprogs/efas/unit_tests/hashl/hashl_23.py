from EFA_v2 import *
def hashl_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6866351002544477094, 2226330525215974761, -4673773259925235075]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 24394")
    tran0.writeAction("slorii X17 X17 12 733")
    tran0.writeAction("slorii X17 X17 12 2937")
    tran0.writeAction("slorii X17 X17 12 3321")
    tran0.writeAction("slorii X17 X17 12 934")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 7909")
    tran0.writeAction("slorii X17 X17 12 2109")
    tran0.writeAction("slorii X17 X17 12 300")
    tran0.writeAction("slorii X17 X17 12 438")
    tran0.writeAction("slorii X17 X17 12 1385")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 48931")
    tran0.writeAction("slorii X17 X17 12 1727")
    tran0.writeAction("slorii X17 X17 12 2969")
    tran0.writeAction("slorii X17 X17 12 1789")
    tran0.writeAction("slorii X17 X17 12 2685")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
