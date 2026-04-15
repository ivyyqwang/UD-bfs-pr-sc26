from EFA_v2 import *
def vmadd_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [358798176, 1132470714, 608792746, 1182527968, 2707563894, 1822391061, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1080")
    tran0.writeAction("slorii X19 X19 12 33")
    tran0.writeAction("slorii X19 X19 8 186")
    tran0.writeAction("slorii X19 X19 12 342")
    tran0.writeAction("slorii X19 X19 12 723")
    tran0.writeAction("slorii X19 X19 8 96")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1127")
    tran0.writeAction("slorii X17 X17 12 3057")
    tran0.writeAction("slorii X17 X17 8 224")
    tran0.writeAction("slorii X17 X17 12 580")
    tran0.writeAction("slorii X17 X17 12 2416")
    tran0.writeAction("slorii X17 X17 8 170")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1737")
    tran0.writeAction("slorii X18 X18 12 3963")
    tran0.writeAction("slorii X18 X18 8 21")
    tran0.writeAction("slorii X18 X18 12 2582")
    tran0.writeAction("slorii X18 X18 12 549")
    tran0.writeAction("slorii X18 X18 8 118")
    tran0.writeAction("vmadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
