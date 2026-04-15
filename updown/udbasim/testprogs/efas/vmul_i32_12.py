from EFA_v2 import *
def vmul_i32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1729596340, 1847729917, -505969206, -1642965955, 1962734207, -1658296832, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1762")
    tran0.writeAction("slorii X19 X19 12 542")
    tran0.writeAction("slorii X19 X19 8 253")
    tran0.writeAction("slorii X19 X19 12 2446")
    tran0.writeAction("slorii X19 X19 12 2164")
    tran0.writeAction("slorii X19 X19 8 76")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2529")
    tran0.writeAction("slorii X17 X17 12 596")
    tran0.writeAction("slorii X17 X17 8 61")
    tran0.writeAction("slorii X17 X17 12 3613")
    tran0.writeAction("slorii X17 X17 12 1925")
    tran0.writeAction("slorii X17 X17 8 202")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2514")
    tran0.writeAction("slorii X18 X18 12 2150")
    tran0.writeAction("slorii X18 X18 8 0")
    tran0.writeAction("slorii X18 X18 12 1871")
    tran0.writeAction("slorii X18 X18 12 3314")
    tran0.writeAction("slorii X18 X18 8 127")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
