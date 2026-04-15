from EFA_v2 import *
def vmul_32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3426398067, 869264013, 738174982, 1221948439, 3772200487, 208226718, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 828")
    tran0.writeAction("slorii X19 X19 12 4074")
    tran0.writeAction("slorii X19 X19 8 141")
    tran0.writeAction("slorii X19 X19 12 3267")
    tran0.writeAction("slorii X19 X19 12 2735")
    tran0.writeAction("slorii X19 X19 8 115")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1165")
    tran0.writeAction("slorii X17 X17 12 1396")
    tran0.writeAction("slorii X17 X17 8 23")
    tran0.writeAction("slorii X17 X17 12 703")
    tran0.writeAction("slorii X17 X17 12 4008")
    tran0.writeAction("slorii X17 X17 8 6")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 198")
    tran0.writeAction("slorii X18 X18 12 2377")
    tran0.writeAction("slorii X18 X18 8 158")
    tran0.writeAction("slorii X18 X18 12 3597")
    tran0.writeAction("slorii X18 X18 12 1846")
    tran0.writeAction("slorii X18 X18 8 39")
    tran0.writeAction("vmul.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
