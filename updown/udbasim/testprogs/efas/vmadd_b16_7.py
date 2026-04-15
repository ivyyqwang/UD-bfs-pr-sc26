from EFA_v2 import *
def vmadd_b16_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [47747, 47261, 52054, 48415, 65072, 7512, 54313, 29585, 37217, 44547, 2861, 19214, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3025")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 3253")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 2953")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 2984")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1849")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 3394")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 469")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 4067")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1200")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 178")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 2784")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2326")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("vmadd.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
