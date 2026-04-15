from EFA_v2 import *
def fmadd_64_48():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [12689925982010631237, 17259975170965519212, 9977149497575259563]
    tran0.writeAction("movir X16 45083")
    tran0.writeAction("slorii X16 X16 12 2759")
    tran0.writeAction("slorii X16 X16 12 591")
    tran0.writeAction("slorii X16 X16 12 3046")
    tran0.writeAction("slorii X16 X16 12 1093")
    tran0.writeAction("movir X17 61319")
    tran0.writeAction("slorii X17 X17 12 3071")
    tran0.writeAction("slorii X17 X17 12 2177")
    tran0.writeAction("slorii X17 X17 12 1891")
    tran0.writeAction("slorii X17 X17 12 2924")
    tran0.writeAction("movir X18 35445")
    tran0.writeAction("slorii X18 X18 12 3913")
    tran0.writeAction("slorii X18 X18 12 2905")
    tran0.writeAction("slorii X18 X18 12 3851")
    tran0.writeAction("slorii X18 X18 12 3499")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
