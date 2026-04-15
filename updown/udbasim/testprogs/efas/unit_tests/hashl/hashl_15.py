from EFA_v2 import *
def hashl_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7582751303360041885, 8409690610824195163]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 38596")
    tran0.writeAction("slorii X17 X17 12 2685")
    tran0.writeAction("slorii X17 X17 12 3423")
    tran0.writeAction("slorii X17 X17 12 386")
    tran0.writeAction("slorii X17 X17 12 3171")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 29877")
    tran0.writeAction("slorii X17 X17 12 912")
    tran0.writeAction("slorii X17 X17 12 3545")
    tran0.writeAction("slorii X17 X17 12 466")
    tran0.writeAction("slorii X17 X17 12 3163")
    tran0.writeAction("hashl X16 X17 1")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
