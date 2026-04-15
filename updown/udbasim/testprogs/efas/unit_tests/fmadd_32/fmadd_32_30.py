from EFA_v2 import *
def fmadd_32_30():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [800098180, 1025818660, 1604468003]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 47")
    tran0.writeAction("slorii X16 X16 12 2824")
    tran0.writeAction("slorii X16 X16 12 1924")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 61")
    tran0.writeAction("slorii X17 X17 12 588")
    tran0.writeAction("slorii X17 X17 12 36")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 95")
    tran0.writeAction("slorii X18 X18 12 2595")
    tran0.writeAction("slorii X18 X18 12 3363")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
