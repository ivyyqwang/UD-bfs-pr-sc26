from EFA_v2 import *
def hashl_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2822448454969329383, 395009865153271087, 5843924848215454722]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 55508")
    tran0.writeAction("slorii X17 X17 12 2657")
    tran0.writeAction("slorii X17 X17 12 1420")
    tran0.writeAction("slorii X17 X17 12 2879")
    tran0.writeAction("slorii X17 X17 12 2329")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 1403")
    tran0.writeAction("slorii X17 X17 12 1462")
    tran0.writeAction("slorii X17 X17 12 295")
    tran0.writeAction("slorii X17 X17 12 965")
    tran0.writeAction("slorii X17 X17 12 1327")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 20761")
    tran0.writeAction("slorii X17 X17 12 3242")
    tran0.writeAction("slorii X17 X17 12 4063")
    tran0.writeAction("slorii X17 X17 12 3935")
    tran0.writeAction("slorii X17 X17 12 1026")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
