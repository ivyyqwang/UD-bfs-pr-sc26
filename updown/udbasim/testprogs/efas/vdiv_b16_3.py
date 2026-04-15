from EFA_v2 import *
def vdiv_b16_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [22123, 64921, 14958, 4809, 20636, 34011, 57405, 43826, 4887, 37513, 16305, 29902, 14]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 300")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 934")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 4057")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 1382")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2739")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 3587")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 2125")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 1289")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1868")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 1019")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 2344")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 305")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("vdiv.b16 X19 X17 X18 14 ")
    tran0.writeAction("yieldt")
    return efa
