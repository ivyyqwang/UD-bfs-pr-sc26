from EFA_v2 import *
def vdiv_i32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-415291916, -604567384, -1653770309, 499308321, 2105397135, -1484392135, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3519")
    tran0.writeAction("slorii X19 X19 12 1800")
    tran0.writeAction("slorii X19 X19 8 168")
    tran0.writeAction("slorii X19 X19 12 3699")
    tran0.writeAction("slorii X19 X19 12 3877")
    tran0.writeAction("slorii X19 X19 8 244")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 476")
    tran0.writeAction("slorii X17 X17 12 727")
    tran0.writeAction("slorii X17 X17 8 33")
    tran0.writeAction("slorii X17 X17 12 2518")
    tran0.writeAction("slorii X17 X17 12 3447")
    tran0.writeAction("slorii X17 X17 8 187")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2680")
    tran0.writeAction("slorii X18 X18 12 1529")
    tran0.writeAction("slorii X18 X18 8 57")
    tran0.writeAction("slorii X18 X18 12 2007")
    tran0.writeAction("slorii X18 X18 12 3535")
    tran0.writeAction("slorii X18 X18 8 143")
    tran0.writeAction("vdiv.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
