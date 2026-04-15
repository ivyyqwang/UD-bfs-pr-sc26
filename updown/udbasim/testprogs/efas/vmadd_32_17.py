from EFA_v2 import *
def vmadd_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1918630538, 452999578, 74166565, 206962533, 2005145930, 2983837761, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 432")
    tran0.writeAction("slorii X19 X19 12 57")
    tran0.writeAction("slorii X19 X19 8 154")
    tran0.writeAction("slorii X19 X19 12 1829")
    tran0.writeAction("slorii X19 X19 12 3066")
    tran0.writeAction("slorii X19 X19 8 138")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 197")
    tran0.writeAction("slorii X17 X17 12 1535")
    tran0.writeAction("slorii X17 X17 8 101")
    tran0.writeAction("slorii X17 X17 12 70")
    tran0.writeAction("slorii X17 X17 12 2993")
    tran0.writeAction("slorii X17 X17 8 37")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2845")
    tran0.writeAction("slorii X18 X18 12 2496")
    tran0.writeAction("slorii X18 X18 8 65")
    tran0.writeAction("slorii X18 X18 12 1912")
    tran0.writeAction("slorii X18 X18 12 1049")
    tran0.writeAction("slorii X18 X18 8 74")
    tran0.writeAction("vmadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
