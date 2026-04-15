from EFA_v2 import *
def vmadd_i32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-66223945, 414279879, 627189419, 311795974, 622186218, -1210528229, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 395")
    tran0.writeAction("slorii X19 X19 12 360")
    tran0.writeAction("slorii X19 X19 8 199")
    tran0.writeAction("slorii X19 X19 12 4032")
    tran0.writeAction("slorii X19 X19 12 3456")
    tran0.writeAction("slorii X19 X19 8 183")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 297")
    tran0.writeAction("slorii X17 X17 12 1441")
    tran0.writeAction("slorii X17 X17 8 6")
    tran0.writeAction("slorii X17 X17 12 598")
    tran0.writeAction("slorii X17 X17 12 550")
    tran0.writeAction("slorii X17 X17 8 171")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2941")
    tran0.writeAction("slorii X18 X18 12 2254")
    tran0.writeAction("slorii X18 X18 8 27")
    tran0.writeAction("slorii X18 X18 12 593")
    tran0.writeAction("slorii X18 X18 12 1486")
    tran0.writeAction("slorii X18 X18 8 234")
    tran0.writeAction("vmadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
