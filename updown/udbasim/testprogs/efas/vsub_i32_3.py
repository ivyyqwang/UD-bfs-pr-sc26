from EFA_v2 import *
def vsub_i32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-461537480, 1252895133, -1860646853, 814926936, 954758763, 1090752008, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1194")
    tran0.writeAction("slorii X19 X19 12 3497")
    tran0.writeAction("slorii X19 X19 8 157")
    tran0.writeAction("slorii X19 X19 12 3655")
    tran0.writeAction("slorii X19 X19 12 3455")
    tran0.writeAction("slorii X19 X19 8 56")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 777")
    tran0.writeAction("slorii X17 X17 12 716")
    tran0.writeAction("slorii X17 X17 8 88")
    tran0.writeAction("slorii X17 X17 12 2321")
    tran0.writeAction("slorii X17 X17 12 2248")
    tran0.writeAction("slorii X17 X17 8 59")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1040")
    tran0.writeAction("slorii X18 X18 12 910")
    tran0.writeAction("slorii X18 X18 8 8")
    tran0.writeAction("slorii X18 X18 12 910")
    tran0.writeAction("slorii X18 X18 12 2166")
    tran0.writeAction("slorii X18 X18 8 107")
    tran0.writeAction("vsub.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
