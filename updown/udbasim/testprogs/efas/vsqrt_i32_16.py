from EFA_v2 import *
def vsqrt_i32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-362777096, -1069403643, 624855495, 765455827, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3076")
    tran0.writeAction("slorii X19 X19 12 562")
    tran0.writeAction("slorii X19 X19 8 5")
    tran0.writeAction("slorii X19 X19 12 3750")
    tran0.writeAction("slorii X19 X19 12 117")
    tran0.writeAction("slorii X19 X19 8 248")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 729")
    tran0.writeAction("slorii X18 X18 12 4077")
    tran0.writeAction("slorii X18 X18 8 211")
    tran0.writeAction("slorii X18 X18 12 595")
    tran0.writeAction("slorii X18 X18 12 3721")
    tran0.writeAction("slorii X18 X18 8 199")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
