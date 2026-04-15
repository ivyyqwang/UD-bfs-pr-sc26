from EFA_v2 import *
def vmadd_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1810044799, 1955810408, 2541239624, 3280096293, 243277190, 3384536547, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1865")
    tran0.writeAction("slorii X19 X19 12 844")
    tran0.writeAction("slorii X19 X19 8 104")
    tran0.writeAction("slorii X19 X19 12 1726")
    tran0.writeAction("slorii X19 X19 12 791")
    tran0.writeAction("slorii X19 X19 8 127")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3128")
    tran0.writeAction("slorii X17 X17 12 588")
    tran0.writeAction("slorii X17 X17 8 37")
    tran0.writeAction("slorii X17 X17 12 2423")
    tran0.writeAction("slorii X17 X17 12 2109")
    tran0.writeAction("slorii X17 X17 8 72")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3227")
    tran0.writeAction("slorii X18 X18 12 3053")
    tran0.writeAction("slorii X18 X18 8 227")
    tran0.writeAction("slorii X18 X18 12 232")
    tran0.writeAction("slorii X18 X18 12 29")
    tran0.writeAction("slorii X18 X18 8 134")
    tran0.writeAction("vmadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
