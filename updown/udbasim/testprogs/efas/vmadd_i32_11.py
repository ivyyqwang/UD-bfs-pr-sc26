from EFA_v2 import *
def vmadd_i32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1425047658, 863482901, -159837666, -1200244339, 1042794903, 380933526, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 823")
    tran0.writeAction("slorii X19 X19 12 1972")
    tran0.writeAction("slorii X19 X19 8 21")
    tran0.writeAction("slorii X19 X19 12 1359")
    tran0.writeAction("slorii X19 X19 12 128")
    tran0.writeAction("slorii X19 X19 8 106")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2951")
    tran0.writeAction("slorii X17 X17 12 1465")
    tran0.writeAction("slorii X17 X17 8 141")
    tran0.writeAction("slorii X17 X17 12 3943")
    tran0.writeAction("slorii X17 X17 12 2322")
    tran0.writeAction("slorii X17 X17 8 30")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 363")
    tran0.writeAction("slorii X18 X18 12 1173")
    tran0.writeAction("slorii X18 X18 8 150")
    tran0.writeAction("slorii X18 X18 12 994")
    tran0.writeAction("slorii X18 X18 12 1993")
    tran0.writeAction("slorii X18 X18 8 151")
    tran0.writeAction("vmadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
