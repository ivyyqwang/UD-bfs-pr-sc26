from EFA_v2 import *
def fmadd_64_54():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13649031903802066325, 6111943817697792809, 4414661445267280751]
    tran0.writeAction("movir X16 48491")
    tran0.writeAction("slorii X16 X16 12 419")
    tran0.writeAction("slorii X16 X16 12 874")
    tran0.writeAction("slorii X16 X16 12 392")
    tran0.writeAction("slorii X16 X16 12 1429")
    tran0.writeAction("movir X17 21713")
    tran0.writeAction("slorii X17 X17 12 4040")
    tran0.writeAction("slorii X17 X17 12 1293")
    tran0.writeAction("slorii X17 X17 12 89")
    tran0.writeAction("slorii X17 X17 12 809")
    tran0.writeAction("movir X18 15684")
    tran0.writeAction("slorii X18 X18 12 115")
    tran0.writeAction("slorii X18 X18 12 464")
    tran0.writeAction("slorii X18 X18 12 3149")
    tran0.writeAction("slorii X18 X18 12 879")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
