from EFA_v2 import *
def vmadd_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2449713160, 463018133, 3185842605, 3661819808, 799852957, 4155757572, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 441")
    tran0.writeAction("slorii X19 X19 12 2328")
    tran0.writeAction("slorii X19 X19 8 149")
    tran0.writeAction("slorii X19 X19 12 2336")
    tran0.writeAction("slorii X19 X19 12 936")
    tran0.writeAction("slorii X19 X19 8 8")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3492")
    tran0.writeAction("slorii X17 X17 12 751")
    tran0.writeAction("slorii X17 X17 8 160")
    tran0.writeAction("slorii X17 X17 12 3038")
    tran0.writeAction("slorii X17 X17 12 1049")
    tran0.writeAction("slorii X17 X17 8 173")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3963")
    tran0.writeAction("slorii X18 X18 12 980")
    tran0.writeAction("slorii X18 X18 8 4")
    tran0.writeAction("slorii X18 X18 12 762")
    tran0.writeAction("slorii X18 X18 12 3273")
    tran0.writeAction("slorii X18 X18 8 157")
    tran0.writeAction("vmadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
