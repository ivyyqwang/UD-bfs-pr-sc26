from EFA_v2 import *
def fmadd_64_39():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4372995578349305734, 10879466107622739597, 14969828626561318430]
    tran0.writeAction("movir X16 15536")
    tran0.writeAction("slorii X16 X16 12 4")
    tran0.writeAction("slorii X16 X16 12 3891")
    tran0.writeAction("slorii X16 X16 12 3539")
    tran0.writeAction("slorii X16 X16 12 3974")
    tran0.writeAction("movir X17 38651")
    tran0.writeAction("slorii X17 X17 12 2572")
    tran0.writeAction("slorii X17 X17 12 2162")
    tran0.writeAction("slorii X17 X17 12 3092")
    tran0.writeAction("slorii X17 X17 12 3725")
    tran0.writeAction("movir X18 53183")
    tran0.writeAction("slorii X18 X18 12 2109")
    tran0.writeAction("slorii X18 X18 12 642")
    tran0.writeAction("slorii X18 X18 12 2707")
    tran0.writeAction("slorii X18 X18 12 3614")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
