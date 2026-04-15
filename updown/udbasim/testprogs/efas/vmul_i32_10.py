from EFA_v2 import *
def vmul_i32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [786722349, -375747444, -192282038, 1515359460, 136273581, 866132484, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3737")
    tran0.writeAction("slorii X19 X19 12 2700")
    tran0.writeAction("slorii X19 X19 8 140")
    tran0.writeAction("slorii X19 X19 12 750")
    tran0.writeAction("slorii X19 X19 12 1134")
    tran0.writeAction("slorii X19 X19 8 45")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1445")
    tran0.writeAction("slorii X17 X17 12 652")
    tran0.writeAction("slorii X17 X17 8 228")
    tran0.writeAction("slorii X17 X17 12 3912")
    tran0.writeAction("slorii X17 X17 12 2562")
    tran0.writeAction("slorii X17 X17 8 74")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 826")
    tran0.writeAction("slorii X18 X18 12 34")
    tran0.writeAction("slorii X18 X18 8 4")
    tran0.writeAction("slorii X18 X18 12 129")
    tran0.writeAction("slorii X18 X18 12 3934")
    tran0.writeAction("slorii X18 X18 8 173")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
