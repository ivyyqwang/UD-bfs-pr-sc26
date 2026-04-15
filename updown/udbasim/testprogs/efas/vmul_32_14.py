from EFA_v2 import *
def vmul_32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3663650210, 3288519020, 1272568853, 1088196348, 1066760868, 320021801, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3136")
    tran0.writeAction("slorii X19 X19 12 721")
    tran0.writeAction("slorii X19 X19 8 108")
    tran0.writeAction("slorii X19 X19 12 3493")
    tran0.writeAction("slorii X19 X19 12 3805")
    tran0.writeAction("slorii X19 X19 8 162")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1037")
    tran0.writeAction("slorii X17 X17 12 3214")
    tran0.writeAction("slorii X17 X17 8 252")
    tran0.writeAction("slorii X17 X17 12 1213")
    tran0.writeAction("slorii X17 X17 12 2524")
    tran0.writeAction("slorii X17 X17 8 21")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 305")
    tran0.writeAction("slorii X18 X18 12 805")
    tran0.writeAction("slorii X18 X18 8 41")
    tran0.writeAction("slorii X18 X18 12 1017")
    tran0.writeAction("slorii X18 X18 12 1402")
    tran0.writeAction("slorii X18 X18 8 164")
    tran0.writeAction("vmul.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
