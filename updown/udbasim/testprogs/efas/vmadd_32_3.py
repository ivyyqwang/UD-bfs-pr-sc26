from EFA_v2 import *
def vmadd_32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1271891685, 2372418927, 1289819479, 3629512037, 2409284435, 115166526, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2262")
    tran0.writeAction("slorii X19 X19 12 2109")
    tran0.writeAction("slorii X19 X19 8 111")
    tran0.writeAction("slorii X19 X19 12 1212")
    tran0.writeAction("slorii X19 X19 12 3974")
    tran0.writeAction("slorii X19 X19 8 229")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3461")
    tran0.writeAction("slorii X17 X17 12 1525")
    tran0.writeAction("slorii X17 X17 8 101")
    tran0.writeAction("slorii X17 X17 12 1230")
    tran0.writeAction("slorii X17 X17 12 277")
    tran0.writeAction("slorii X17 X17 8 87")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 109")
    tran0.writeAction("slorii X18 X18 12 3405")
    tran0.writeAction("slorii X18 X18 8 62")
    tran0.writeAction("slorii X18 X18 12 2297")
    tran0.writeAction("slorii X18 X18 12 2755")
    tran0.writeAction("slorii X18 X18 8 83")
    tran0.writeAction("vmadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
