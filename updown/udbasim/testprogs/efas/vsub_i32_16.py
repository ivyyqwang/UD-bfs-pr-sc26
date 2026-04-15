from EFA_v2 import *
def vsub_i32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1960255889, -113014623, -393466249, 1596018423, -2019904788, -1649226634, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3988")
    tran0.writeAction("slorii X19 X19 12 904")
    tran0.writeAction("slorii X19 X19 8 161")
    tran0.writeAction("slorii X19 X19 12 1869")
    tran0.writeAction("slorii X19 X19 12 1825")
    tran0.writeAction("slorii X19 X19 8 145")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1522")
    tran0.writeAction("slorii X17 X17 12 334")
    tran0.writeAction("slorii X17 X17 8 247")
    tran0.writeAction("slorii X17 X17 12 3720")
    tran0.writeAction("slorii X17 X17 12 3118")
    tran0.writeAction("slorii X17 X17 8 119")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2523")
    tran0.writeAction("slorii X18 X18 12 716")
    tran0.writeAction("slorii X18 X18 8 118")
    tran0.writeAction("slorii X18 X18 12 2169")
    tran0.writeAction("slorii X18 X18 12 2738")
    tran0.writeAction("slorii X18 X18 8 236")
    tran0.writeAction("vsub.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
