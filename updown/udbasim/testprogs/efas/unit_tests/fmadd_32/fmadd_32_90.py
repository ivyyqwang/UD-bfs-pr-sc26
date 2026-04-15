from EFA_v2 import *
def fmadd_32_90():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3768626075, 2894905403, 904580425]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 224")
    tran0.writeAction("slorii X16 X16 12 2570")
    tran0.writeAction("slorii X16 X16 12 2971")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 172")
    tran0.writeAction("slorii X17 X17 12 2252")
    tran0.writeAction("slorii X17 X17 12 59")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 53")
    tran0.writeAction("slorii X18 X18 12 3756")
    tran0.writeAction("slorii X18 X18 12 3401")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
