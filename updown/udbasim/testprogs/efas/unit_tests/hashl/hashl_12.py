from EFA_v2 import *
def hashl_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [5464974569179768372, 4443159691346541684, -857651713134737153, 8768969233352596246]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 19415")
    tran0.writeAction("slorii X17 X17 12 2006")
    tran0.writeAction("slorii X17 X17 12 2686")
    tran0.writeAction("slorii X17 X17 12 2062")
    tran0.writeAction("slorii X17 X17 12 1588")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 15785")
    tran0.writeAction("slorii X17 X17 12 1123")
    tran0.writeAction("slorii X17 X17 12 715")
    tran0.writeAction("slorii X17 X17 12 183")
    tran0.writeAction("slorii X17 X17 12 3188")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 62489")
    tran0.writeAction("slorii X17 X17 12 36")
    tran0.writeAction("slorii X17 X17 12 3993")
    tran0.writeAction("slorii X17 X17 12 2452")
    tran0.writeAction("slorii X17 X17 12 2303")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 31153")
    tran0.writeAction("slorii X17 X17 12 2608")
    tran0.writeAction("slorii X17 X17 12 3784")
    tran0.writeAction("slorii X17 X17 12 1273")
    tran0.writeAction("slorii X17 X17 12 2838")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
