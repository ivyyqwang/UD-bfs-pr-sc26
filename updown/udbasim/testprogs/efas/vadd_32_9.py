from EFA_v2 import *
def vadd_32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [717908945, 1060291615, 1052746834, 3630405484, 597804511, 981842293, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1011")
    tran0.writeAction("slorii X19 X19 12 708")
    tran0.writeAction("slorii X19 X19 8 31")
    tran0.writeAction("slorii X19 X19 12 684")
    tran0.writeAction("slorii X19 X19 12 2667")
    tran0.writeAction("slorii X19 X19 8 209")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3462")
    tran0.writeAction("slorii X17 X17 12 919")
    tran0.writeAction("slorii X17 X17 8 108")
    tran0.writeAction("slorii X17 X17 12 1003")
    tran0.writeAction("slorii X17 X17 12 4004")
    tran0.writeAction("slorii X17 X17 8 82")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 936")
    tran0.writeAction("slorii X18 X18 12 1465")
    tran0.writeAction("slorii X18 X18 8 117")
    tran0.writeAction("slorii X18 X18 12 570")
    tran0.writeAction("slorii X18 X18 12 453")
    tran0.writeAction("slorii X18 X18 8 223")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
