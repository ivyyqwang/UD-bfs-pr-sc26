from EFA_v2 import *
def fmadd_64_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8538429555945599191, 11034208679968159700, 11812409103019775858]
    tran0.writeAction("movir X16 30334")
    tran0.writeAction("slorii X16 X16 12 2439")
    tran0.writeAction("slorii X16 X16 12 333")
    tran0.writeAction("slorii X16 X16 12 3415")
    tran0.writeAction("slorii X16 X16 12 215")
    tran0.writeAction("movir X17 39201")
    tran0.writeAction("slorii X17 X17 12 1573")
    tran0.writeAction("slorii X17 X17 12 1323")
    tran0.writeAction("slorii X17 X17 12 139")
    tran0.writeAction("slorii X17 X17 12 2004")
    tran0.writeAction("movir X18 41966")
    tran0.writeAction("slorii X18 X18 12 439")
    tran0.writeAction("slorii X18 X18 12 3727")
    tran0.writeAction("slorii X18 X18 12 345")
    tran0.writeAction("slorii X18 X18 12 1906")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
