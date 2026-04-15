from EFA_v2 import *
def vadd_i32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-346976475, -602964072, 558887297, -2063955286, -1474880581, 1845964750, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3520")
    tran0.writeAction("slorii X19 X19 12 3967")
    tran0.writeAction("slorii X19 X19 8 152")
    tran0.writeAction("slorii X19 X19 12 3765")
    tran0.writeAction("slorii X19 X19 12 399")
    tran0.writeAction("slorii X19 X19 8 37")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2127")
    tran0.writeAction("slorii X17 X17 12 2698")
    tran0.writeAction("slorii X17 X17 8 170")
    tran0.writeAction("slorii X17 X17 12 532")
    tran0.writeAction("slorii X17 X17 12 4081")
    tran0.writeAction("slorii X17 X17 8 129")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1760")
    tran0.writeAction("slorii X18 X18 12 1839")
    tran0.writeAction("slorii X18 X18 8 206")
    tran0.writeAction("slorii X18 X18 12 2689")
    tran0.writeAction("slorii X18 X18 12 1819")
    tran0.writeAction("slorii X18 X18 8 187")
    tran0.writeAction("vadd.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
