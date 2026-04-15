from EFA_v2 import *
def fmadd_32_96():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [488999713, 47828747, 792897688]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 29")
    tran0.writeAction("slorii X16 X16 12 600")
    tran0.writeAction("slorii X16 X16 12 2849")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 2")
    tran0.writeAction("slorii X17 X17 12 3484")
    tran0.writeAction("slorii X17 X17 12 3851")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 47")
    tran0.writeAction("slorii X18 X18 12 1066")
    tran0.writeAction("slorii X18 X18 12 2200")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
