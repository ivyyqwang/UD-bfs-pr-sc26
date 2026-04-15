from EFA_v2 import *
def fmadd_64_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8020694356119512542, 13015503535982309667, 9584457190360860734]
    tran0.writeAction("movir X16 28495")
    tran0.writeAction("slorii X16 X16 12 944")
    tran0.writeAction("slorii X16 X16 12 1404")
    tran0.writeAction("slorii X16 X16 12 1982")
    tran0.writeAction("slorii X16 X16 12 1502")
    tran0.writeAction("movir X17 46240")
    tran0.writeAction("slorii X17 X17 12 1464")
    tran0.writeAction("slorii X17 X17 12 451")
    tran0.writeAction("slorii X17 X17 12 271")
    tran0.writeAction("slorii X17 X17 12 291")
    tran0.writeAction("movir X18 34050")
    tran0.writeAction("slorii X18 X18 12 3408")
    tran0.writeAction("slorii X18 X18 12 2228")
    tran0.writeAction("slorii X18 X18 12 1628")
    tran0.writeAction("slorii X18 X18 12 2110")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
