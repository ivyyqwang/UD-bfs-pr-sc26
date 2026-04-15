from EFA_v2 import *
def fmadd_32_73():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4226867275, 1826495821, 4249845760]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 251")
    tran0.writeAction("slorii X16 X16 12 3854")
    tran0.writeAction("slorii X16 X16 12 75")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 108")
    tran0.writeAction("slorii X17 X17 12 3553")
    tran0.writeAction("slorii X17 X17 12 3405")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 253")
    tran0.writeAction("slorii X18 X18 12 1272")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
