from EFA_v2 import *
def vfill_i32_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-813996508, -558057522, -1227]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3563")
    tran0.writeAction("slorii X18 X18 12 3255")
    tran0.writeAction("slorii X18 X18 8 206")
    tran0.writeAction("slorii X18 X18 12 3319")
    tran0.writeAction("slorii X18 X18 12 2918")
    tran0.writeAction("slorii X18 X18 8 36")
    tran0.writeAction("vfill.i32 X18 -1227 ")
    tran0.writeAction("yieldt")
    return efa
