from EFA_v2 import *
def vgt_b16_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [10992, 52834, 8462, 28613, 61371, 61913, 43305, 6100, 6043, 29258, 30434, 6257, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1788")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 528")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3302")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 687")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 381")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("slorii X17 X17 12 2706")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 3869")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 3835")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 391")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 1902")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 1828")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 377")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vgt.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
