from EFA_v2 import *
def fmadd_32_36():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4039298932, 3414975365, 211838614]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 240")
    tran0.writeAction("slorii X16 X16 12 3116")
    tran0.writeAction("slorii X16 X16 12 3956")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 203")
    tran0.writeAction("slorii X17 X17 12 2246")
    tran0.writeAction("slorii X17 X17 12 901")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 12")
    tran0.writeAction("slorii X18 X18 12 2566")
    tran0.writeAction("slorii X18 X18 12 1686")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
