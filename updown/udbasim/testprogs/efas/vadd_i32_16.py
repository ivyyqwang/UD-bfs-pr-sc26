from EFA_v2 import *
def vadd_i32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-72590744, 1807723819, 33565298, -1231344304, -1369880787, -487258291, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1723")
    tran0.writeAction("slorii X19 X19 12 4013")
    tran0.writeAction("slorii X19 X19 8 43")
    tran0.writeAction("slorii X19 X19 12 4026")
    tran0.writeAction("slorii X19 X19 12 3162")
    tran0.writeAction("slorii X19 X19 8 104")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2921")
    tran0.writeAction("slorii X17 X17 12 2861")
    tran0.writeAction("slorii X17 X17 8 80")
    tran0.writeAction("slorii X17 X17 12 32")
    tran0.writeAction("slorii X17 X17 12 42")
    tran0.writeAction("slorii X17 X17 8 114")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3631")
    tran0.writeAction("slorii X18 X18 12 1287")
    tran0.writeAction("slorii X18 X18 8 77")
    tran0.writeAction("slorii X18 X18 12 2789")
    tran0.writeAction("slorii X18 X18 12 2375")
    tran0.writeAction("slorii X18 X18 8 45")
    tran0.writeAction("vadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
