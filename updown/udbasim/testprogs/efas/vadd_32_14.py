from EFA_v2 import *
def vadd_32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3562452122, 291734140, 1961724871, 664684388, 924631354, 544898515, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 278")
    tran0.writeAction("slorii X19 X19 12 898")
    tran0.writeAction("slorii X19 X19 8 124")
    tran0.writeAction("slorii X19 X19 12 3397")
    tran0.writeAction("slorii X19 X19 12 1716")
    tran0.writeAction("slorii X19 X19 8 154")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 633")
    tran0.writeAction("slorii X17 X17 12 3655")
    tran0.writeAction("slorii X17 X17 8 100")
    tran0.writeAction("slorii X17 X17 12 1870")
    tran0.writeAction("slorii X17 X17 12 3467")
    tran0.writeAction("slorii X17 X17 8 199")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 519")
    tran0.writeAction("slorii X18 X18 12 2685")
    tran0.writeAction("slorii X18 X18 8 211")
    tran0.writeAction("slorii X18 X18 12 881")
    tran0.writeAction("slorii X18 X18 12 3265")
    tran0.writeAction("slorii X18 X18 8 58")
    tran0.writeAction("vadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
