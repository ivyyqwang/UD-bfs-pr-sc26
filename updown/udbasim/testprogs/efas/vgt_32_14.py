from EFA_v2 import *
def vgt_32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2008876635, 2226514806, 1328015313, 1471896175, 4079437225, 3417244567, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2123")
    tran0.writeAction("slorii X19 X19 12 1515")
    tran0.writeAction("slorii X19 X19 8 118")
    tran0.writeAction("slorii X19 X19 12 1915")
    tran0.writeAction("slorii X19 X19 12 3334")
    tran0.writeAction("slorii X19 X19 8 91")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1403")
    tran0.writeAction("slorii X17 X17 12 2906")
    tran0.writeAction("slorii X17 X17 8 111")
    tran0.writeAction("slorii X17 X17 12 1266")
    tran0.writeAction("slorii X17 X17 12 2023")
    tran0.writeAction("slorii X17 X17 8 209")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3258")
    tran0.writeAction("slorii X18 X18 12 3843")
    tran0.writeAction("slorii X18 X18 8 151")
    tran0.writeAction("slorii X18 X18 12 3890")
    tran0.writeAction("slorii X18 X18 12 1861")
    tran0.writeAction("slorii X18 X18 8 169")
    tran0.writeAction("vgt.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
