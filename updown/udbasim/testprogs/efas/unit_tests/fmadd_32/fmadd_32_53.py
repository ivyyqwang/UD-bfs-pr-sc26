from EFA_v2 import *
def fmadd_32_53():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [561680094, 167394843, 1850079635]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 33")
    tran0.writeAction("slorii X16 X16 12 1960")
    tran0.writeAction("slorii X16 X16 12 3806")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 9")
    tran0.writeAction("slorii X17 X17 12 4003")
    tran0.writeAction("slorii X17 X17 12 3611")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 110")
    tran0.writeAction("slorii X18 X18 12 1119")
    tran0.writeAction("slorii X18 X18 12 2451")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
