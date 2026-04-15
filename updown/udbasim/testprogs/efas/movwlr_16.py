from EFA_v2 import *
def movwlr_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 47892")
    tran0.writeAction("slorii X16 X16 12 3742")
    tran0.writeAction("slorii X16 X16 12 3126")
    tran0.writeAction("slorii X16 X16 12 3453")
    tran0.writeAction("slorii X16 X16 12 3803")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 30")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 635")
    tran0.writeAction("addi X18 X19 0")
    tran0.writeAction("add X17 X7 X17")
    tran0.writeAction("movwrl X16 X17(X18,0,3)")
    tran0.writeAction("movwlr X17(X18,1,3) X20")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
