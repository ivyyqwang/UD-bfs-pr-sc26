from EFA_v2 import *
def vmadd_b16_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [19045, 62167, 48178, 64495, 44584, 20647, 35368, 49665, 10241, 35000, 53318, 48489, 11]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 4030")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 3011")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 3885")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 1190")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3104")
    tran0.writeAction("slorii X17 X17 4 1")
    tran0.writeAction("slorii X17 X17 12 2210")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 1290")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 2786")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3030")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 3332")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 2187")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 640")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("vmadd.b16 X19 X17 X18 11 ")
    tran0.writeAction("yieldt")
    return efa
