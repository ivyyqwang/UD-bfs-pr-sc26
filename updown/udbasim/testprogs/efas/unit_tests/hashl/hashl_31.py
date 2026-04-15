from EFA_v2 import *
def hashl_31():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2786888190348250956, -5521531870950984529, -6550438949688064181]
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 9901")
    tran0.writeAction("slorii X17 X17 12 64")
    tran0.writeAction("slorii X17 X17 12 2854")
    tran0.writeAction("slorii X17 X17 12 1796")
    tran0.writeAction("slorii X17 X17 12 3916")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("movir X17 45919")
    tran0.writeAction("slorii X17 X17 12 2368")
    tran0.writeAction("slorii X17 X17 12 1159")
    tran0.writeAction("slorii X17 X17 12 3967")
    tran0.writeAction("slorii X17 X17 12 1199")
    tran0.writeAction("movrl X17 0(X16) 1 8")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movir X17 42264")
    tran0.writeAction("slorii X17 X17 12 679")
    tran0.writeAction("slorii X17 X17 12 2848")
    tran0.writeAction("slorii X17 X17 12 3932")
    tran0.writeAction("slorii X17 X17 12 1867")
    tran0.writeAction("hashl X16 X17 2")
    tran0.writeAction("addi X7 X16 0")
    tran0.writeAction("movrl X17 0(X16) 0 8")
    tran0.writeAction("yieldt")
    return efa
