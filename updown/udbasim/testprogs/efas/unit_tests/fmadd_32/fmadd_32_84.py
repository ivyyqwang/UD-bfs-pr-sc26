from EFA_v2 import *
def fmadd_32_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3597166363, 1572674966, 2222294922]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 214")
    tran0.writeAction("slorii X16 X16 12 1670")
    tran0.writeAction("slorii X16 X16 12 1819")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 93")
    tran0.writeAction("slorii X17 X17 12 3025")
    tran0.writeAction("slorii X17 X17 12 3478")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 132")
    tran0.writeAction("slorii X18 X18 12 1880")
    tran0.writeAction("slorii X18 X18 12 1930")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
