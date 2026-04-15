from EFA_v2 import *
def vdiv_32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1222370604, 723431220, 2441266005, 3677261768, 3169517417, 3246196677, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 689")
    tran0.writeAction("slorii X19 X19 12 3759")
    tran0.writeAction("slorii X19 X19 8 52")
    tran0.writeAction("slorii X19 X19 12 1165")
    tran0.writeAction("slorii X19 X19 12 3045")
    tran0.writeAction("slorii X19 X19 8 44")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3506")
    tran0.writeAction("slorii X17 X17 12 3727")
    tran0.writeAction("slorii X17 X17 8 200")
    tran0.writeAction("slorii X17 X17 12 2328")
    tran0.writeAction("slorii X17 X17 12 707")
    tran0.writeAction("slorii X17 X17 8 85")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3095")
    tran0.writeAction("slorii X18 X18 12 3335")
    tran0.writeAction("slorii X18 X18 8 197")
    tran0.writeAction("slorii X18 X18 12 3022")
    tran0.writeAction("slorii X18 X18 12 2815")
    tran0.writeAction("slorii X18 X18 8 105")
    tran0.writeAction("vdiv.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
