from EFA_v2 import *
def vmadd_32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2852625973, 3983750352, 3920820433, 3269724867, 2704677041, 667910403, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3799")
    tran0.writeAction("slorii X19 X19 12 820")
    tran0.writeAction("slorii X19 X19 8 208")
    tran0.writeAction("slorii X19 X19 12 2720")
    tran0.writeAction("slorii X19 X19 12 1950")
    tran0.writeAction("slorii X19 X19 8 53")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3118")
    tran0.writeAction("slorii X17 X17 12 1034")
    tran0.writeAction("slorii X17 X17 8 195")
    tran0.writeAction("slorii X17 X17 12 3739")
    tran0.writeAction("slorii X17 X17 12 760")
    tran0.writeAction("slorii X17 X17 8 209")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 636")
    tran0.writeAction("slorii X18 X18 12 3969")
    tran0.writeAction("slorii X18 X18 8 3")
    tran0.writeAction("slorii X18 X18 12 2579")
    tran0.writeAction("slorii X18 X18 12 1560")
    tran0.writeAction("slorii X18 X18 8 177")
    tran0.writeAction("vmadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
