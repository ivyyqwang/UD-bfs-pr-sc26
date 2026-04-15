from EFA_v2 import *
def vgt_i32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1746462376, -1568260485, 1778384093, -724892996, 1905001337, 704530893, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2600")
    tran0.writeAction("slorii X19 X19 12 1598")
    tran0.writeAction("slorii X19 X19 8 123")
    tran0.writeAction("slorii X19 X19 12 2430")
    tran0.writeAction("slorii X19 X19 12 1817")
    tran0.writeAction("slorii X19 X19 8 88")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3404")
    tran0.writeAction("slorii X17 X17 12 2818")
    tran0.writeAction("slorii X17 X17 8 188")
    tran0.writeAction("slorii X17 X17 12 1695")
    tran0.writeAction("slorii X17 X17 12 4092")
    tran0.writeAction("slorii X17 X17 8 221")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 671")
    tran0.writeAction("slorii X18 X18 12 3657")
    tran0.writeAction("slorii X18 X18 8 205")
    tran0.writeAction("slorii X18 X18 12 1816")
    tran0.writeAction("slorii X18 X18 12 3075")
    tran0.writeAction("slorii X18 X18 8 121")
    tran0.writeAction("vgt.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
