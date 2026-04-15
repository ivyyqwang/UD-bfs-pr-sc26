from EFA_v2 import *
def fmadd_64_89():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10001945482074205343, 16544620091704816483, 12458371691604773920]
    tran0.writeAction("movir X16 35534")
    tran0.writeAction("slorii X16 X16 12 198")
    tran0.writeAction("slorii X16 X16 12 3169")
    tran0.writeAction("slorii X16 X16 12 3506")
    tran0.writeAction("slorii X16 X16 12 3231")
    tran0.writeAction("movir X17 58778")
    tran0.writeAction("slorii X17 X17 12 1221")
    tran0.writeAction("slorii X17 X17 12 245")
    tran0.writeAction("slorii X17 X17 12 3507")
    tran0.writeAction("slorii X17 X17 12 867")
    tran0.writeAction("movir X18 44261")
    tran0.writeAction("slorii X18 X18 12 112")
    tran0.writeAction("slorii X18 X18 12 3029")
    tran0.writeAction("slorii X18 X18 12 3624")
    tran0.writeAction("slorii X18 X18 12 3104")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
