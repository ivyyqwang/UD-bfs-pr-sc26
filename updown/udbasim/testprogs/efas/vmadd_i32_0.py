from EFA_v2 import *
def vmadd_i32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1191455968, -2059870110, -751109851, -597158378, -1647620021, -706930427, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2131")
    tran0.writeAction("slorii X19 X19 12 2272")
    tran0.writeAction("slorii X19 X19 8 98")
    tran0.writeAction("slorii X19 X19 12 1136")
    tran0.writeAction("slorii X19 X19 12 1068")
    tran0.writeAction("slorii X19 X19 8 224")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3526")
    tran0.writeAction("slorii X17 X17 12 2070")
    tran0.writeAction("slorii X17 X17 8 22")
    tran0.writeAction("slorii X17 X17 12 3379")
    tran0.writeAction("slorii X17 X17 12 2809")
    tran0.writeAction("slorii X17 X17 8 37")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3421")
    tran0.writeAction("slorii X18 X18 12 3353")
    tran0.writeAction("slorii X18 X18 8 5")
    tran0.writeAction("slorii X18 X18 12 2524")
    tran0.writeAction("slorii X18 X18 12 2896")
    tran0.writeAction("slorii X18 X18 8 75")
    tran0.writeAction("vmadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
