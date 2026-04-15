from EFA_v2 import *
def vmadd_i32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1550215692, 1020522794, -1000769241, 384070253, 153303153, -303862889, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 973")
    tran0.writeAction("slorii X19 X19 12 1009")
    tran0.writeAction("slorii X19 X19 8 42")
    tran0.writeAction("slorii X19 X19 12 2617")
    tran0.writeAction("slorii X19 X19 12 2453")
    tran0.writeAction("slorii X19 X19 8 244")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 366")
    tran0.writeAction("slorii X17 X17 12 1138")
    tran0.writeAction("slorii X17 X17 8 109")
    tran0.writeAction("slorii X17 X17 12 3141")
    tran0.writeAction("slorii X17 X17 12 2425")
    tran0.writeAction("slorii X17 X17 8 39")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3806")
    tran0.writeAction("slorii X18 X18 12 875")
    tran0.writeAction("slorii X18 X18 8 151")
    tran0.writeAction("slorii X18 X18 12 146")
    tran0.writeAction("slorii X18 X18 12 824")
    tran0.writeAction("slorii X18 X18 8 113")
    tran0.writeAction("vmadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
