from EFA_v2 import *
def fmadd_64_72():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4142929865812550138, 9551477301812660994, 15927210769841271309]
    tran0.writeAction("movir X16 14718")
    tran0.writeAction("slorii X16 X16 12 2636")
    tran0.writeAction("slorii X16 X16 12 837")
    tran0.writeAction("slorii X16 X16 12 466")
    tran0.writeAction("slorii X16 X16 12 506")
    tran0.writeAction("movir X17 33933")
    tran0.writeAction("slorii X17 X17 12 2720")
    tran0.writeAction("slorii X17 X17 12 6")
    tran0.writeAction("slorii X17 X17 12 3072")
    tran0.writeAction("slorii X17 X17 12 2818")
    tran0.writeAction("movir X18 56584")
    tran0.writeAction("slorii X18 X18 12 3356")
    tran0.writeAction("slorii X18 X18 12 3879")
    tran0.writeAction("slorii X18 X18 12 675")
    tran0.writeAction("slorii X18 X18 12 525")
    tran0.writeAction("fmadd.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
