from EFA_v2 import *
def vdiv_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1627339297, 2523189445, 4207940240, 4232751419, 1797182057, 619953939, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2406")
    tran0.writeAction("slorii X19 X19 12 1232")
    tran0.writeAction("slorii X19 X19 8 197")
    tran0.writeAction("slorii X19 X19 12 1551")
    tran0.writeAction("slorii X19 X19 12 3898")
    tran0.writeAction("slorii X19 X19 8 33")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 4036")
    tran0.writeAction("slorii X17 X17 12 2729")
    tran0.writeAction("slorii X17 X17 8 59")
    tran0.writeAction("slorii X17 X17 12 4013")
    tran0.writeAction("slorii X17 X17 12 18")
    tran0.writeAction("slorii X17 X17 8 144")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 591")
    tran0.writeAction("slorii X18 X18 12 959")
    tran0.writeAction("slorii X18 X18 8 19")
    tran0.writeAction("slorii X18 X18 12 1713")
    tran0.writeAction("slorii X18 X18 12 3794")
    tran0.writeAction("slorii X18 X18 8 105")
    tran0.writeAction("vdiv.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
