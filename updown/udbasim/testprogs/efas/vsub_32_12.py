from EFA_v2 import *
def vsub_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1201499945, 750709758, 1556770852, 2986573490, 3571894048, 269824153, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 715")
    tran0.writeAction("slorii X19 X19 12 3819")
    tran0.writeAction("slorii X19 X19 8 254")
    tran0.writeAction("slorii X19 X19 12 1145")
    tran0.writeAction("slorii X19 X19 12 3439")
    tran0.writeAction("slorii X19 X19 8 41")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2848")
    tran0.writeAction("slorii X17 X17 12 894")
    tran0.writeAction("slorii X17 X17 8 178")
    tran0.writeAction("slorii X17 X17 12 1484")
    tran0.writeAction("slorii X17 X17 12 2672")
    tran0.writeAction("slorii X17 X17 8 36")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 257")
    tran0.writeAction("slorii X18 X18 12 1328")
    tran0.writeAction("slorii X18 X18 8 153")
    tran0.writeAction("slorii X18 X18 12 3406")
    tran0.writeAction("slorii X18 X18 12 1735")
    tran0.writeAction("slorii X18 X18 8 32")
    tran0.writeAction("vsub.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
