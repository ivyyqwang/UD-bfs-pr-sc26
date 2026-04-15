from EFA_v2 import *
def vgt_b16_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7410, 19110, 1699, 41266, 6304, 13237, 4422, 25606, 40540, 4472, 38010, 27870, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2579")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 106")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 1194")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 463")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1600")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 276")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 827")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 394")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1741")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 2375")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 279")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 2533")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("vgt.b16 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
