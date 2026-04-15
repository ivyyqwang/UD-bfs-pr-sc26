from EFA_v2 import *
def vmadd_i32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1668426359, 939055907, 549215846, 1176037576, 1343542591, -1693978085, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 895")
    tran0.writeAction("slorii X19 X19 12 2267")
    tran0.writeAction("slorii X19 X19 8 35")
    tran0.writeAction("slorii X19 X19 12 1591")
    tran0.writeAction("slorii X19 X19 12 554")
    tran0.writeAction("slorii X19 X19 8 119")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1121")
    tran0.writeAction("slorii X17 X17 12 2280")
    tran0.writeAction("slorii X17 X17 8 200")
    tran0.writeAction("slorii X17 X17 12 523")
    tran0.writeAction("slorii X17 X17 12 3166")
    tran0.writeAction("slorii X17 X17 8 102")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2480")
    tran0.writeAction("slorii X18 X18 12 2034")
    tran0.writeAction("slorii X18 X18 8 27")
    tran0.writeAction("slorii X18 X18 12 1281")
    tran0.writeAction("slorii X18 X18 12 1237")
    tran0.writeAction("slorii X18 X18 8 63")
    tran0.writeAction("vmadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
