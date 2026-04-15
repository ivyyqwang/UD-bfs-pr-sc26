from EFA_v2 import *
def vgt_b16_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [53807, 55451, 26603, 17759, 13284, 11251, 8808, 39470, 16217, 57000, 43382, 51739, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1109")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 1662")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3465")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3362")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2466")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 550")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 703")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 830")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3233")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 2711")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 3562")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 1013")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("vgt.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
