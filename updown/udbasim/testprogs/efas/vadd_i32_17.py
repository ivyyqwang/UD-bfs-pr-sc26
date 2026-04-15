from EFA_v2 import *
def vadd_i32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [393049499, -1130131693, -843316300, 1537094861, -992356409, 1722887695, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3018")
    tran0.writeAction("slorii X19 X19 12 911")
    tran0.writeAction("slorii X19 X19 8 19")
    tran0.writeAction("slorii X19 X19 12 374")
    tran0.writeAction("slorii X19 X19 12 3445")
    tran0.writeAction("slorii X19 X19 8 155")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1465")
    tran0.writeAction("slorii X17 X17 12 3636")
    tran0.writeAction("slorii X17 X17 8 205")
    tran0.writeAction("slorii X17 X17 12 3291")
    tran0.writeAction("slorii X17 X17 12 3075")
    tran0.writeAction("slorii X17 X17 8 180")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1643")
    tran0.writeAction("slorii X18 X18 12 302")
    tran0.writeAction("slorii X18 X18 8 15")
    tran0.writeAction("slorii X18 X18 12 3149")
    tran0.writeAction("slorii X18 X18 12 2519")
    tran0.writeAction("slorii X18 X18 8 199")
    tran0.writeAction("vadd.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
