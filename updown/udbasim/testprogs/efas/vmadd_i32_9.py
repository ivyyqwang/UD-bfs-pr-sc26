from EFA_v2 import *
def vmadd_i32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-565253194, -1028984853, -289649549, -1535953424, -984151595, -972799009, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3114")
    tran0.writeAction("slorii X19 X19 12 2799")
    tran0.writeAction("slorii X19 X19 8 235")
    tran0.writeAction("slorii X19 X19 12 3556")
    tran0.writeAction("slorii X19 X19 12 3819")
    tran0.writeAction("slorii X19 X19 8 182")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2631")
    tran0.writeAction("slorii X17 X17 12 821")
    tran0.writeAction("slorii X17 X17 8 240")
    tran0.writeAction("slorii X17 X17 12 3819")
    tran0.writeAction("slorii X17 X17 12 3148")
    tran0.writeAction("slorii X17 X17 8 115")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3168")
    tran0.writeAction("slorii X18 X18 12 1091")
    tran0.writeAction("slorii X18 X18 8 223")
    tran0.writeAction("slorii X18 X18 12 3157")
    tran0.writeAction("slorii X18 X18 12 1801")
    tran0.writeAction("slorii X18 X18 8 213")
    tran0.writeAction("vmadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
