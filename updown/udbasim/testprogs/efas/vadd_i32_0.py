from EFA_v2 import *
def vadd_i32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [194123289, 1365078506, -1775005667, -1019096506, -1698845822, 1970645840, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1301")
    tran0.writeAction("slorii X19 X19 12 3441")
    tran0.writeAction("slorii X19 X19 8 234")
    tran0.writeAction("slorii X19 X19 12 185")
    tran0.writeAction("slorii X19 X19 12 534")
    tran0.writeAction("slorii X19 X19 8 25")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3124")
    tran0.writeAction("slorii X17 X17 12 466")
    tran0.writeAction("slorii X17 X17 8 70")
    tran0.writeAction("slorii X17 X17 12 2403")
    tran0.writeAction("slorii X17 X17 12 912")
    tran0.writeAction("slorii X17 X17 8 29")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1879")
    tran0.writeAction("slorii X18 X18 12 1451")
    tran0.writeAction("slorii X18 X18 8 80")
    tran0.writeAction("slorii X18 X18 12 2475")
    tran0.writeAction("slorii X18 X18 12 3499")
    tran0.writeAction("slorii X18 X18 8 130")
    tran0.writeAction("vadd.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
