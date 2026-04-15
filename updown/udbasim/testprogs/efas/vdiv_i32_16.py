from EFA_v2 import *
def vdiv_i32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-637958362, 1156433923, -1904199371, -1404002602, 1138096861, 1337569020, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1102")
    tran0.writeAction("slorii X19 X19 12 3528")
    tran0.writeAction("slorii X19 X19 8 3")
    tran0.writeAction("slorii X19 X19 12 3487")
    tran0.writeAction("slorii X19 X19 12 2439")
    tran0.writeAction("slorii X19 X19 8 38")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2757")
    tran0.writeAction("slorii X17 X17 12 158")
    tran0.writeAction("slorii X17 X17 8 214")
    tran0.writeAction("slorii X17 X17 12 2280")
    tran0.writeAction("slorii X17 X17 12 57")
    tran0.writeAction("slorii X17 X17 8 53")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1275")
    tran0.writeAction("slorii X18 X18 12 2478")
    tran0.writeAction("slorii X18 X18 8 252")
    tran0.writeAction("slorii X18 X18 12 1085")
    tran0.writeAction("slorii X18 X18 12 1530")
    tran0.writeAction("slorii X18 X18 8 221")
    tran0.writeAction("vdiv.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
