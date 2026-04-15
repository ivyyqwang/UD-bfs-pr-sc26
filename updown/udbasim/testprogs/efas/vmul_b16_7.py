from EFA_v2 import *
def vmul_b16_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [51104, 61832, 33974, 48284, 49245, 2011, 42766, 39471, 18450, 44382, 44875, 47702, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3017")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("slorii X19 X19 12 2123")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 3864")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 3194")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2466")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 2672")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 125")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 3077")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2981")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 2804")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 2773")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 1153")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("vmul.b16 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
