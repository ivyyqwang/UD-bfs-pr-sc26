from EFA_v2 import *
def vadd_i32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1658882183, -667678177, -610523344, -1387398302, 2125454447, 1932767472, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3459")
    tran0.writeAction("slorii X19 X19 12 1034")
    tran0.writeAction("slorii X19 X19 8 31")
    tran0.writeAction("slorii X19 X19 12 2513")
    tran0.writeAction("slorii X19 X19 12 3959")
    tran0.writeAction("slorii X19 X19 8 121")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2772")
    tran0.writeAction("slorii X17 X17 12 3579")
    tran0.writeAction("slorii X17 X17 8 98")
    tran0.writeAction("slorii X17 X17 12 3513")
    tran0.writeAction("slorii X17 X17 12 3111")
    tran0.writeAction("slorii X17 X17 8 48")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1843")
    tran0.writeAction("slorii X18 X18 12 944")
    tran0.writeAction("slorii X18 X18 8 240")
    tran0.writeAction("slorii X18 X18 12 2026")
    tran0.writeAction("slorii X18 X18 12 4060")
    tran0.writeAction("slorii X18 X18 8 111")
    tran0.writeAction("vadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
