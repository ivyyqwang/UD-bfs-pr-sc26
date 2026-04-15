from EFA_v2 import *
def fmadd_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3320092842, 1738453503, 2281410243]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 197")
    tran0.writeAction("slorii X16 X16 12 3657")
    tran0.writeAction("slorii X16 X16 12 2218")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 103")
    tran0.writeAction("slorii X17 X17 12 2539")
    tran0.writeAction("slorii X17 X17 12 511")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 135")
    tran0.writeAction("slorii X18 X18 12 4024")
    tran0.writeAction("slorii X18 X18 12 3779")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
