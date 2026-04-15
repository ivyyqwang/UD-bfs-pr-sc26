from EFA_v2 import *
def vgt_i32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1982787732, 2062807338, -1054859658, -1650986485, -258148992, 770517264, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1967")
    tran0.writeAction("slorii X19 X19 12 1009")
    tran0.writeAction("slorii X19 X19 8 42")
    tran0.writeAction("slorii X19 X19 12 1890")
    tran0.writeAction("slorii X19 X19 12 3824")
    tran0.writeAction("slorii X19 X19 8 148")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2521")
    tran0.writeAction("slorii X17 X17 12 2034")
    tran0.writeAction("slorii X17 X17 8 11")
    tran0.writeAction("slorii X17 X17 12 3090")
    tran0.writeAction("slorii X17 X17 12 30")
    tran0.writeAction("slorii X17 X17 8 118")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 734")
    tran0.writeAction("slorii X18 X18 12 3369")
    tran0.writeAction("slorii X18 X18 8 16")
    tran0.writeAction("slorii X18 X18 12 3849")
    tran0.writeAction("slorii X18 X18 12 3317")
    tran0.writeAction("slorii X18 X18 8 128")
    tran0.writeAction("vgt.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
