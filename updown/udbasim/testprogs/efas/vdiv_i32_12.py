from EFA_v2 import *
def vdiv_i32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1463111839, 1992302090, 1998080108, 2054406862, 231142006, -1771474886, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1900")
    tran0.writeAction("slorii X19 X19 12 30")
    tran0.writeAction("slorii X19 X19 8 10")
    tran0.writeAction("slorii X19 X19 12 1395")
    tran0.writeAction("slorii X19 X19 12 1360")
    tran0.writeAction("slorii X19 X19 8 159")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1959")
    tran0.writeAction("slorii X17 X17 12 962")
    tran0.writeAction("slorii X17 X17 8 206")
    tran0.writeAction("slorii X17 X17 12 1905")
    tran0.writeAction("slorii X17 X17 12 2120")
    tran0.writeAction("slorii X17 X17 8 108")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2406")
    tran0.writeAction("slorii X18 X18 12 2416")
    tran0.writeAction("slorii X18 X18 8 58")
    tran0.writeAction("slorii X18 X18 12 220")
    tran0.writeAction("slorii X18 X18 12 1778")
    tran0.writeAction("slorii X18 X18 8 118")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
