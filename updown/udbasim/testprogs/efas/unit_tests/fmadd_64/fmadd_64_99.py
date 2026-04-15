from EFA_v2 import *
def fmadd_64_99():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [17555852106833219195, 18326794513872222411, 11079019335374125124]
    tran0.writeAction("movir X16 62370")
    tran0.writeAction("slorii X16 X16 12 3751")
    tran0.writeAction("slorii X16 X16 12 2541")
    tran0.writeAction("slorii X16 X16 12 356")
    tran0.writeAction("slorii X16 X16 12 3707")
    tran0.writeAction("movir X17 65109")
    tran0.writeAction("slorii X17 X17 12 3496")
    tran0.writeAction("slorii X17 X17 12 710")
    tran0.writeAction("slorii X17 X17 12 3815")
    tran0.writeAction("slorii X17 X17 12 2251")
    tran0.writeAction("movir X18 39360")
    tran0.writeAction("slorii X18 X18 12 2390")
    tran0.writeAction("slorii X18 X18 12 744")
    tran0.writeAction("slorii X18 X18 12 2699")
    tran0.writeAction("slorii X18 X18 12 2116")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
