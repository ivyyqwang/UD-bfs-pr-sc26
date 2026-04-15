from EFA_v2 import *
def fmadd_32_37():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [865425683, 3248178804, 3517423062]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 51")
    tran0.writeAction("slorii X16 X16 12 2389")
    tran0.writeAction("slorii X16 X16 12 2323")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 193")
    tran0.writeAction("slorii X17 X17 12 2484")
    tran0.writeAction("slorii X17 X17 12 1652")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 209")
    tran0.writeAction("slorii X18 X18 12 2681")
    tran0.writeAction("slorii X18 X18 12 3542")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
