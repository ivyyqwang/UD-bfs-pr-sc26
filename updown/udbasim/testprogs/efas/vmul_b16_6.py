from EFA_v2 import *
def vmul_b16_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [29537, 26852, 5327, 5601, 14870, 62132, 50107, 10093, 26214, 56509, 60713, 25450, 11]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 350")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 332")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 1678")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 1846")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 630")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 3131")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 3883")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 929")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1590")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3794")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 3531")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 1638")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vmul.b16 X19 X17 X18 11 ")
    tran0.writeAction("yieldt")
    return efa
