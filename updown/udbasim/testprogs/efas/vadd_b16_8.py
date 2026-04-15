from EFA_v2 import *
def vadd_b16_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [60336, 20067, 56958, 56750, 4645, 18230, 57255, 10263, 2771, 35031, 14566, 22996, 12]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3546")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3559")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 1254")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 3771")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 641")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 3578")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 1139")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 290")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1437")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 910")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 2189")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 173")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("vadd.b16 X19 X17 X18 12 ")
    tran0.writeAction("yieldt")
    return efa
