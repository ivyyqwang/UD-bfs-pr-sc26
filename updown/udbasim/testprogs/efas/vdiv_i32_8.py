from EFA_v2 import *
def vdiv_i32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2119272157, 301419322, -640405526, -1920260794, 392023705, -885768778, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 287")
    tran0.writeAction("slorii X19 X19 12 1867")
    tran0.writeAction("slorii X19 X19 8 58")
    tran0.writeAction("slorii X19 X19 12 2074")
    tran0.writeAction("slorii X19 X19 12 3705")
    tran0.writeAction("slorii X19 X19 8 35")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2264")
    tran0.writeAction("slorii X17 X17 12 2853")
    tran0.writeAction("slorii X17 X17 8 70")
    tran0.writeAction("slorii X17 X17 12 3485")
    tran0.writeAction("slorii X17 X17 12 1071")
    tran0.writeAction("slorii X17 X17 8 234")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3251")
    tran0.writeAction("slorii X18 X18 12 1085")
    tran0.writeAction("slorii X18 X18 8 182")
    tran0.writeAction("slorii X18 X18 12 373")
    tran0.writeAction("slorii X18 X18 12 3534")
    tran0.writeAction("slorii X18 X18 8 153")
    tran0.writeAction("vdiv.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
