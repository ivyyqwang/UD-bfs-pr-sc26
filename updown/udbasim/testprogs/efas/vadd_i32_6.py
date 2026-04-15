from EFA_v2 import *
def vadd_i32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2083637430, -201342864, 112111634, -1922795841, 934492524, 277833879, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3903")
    tran0.writeAction("slorii X19 X19 12 4032")
    tran0.writeAction("slorii X19 X19 8 112")
    tran0.writeAction("slorii X19 X19 12 2108")
    tran0.writeAction("slorii X19 X19 12 3639")
    tran0.writeAction("slorii X19 X19 8 74")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2262")
    tran0.writeAction("slorii X17 X17 12 1142")
    tran0.writeAction("slorii X17 X17 8 191")
    tran0.writeAction("slorii X17 X17 12 106")
    tran0.writeAction("slorii X17 X17 12 3760")
    tran0.writeAction("slorii X17 X17 8 18")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 264")
    tran0.writeAction("slorii X18 X18 12 3944")
    tran0.writeAction("slorii X18 X18 8 151")
    tran0.writeAction("slorii X18 X18 12 891")
    tran0.writeAction("slorii X18 X18 12 825")
    tran0.writeAction("slorii X18 X18 8 108")
    tran0.writeAction("vadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
