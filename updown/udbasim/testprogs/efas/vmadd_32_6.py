from EFA_v2 import *
def vmadd_32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2720896545, 3283637757, 1110570868, 3110835054, 68329732, 3011603539, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3131")
    tran0.writeAction("slorii X19 X19 12 2133")
    tran0.writeAction("slorii X19 X19 8 253")
    tran0.writeAction("slorii X19 X19 12 2594")
    tran0.writeAction("slorii X19 X19 12 3478")
    tran0.writeAction("slorii X19 X19 8 33")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2966")
    tran0.writeAction("slorii X17 X17 12 2963")
    tran0.writeAction("slorii X17 X17 8 110")
    tran0.writeAction("slorii X17 X17 12 1059")
    tran0.writeAction("slorii X17 X17 12 503")
    tran0.writeAction("slorii X17 X17 8 116")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2872")
    tran0.writeAction("slorii X18 X18 12 364")
    tran0.writeAction("slorii X18 X18 8 83")
    tran0.writeAction("slorii X18 X18 12 65")
    tran0.writeAction("slorii X18 X18 12 673")
    tran0.writeAction("slorii X18 X18 8 4")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
