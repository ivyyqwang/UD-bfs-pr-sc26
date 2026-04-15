from EFA_v2 import *
def movwlr_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
    tran0.writeAction("movir X16 17622")
    tran0.writeAction("slorii X16 X16 12 2061")
    tran0.writeAction("slorii X16 X16 12 644")
    tran0.writeAction("slorii X16 X16 12 2233")
    tran0.writeAction("slorii X16 X16 12 2136")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 249")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 196")
    tran0.writeAction("addi X18 X19 0")
    tran0.writeAction("add X17 X7 X17")
    tran0.writeAction("movwrl X16 X17(X18,0,5)")
    tran0.writeAction("movwlr X17(X18,1,5) X20")
    tran0.writeAction("sub X17 X7 X17")
    tran0.writeAction("yieldt")
    return efa
