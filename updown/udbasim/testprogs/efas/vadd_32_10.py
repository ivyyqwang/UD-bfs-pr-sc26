from EFA_v2 import *
def vadd_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3644341948, 4145816115, 2323963233, 1300702949, 3699365098, 688239141, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3953")
    tran0.writeAction("slorii X19 X19 12 3106")
    tran0.writeAction("slorii X19 X19 8 51")
    tran0.writeAction("slorii X19 X19 12 3475")
    tran0.writeAction("slorii X19 X19 12 2110")
    tran0.writeAction("slorii X19 X19 8 188")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1240")
    tran0.writeAction("slorii X17 X17 12 1830")
    tran0.writeAction("slorii X17 X17 8 229")
    tran0.writeAction("slorii X17 X17 12 2216")
    tran0.writeAction("slorii X17 X17 12 1245")
    tran0.writeAction("slorii X17 X17 8 97")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 656")
    tran0.writeAction("slorii X18 X18 12 1458")
    tran0.writeAction("slorii X18 X18 8 37")
    tran0.writeAction("slorii X18 X18 12 3527")
    tran0.writeAction("slorii X18 X18 12 4052")
    tran0.writeAction("slorii X18 X18 8 234")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
