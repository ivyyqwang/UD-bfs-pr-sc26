from EFA_v2 import *
def vmul_i32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-261414361, 2136525846, -2131248612, -2095128484, 499749405, 2017770830, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2037")
    tran0.writeAction("slorii X19 X19 12 2252")
    tran0.writeAction("slorii X19 X19 8 22")
    tran0.writeAction("slorii X19 X19 12 3846")
    tran0.writeAction("slorii X19 X19 12 2850")
    tran0.writeAction("slorii X19 X19 8 39")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2097")
    tran0.writeAction("slorii X17 X17 12 3808")
    tran0.writeAction("slorii X17 X17 8 92")
    tran0.writeAction("slorii X17 X17 12 2063")
    tran0.writeAction("slorii X17 X17 12 1978")
    tran0.writeAction("slorii X17 X17 8 28")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1924")
    tran0.writeAction("slorii X18 X18 12 1213")
    tran0.writeAction("slorii X18 X18 8 78")
    tran0.writeAction("slorii X18 X18 12 476")
    tran0.writeAction("slorii X18 X18 12 2450")
    tran0.writeAction("slorii X18 X18 8 29")
    tran0.writeAction("vmul.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
