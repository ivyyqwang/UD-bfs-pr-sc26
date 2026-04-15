from EFA_v2 import *
def vfill_i32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1218964448, -2019049081, -727]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2170")
    tran0.writeAction("slorii X18 X18 12 1985")
    tran0.writeAction("slorii X18 X18 8 135")
    tran0.writeAction("slorii X18 X18 12 1162")
    tran0.writeAction("slorii X18 X18 12 2027")
    tran0.writeAction("slorii X18 X18 8 224")
    tran0.writeAction("vfill.i32 X18 -727 ")
    tran0.writeAction("yieldt")
    return efa
