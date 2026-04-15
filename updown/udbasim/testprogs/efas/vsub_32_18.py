from EFA_v2 import *
def vsub_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [76991701, 2653328159, 2507132511, 124600417, 2318177493, 844290994, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2530")
    tran0.writeAction("slorii X19 X19 12 1683")
    tran0.writeAction("slorii X19 X19 8 31")
    tran0.writeAction("slorii X19 X19 12 73")
    tran0.writeAction("slorii X19 X19 12 1740")
    tran0.writeAction("slorii X19 X19 8 213")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 118")
    tran0.writeAction("slorii X17 X17 12 3392")
    tran0.writeAction("slorii X17 X17 8 97")
    tran0.writeAction("slorii X17 X17 12 2390")
    tran0.writeAction("slorii X17 X17 12 4046")
    tran0.writeAction("slorii X17 X17 8 95")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 805")
    tran0.writeAction("slorii X18 X18 12 731")
    tran0.writeAction("slorii X18 X18 8 178")
    tran0.writeAction("slorii X18 X18 12 2210")
    tran0.writeAction("slorii X18 X18 12 3220")
    tran0.writeAction("slorii X18 X18 8 213")
    tran0.writeAction("vsub.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
