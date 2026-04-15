from EFA_v2 import *
def hashl_75():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [228632872950660246, 1587431472860031114, 1320124066741742661, -3391346856191012999]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 812")
    tran0.writeAction("slorii X17 X17 12 1094")
    tran0.writeAction("slorii X17 X17 12 760")
    tran0.writeAction("slorii X17 X17 12 823")
    tran0.writeAction("slorii X17 X17 12 3222")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 5639")
    tran0.writeAction("slorii X17 X17 12 2824")
    tran0.writeAction("slorii X17 X17 12 917")
    tran0.writeAction("slorii X17 X17 12 398")
    tran0.writeAction("slorii X17 X17 12 2186")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 4690")
    tran0.writeAction("slorii X17 X17 12 93")
    tran0.writeAction("slorii X17 X17 12 2089")
    tran0.writeAction("slorii X17 X17 12 2398")
    tran0.writeAction("slorii X17 X17 12 3141")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 53487")
    tran0.writeAction("slorii X17 X17 12 2112")
    tran0.writeAction("slorii X17 X17 12 158")
    tran0.writeAction("slorii X17 X17 12 2444")
    tran0.writeAction("slorii X17 X17 12 3961")
    tran0.writeAction("hashl X16 X17 3")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
