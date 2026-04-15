from EFA_v2 import *
def vgt_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2913749916, 2155633546, 258295118, 383333905, 3723433444, 1128799542, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2055")
    tran0.writeAction("slorii X19 X19 12 3163")
    tran0.writeAction("slorii X19 X19 8 138")
    tran0.writeAction("slorii X19 X19 12 2778")
    tran0.writeAction("slorii X19 X19 12 3147")
    tran0.writeAction("slorii X19 X19 8 156")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 365")
    tran0.writeAction("slorii X17 X17 12 2358")
    tran0.writeAction("slorii X17 X17 8 17")
    tran0.writeAction("slorii X17 X17 12 246")
    tran0.writeAction("slorii X17 X17 12 1349")
    tran0.writeAction("slorii X17 X17 8 78")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1076")
    tran0.writeAction("slorii X18 X18 12 2077")
    tran0.writeAction("slorii X18 X18 8 54")
    tran0.writeAction("slorii X18 X18 12 3550")
    tran0.writeAction("slorii X18 X18 12 3861")
    tran0.writeAction("slorii X18 X18 8 228")
    tran0.writeAction("vgt.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
