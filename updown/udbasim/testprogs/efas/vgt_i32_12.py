from EFA_v2 import *
def vgt_i32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [214020617, -267530424, 2029428032, 1253981581, -1933078172, -1479526231, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3840")
    tran0.writeAction("slorii X19 X19 12 3535")
    tran0.writeAction("slorii X19 X19 8 72")
    tran0.writeAction("slorii X19 X19 12 204")
    tran0.writeAction("slorii X19 X19 12 434")
    tran0.writeAction("slorii X19 X19 8 9")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1195")
    tran0.writeAction("slorii X17 X17 12 3645")
    tran0.writeAction("slorii X17 X17 8 141")
    tran0.writeAction("slorii X17 X17 12 1935")
    tran0.writeAction("slorii X17 X17 12 1693")
    tran0.writeAction("slorii X17 X17 8 64")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2685")
    tran0.writeAction("slorii X18 X18 12 56")
    tran0.writeAction("slorii X18 X18 8 169")
    tran0.writeAction("slorii X18 X18 12 2252")
    tran0.writeAction("slorii X18 X18 12 1937")
    tran0.writeAction("slorii X18 X18 8 100")
    tran0.writeAction("vgt.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
