from EFA_v2 import *
def vsub_i32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [987451111, 663972141, 1742863180, -1117268093, -901615396, -1515373045, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 633")
    tran0.writeAction("slorii X19 X19 12 873")
    tran0.writeAction("slorii X19 X19 8 45")
    tran0.writeAction("slorii X19 X19 12 941")
    tran0.writeAction("slorii X19 X19 12 2894")
    tran0.writeAction("slorii X19 X19 8 231")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3030")
    tran0.writeAction("slorii X17 X17 12 2007")
    tran0.writeAction("slorii X17 X17 8 131")
    tran0.writeAction("slorii X17 X17 12 1662")
    tran0.writeAction("slorii X17 X17 12 507")
    tran0.writeAction("slorii X17 X17 8 76")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2650")
    tran0.writeAction("slorii X18 X18 12 3390")
    tran0.writeAction("slorii X18 X18 8 11")
    tran0.writeAction("slorii X18 X18 12 3236")
    tran0.writeAction("slorii X18 X18 12 624")
    tran0.writeAction("slorii X18 X18 8 220")
    tran0.writeAction("vsub.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
