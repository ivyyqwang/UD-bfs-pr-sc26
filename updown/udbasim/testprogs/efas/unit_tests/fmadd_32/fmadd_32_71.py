from EFA_v2 import *
def fmadd_32_71():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2769857556, 4217785765, 3059561580]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 165")
    tran0.writeAction("slorii X16 X16 12 394")
    tran0.writeAction("slorii X16 X16 12 3092")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 251")
    tran0.writeAction("slorii X17 X17 12 1636")
    tran0.writeAction("slorii X17 X17 12 3493")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 182")
    tran0.writeAction("slorii X18 X18 12 1491")
    tran0.writeAction("slorii X18 X18 12 1132")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
