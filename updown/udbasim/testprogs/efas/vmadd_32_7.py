from EFA_v2 import *
def vmadd_32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1551330532, 3167720188, 1355005521, 13374786, 125611237, 4013907659, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3020")
    tran0.writeAction("slorii X19 X19 12 3986")
    tran0.writeAction("slorii X19 X19 8 252")
    tran0.writeAction("slorii X19 X19 12 1479")
    tran0.writeAction("slorii X19 X19 12 1900")
    tran0.writeAction("slorii X19 X19 8 228")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 12")
    tran0.writeAction("slorii X17 X17 12 3093")
    tran0.writeAction("slorii X17 X17 8 66")
    tran0.writeAction("slorii X17 X17 12 1292")
    tran0.writeAction("slorii X17 X17 12 958")
    tran0.writeAction("slorii X17 X17 8 81")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3827")
    tran0.writeAction("slorii X18 X18 12 3934")
    tran0.writeAction("slorii X18 X18 8 203")
    tran0.writeAction("slorii X18 X18 12 119")
    tran0.writeAction("slorii X18 X18 12 3244")
    tran0.writeAction("slorii X18 X18 8 229")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
