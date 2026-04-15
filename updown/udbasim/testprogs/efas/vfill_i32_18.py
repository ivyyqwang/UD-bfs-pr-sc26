from EFA_v2 import *
def vfill_i32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1552877849, -174957186, -1357]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3929")
    tran0.writeAction("slorii X18 X18 12 605")
    tran0.writeAction("slorii X18 X18 8 126")
    tran0.writeAction("slorii X18 X18 12 2615")
    tran0.writeAction("slorii X18 X18 12 246")
    tran0.writeAction("slorii X18 X18 8 231")
    tran0.writeAction("vfill.i32 X18 -1357 ")
    tran0.writeAction("yieldt")
    return efa
