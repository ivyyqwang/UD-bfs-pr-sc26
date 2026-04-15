from EFA_v2 import *
def fmadd_64_26():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4216291269516172545, 9014987527582886394, 18273614231201252089]
    tran0.writeAction("movir X16 14979")
    tran0.writeAction("slorii X16 X16 12 1129")
    tran0.writeAction("slorii X16 X16 12 541")
    tran0.writeAction("slorii X16 X16 12 377")
    tran0.writeAction("slorii X16 X16 12 3329")
    tran0.writeAction("movir X17 32027")
    tran0.writeAction("slorii X17 X17 12 2742")
    tran0.writeAction("slorii X17 X17 12 1172")
    tran0.writeAction("slorii X17 X17 12 634")
    tran0.writeAction("slorii X17 X17 12 2554")
    tran0.writeAction("movir X18 64920")
    tran0.writeAction("slorii X18 X18 12 3765")
    tran0.writeAction("slorii X18 X18 12 853")
    tran0.writeAction("slorii X18 X18 12 1120")
    tran0.writeAction("slorii X18 X18 12 761")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
