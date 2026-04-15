from EFA_v2 import *
def vgt_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2833661369, 1676697724, 2574653949, 3459099229, 959357017, 1432868059, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1599")
    tran0.writeAction("slorii X19 X19 12 96")
    tran0.writeAction("slorii X19 X19 8 124")
    tran0.writeAction("slorii X19 X19 12 2702")
    tran0.writeAction("slorii X19 X19 12 1597")
    tran0.writeAction("slorii X19 X19 8 185")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3298")
    tran0.writeAction("slorii X17 X17 12 3498")
    tran0.writeAction("slorii X17 X17 8 93")
    tran0.writeAction("slorii X17 X17 12 2455")
    tran0.writeAction("slorii X17 X17 12 1561")
    tran0.writeAction("slorii X17 X17 8 253")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1366")
    tran0.writeAction("slorii X18 X18 12 2004")
    tran0.writeAction("slorii X18 X18 8 219")
    tran0.writeAction("slorii X18 X18 12 914")
    tran0.writeAction("slorii X18 X18 12 3744")
    tran0.writeAction("slorii X18 X18 8 89")
    tran0.writeAction("vgt.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
