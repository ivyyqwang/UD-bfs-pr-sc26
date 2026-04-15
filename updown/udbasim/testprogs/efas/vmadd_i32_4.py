from EFA_v2 import *
def vmadd_i32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2117965706, 543248404, -1495366623, 1564779903, 1066695117, -1716437678, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 518")
    tran0.writeAction("slorii X19 X19 12 336")
    tran0.writeAction("slorii X19 X19 8 20")
    tran0.writeAction("slorii X19 X19 12 2076")
    tran0.writeAction("slorii X19 X19 12 616")
    tran0.writeAction("slorii X19 X19 8 118")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1492")
    tran0.writeAction("slorii X17 X17 12 1189")
    tran0.writeAction("slorii X17 X17 8 127")
    tran0.writeAction("slorii X17 X17 12 2669")
    tran0.writeAction("slorii X17 X17 12 3716")
    tran0.writeAction("slorii X17 X17 8 33")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2459")
    tran0.writeAction("slorii X18 X18 12 317")
    tran0.writeAction("slorii X18 X18 8 82")
    tran0.writeAction("slorii X18 X18 12 1017")
    tran0.writeAction("slorii X18 X18 12 1145")
    tran0.writeAction("slorii X18 X18 8 205")
    tran0.writeAction("vmadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
