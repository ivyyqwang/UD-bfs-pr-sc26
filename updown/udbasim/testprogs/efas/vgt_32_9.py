from EFA_v2 import *
def vgt_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2661891660, 3746629513, 1494926946, 2228620336, 3185993351, 3406172816, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3573")
    tran0.writeAction("slorii X19 X19 12 263")
    tran0.writeAction("slorii X19 X19 8 137")
    tran0.writeAction("slorii X19 X19 12 2538")
    tran0.writeAction("slorii X19 X19 12 2366")
    tran0.writeAction("slorii X19 X19 8 76")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2125")
    tran0.writeAction("slorii X17 X17 12 1548")
    tran0.writeAction("slorii X17 X17 8 48")
    tran0.writeAction("slorii X17 X17 12 1425")
    tran0.writeAction("slorii X17 X17 12 2758")
    tran0.writeAction("slorii X17 X17 8 98")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3248")
    tran0.writeAction("slorii X18 X18 12 1554")
    tran0.writeAction("slorii X18 X18 8 144")
    tran0.writeAction("slorii X18 X18 12 3038")
    tran0.writeAction("slorii X18 X18 12 1638")
    tran0.writeAction("slorii X18 X18 8 135")
    tran0.writeAction("vgt.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
