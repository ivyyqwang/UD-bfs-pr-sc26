from EFA_v2 import *
def fmadd_64_42():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1337715060466548900, 9279812598027147486, 15665732423322606735]
    tran0.writeAction("movir X16 4752")
    tran0.writeAction("slorii X16 X16 12 2124")
    tran0.writeAction("slorii X16 X16 12 653")
    tran0.writeAction("slorii X16 X16 12 3272")
    tran0.writeAction("slorii X16 X16 12 164")
    tran0.writeAction("movir X17 32968")
    tran0.writeAction("slorii X17 X17 12 2118")
    tran0.writeAction("slorii X17 X17 12 1071")
    tran0.writeAction("slorii X17 X17 12 2469")
    tran0.writeAction("slorii X17 X17 12 2270")
    tran0.writeAction("movir X18 55655")
    tran0.writeAction("slorii X18 X18 12 3530")
    tran0.writeAction("slorii X18 X18 12 878")
    tran0.writeAction("slorii X18 X18 12 1897")
    tran0.writeAction("slorii X18 X18 12 3215")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
