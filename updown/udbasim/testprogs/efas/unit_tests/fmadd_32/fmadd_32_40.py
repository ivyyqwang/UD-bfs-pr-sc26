from EFA_v2 import *
def fmadd_32_40():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [569574197, 64240508, 1716863502]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 33")
    tran0.writeAction("slorii X16 X16 12 3888")
    tran0.writeAction("slorii X16 X16 12 821")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 3")
    tran0.writeAction("slorii X17 X17 12 3395")
    tran0.writeAction("slorii X17 X17 12 2940")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 102")
    tran0.writeAction("slorii X18 X18 12 1364")
    tran0.writeAction("slorii X18 X18 12 526")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
