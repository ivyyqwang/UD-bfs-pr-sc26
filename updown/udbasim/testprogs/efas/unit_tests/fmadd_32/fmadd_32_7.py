from EFA_v2 import *
def fmadd_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3588792046, 3480974851, 4109277934]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 213")
    tran0.writeAction("slorii X16 X16 12 3721")
    tran0.writeAction("slorii X16 X16 12 3822")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 207")
    tran0.writeAction("slorii X17 X17 12 1975")
    tran0.writeAction("slorii X17 X17 12 1539")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 0")
    tran0.writeAction("slorii X18 X18 12 244")
    tran0.writeAction("slorii X18 X18 12 3817")
    tran0.writeAction("slorii X18 X18 12 2798")
    tran0.writeAction("fmadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
