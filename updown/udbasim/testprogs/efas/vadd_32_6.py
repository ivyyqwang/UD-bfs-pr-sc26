from EFA_v2 import *
def vadd_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3673717178, 1872194170, 994915033, 3228089382, 1733257663, 547113670, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1785")
    tran0.writeAction("slorii X19 X19 12 1898")
    tran0.writeAction("slorii X19 X19 8 122")
    tran0.writeAction("slorii X19 X19 12 3503")
    tran0.writeAction("slorii X19 X19 12 2169")
    tran0.writeAction("slorii X19 X19 8 186")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3078")
    tran0.writeAction("slorii X17 X17 12 2236")
    tran0.writeAction("slorii X17 X17 8 38")
    tran0.writeAction("slorii X17 X17 12 948")
    tran0.writeAction("slorii X17 X17 12 3378")
    tran0.writeAction("slorii X17 X17 8 217")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 521")
    tran0.writeAction("slorii X18 X18 12 3146")
    tran0.writeAction("slorii X18 X18 8 198")
    tran0.writeAction("slorii X18 X18 12 1652")
    tran0.writeAction("slorii X18 X18 12 3945")
    tran0.writeAction("slorii X18 X18 8 191")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
