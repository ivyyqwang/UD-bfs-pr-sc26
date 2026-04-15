from EFA_v2 import *
def vadd_i32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1353490520, 1839810103, -2026471387, -374258623, 2019054763, -1232010007, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1754")
    tran0.writeAction("slorii X19 X19 12 2374")
    tran0.writeAction("slorii X19 X19 8 55")
    tran0.writeAction("slorii X19 X19 12 2805")
    tran0.writeAction("slorii X19 X19 12 863")
    tran0.writeAction("slorii X19 X19 8 168")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3739")
    tran0.writeAction("slorii X17 X17 12 324")
    tran0.writeAction("slorii X17 X17 8 65")
    tran0.writeAction("slorii X17 X17 12 2163")
    tran0.writeAction("slorii X17 X17 12 1664")
    tran0.writeAction("slorii X17 X17 8 37")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2921")
    tran0.writeAction("slorii X18 X18 12 260")
    tran0.writeAction("slorii X18 X18 8 233")
    tran0.writeAction("slorii X18 X18 12 1925")
    tran0.writeAction("slorii X18 X18 12 2132")
    tran0.writeAction("slorii X18 X18 8 171")
    tran0.writeAction("vadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
