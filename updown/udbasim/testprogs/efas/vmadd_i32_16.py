from EFA_v2 import *
def vmadd_i32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1065666335, -321833715, 13537402, 155954126, -1737924915, -2120802863, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3789")
    tran0.writeAction("slorii X19 X19 12 309")
    tran0.writeAction("slorii X19 X19 8 13")
    tran0.writeAction("slorii X19 X19 12 3079")
    tran0.writeAction("slorii X19 X19 12 2872")
    tran0.writeAction("slorii X19 X19 8 225")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 148")
    tran0.writeAction("slorii X17 X17 12 2987")
    tran0.writeAction("slorii X17 X17 8 206")
    tran0.writeAction("slorii X17 X17 12 12")
    tran0.writeAction("slorii X17 X17 12 3728")
    tran0.writeAction("slorii X17 X17 8 122")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2073")
    tran0.writeAction("slorii X18 X18 12 1821")
    tran0.writeAction("slorii X18 X18 8 209")
    tran0.writeAction("slorii X18 X18 12 2438")
    tran0.writeAction("slorii X18 X18 12 2398")
    tran0.writeAction("slorii X18 X18 8 205")
    tran0.writeAction("vmadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
