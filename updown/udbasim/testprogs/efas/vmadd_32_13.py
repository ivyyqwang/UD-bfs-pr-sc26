from EFA_v2 import *
def vmadd_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2483305677, 123762510, 1575682019, 3636430512, 2430862831, 2253927422, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 118")
    tran0.writeAction("slorii X19 X19 12 119")
    tran0.writeAction("slorii X19 X19 8 78")
    tran0.writeAction("slorii X19 X19 12 2368")
    tran0.writeAction("slorii X19 X19 12 1084")
    tran0.writeAction("slorii X19 X19 8 205")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3467")
    tran0.writeAction("slorii X17 X17 12 3974")
    tran0.writeAction("slorii X17 X17 8 176")
    tran0.writeAction("slorii X17 X17 12 1502")
    tran0.writeAction("slorii X17 X17 12 2815")
    tran0.writeAction("slorii X17 X17 8 227")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2149")
    tran0.writeAction("slorii X18 X18 12 2099")
    tran0.writeAction("slorii X18 X18 8 254")
    tran0.writeAction("slorii X18 X18 12 2318")
    tran0.writeAction("slorii X18 X18 12 1029")
    tran0.writeAction("slorii X18 X18 8 239")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
