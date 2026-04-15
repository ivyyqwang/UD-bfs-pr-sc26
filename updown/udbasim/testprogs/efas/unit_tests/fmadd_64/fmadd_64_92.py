from EFA_v2 import *
def fmadd_64_92():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [16120429902833039787, 2560159814749866368, 647377401055901645]
    tran0.writeAction("movir X16 57271")
    tran0.writeAction("slorii X16 X16 12 1113")
    tran0.writeAction("slorii X16 X16 12 1600")
    tran0.writeAction("slorii X16 X16 12 3883")
    tran0.writeAction("slorii X16 X16 12 2475")
    tran0.writeAction("movir X17 9095")
    tran0.writeAction("slorii X17 X17 12 2108")
    tran0.writeAction("slorii X17 X17 12 2438")
    tran0.writeAction("slorii X17 X17 12 1620")
    tran0.writeAction("slorii X17 X17 12 2432")
    tran0.writeAction("movir X18 2299")
    tran0.writeAction("slorii X18 X18 12 3877")
    tran0.writeAction("slorii X18 X18 12 249")
    tran0.writeAction("slorii X18 X18 12 2263")
    tran0.writeAction("slorii X18 X18 12 1997")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
