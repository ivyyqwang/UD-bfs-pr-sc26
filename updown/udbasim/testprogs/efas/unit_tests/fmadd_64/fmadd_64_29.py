from EFA_v2 import *
def fmadd_64_29():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3436076587683204401, 17929726389516579887, 16772304147774936947]
    tran0.writeAction("movir X16 12207")
    tran0.writeAction("slorii X16 X16 12 1623")
    tran0.writeAction("slorii X16 X16 12 909")
    tran0.writeAction("slorii X16 X16 12 3660")
    tran0.writeAction("slorii X16 X16 12 3377")
    tran0.writeAction("movir X17 63699")
    tran0.writeAction("slorii X17 X17 12 754")
    tran0.writeAction("slorii X17 X17 12 1999")
    tran0.writeAction("slorii X17 X17 12 339")
    tran0.writeAction("slorii X17 X17 12 1071")
    tran0.writeAction("movir X18 59587")
    tran0.writeAction("slorii X18 X18 12 796")
    tran0.writeAction("slorii X18 X18 12 584")
    tran0.writeAction("slorii X18 X18 12 3833")
    tran0.writeAction("slorii X18 X18 12 1907")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
