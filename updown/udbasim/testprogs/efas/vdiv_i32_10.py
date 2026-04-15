from EFA_v2 import *
def vdiv_i32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-553221398, 2028889601, 1705700111, 501530752, 1094528270, -1811697291, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1934")
    tran0.writeAction("slorii X19 X19 12 3686")
    tran0.writeAction("slorii X19 X19 8 1")
    tran0.writeAction("slorii X19 X19 12 3568")
    tran0.writeAction("slorii X19 X19 12 1666")
    tran0.writeAction("slorii X19 X19 8 234")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 478")
    tran0.writeAction("slorii X17 X17 12 1216")
    tran0.writeAction("slorii X17 X17 8 128")
    tran0.writeAction("slorii X17 X17 12 1626")
    tran0.writeAction("slorii X17 X17 12 2795")
    tran0.writeAction("slorii X17 X17 8 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2368")
    tran0.writeAction("slorii X18 X18 12 945")
    tran0.writeAction("slorii X18 X18 8 117")
    tran0.writeAction("slorii X18 X18 12 1043")
    tran0.writeAction("slorii X18 X18 12 3373")
    tran0.writeAction("slorii X18 X18 8 14")
    tran0.writeAction("vdiv.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
