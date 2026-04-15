from EFA_v2 import *
def vgt_i32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [333480956, 45055947, 1169397265, 81344178, -1624262504, 631943734, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 42")
    tran0.writeAction("slorii X19 X19 12 3967")
    tran0.writeAction("slorii X19 X19 8 203")
    tran0.writeAction("slorii X19 X19 12 318")
    tran0.writeAction("slorii X19 X19 12 131")
    tran0.writeAction("slorii X19 X19 8 252")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 77")
    tran0.writeAction("slorii X17 X17 12 2358")
    tran0.writeAction("slorii X17 X17 8 178")
    tran0.writeAction("slorii X17 X17 12 1115")
    tran0.writeAction("slorii X17 X17 12 918")
    tran0.writeAction("slorii X17 X17 8 17")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 602")
    tran0.writeAction("slorii X18 X18 12 2738")
    tran0.writeAction("slorii X18 X18 8 54")
    tran0.writeAction("slorii X18 X18 12 2546")
    tran0.writeAction("slorii X18 X18 12 4024")
    tran0.writeAction("slorii X18 X18 8 152")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
