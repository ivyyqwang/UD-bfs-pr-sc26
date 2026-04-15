from EFA_v2 import *
def vgt_i32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1295791515, -198771805, 1831623106, 1900072089, -1479324394, 431973928, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3906")
    tran0.writeAction("slorii X19 X19 12 1787")
    tran0.writeAction("slorii X19 X19 8 163")
    tran0.writeAction("slorii X19 X19 12 1235")
    tran0.writeAction("slorii X19 X19 12 3125")
    tran0.writeAction("slorii X19 X19 8 155")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1812")
    tran0.writeAction("slorii X17 X17 12 204")
    tran0.writeAction("slorii X17 X17 8 153")
    tran0.writeAction("slorii X17 X17 12 1746")
    tran0.writeAction("slorii X17 X17 12 3161")
    tran0.writeAction("slorii X17 X17 8 194")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 411")
    tran0.writeAction("slorii X18 X18 12 3942")
    tran0.writeAction("slorii X18 X18 8 40")
    tran0.writeAction("slorii X18 X18 12 2685")
    tran0.writeAction("slorii X18 X18 12 845")
    tran0.writeAction("slorii X18 X18 8 22")
    tran0.writeAction("vgt.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
