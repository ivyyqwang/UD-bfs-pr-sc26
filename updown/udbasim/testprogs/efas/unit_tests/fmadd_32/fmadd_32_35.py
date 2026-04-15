from EFA_v2 import *
def fmadd_32_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3436093055, 3245053995, 83286688]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 204")
    tran0.writeAction("slorii X16 X16 12 3305")
    tran0.writeAction("slorii X16 X16 12 3711")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 193")
    tran0.writeAction("slorii X17 X17 12 1721")
    tran0.writeAction("slorii X17 X17 12 2091")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 4")
    tran0.writeAction("slorii X18 X18 12 3949")
    tran0.writeAction("slorii X18 X18 12 2720")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
