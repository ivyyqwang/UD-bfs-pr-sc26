from EFA_v2 import *
def vfill_i32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-307369843, 2024459468, -687]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1930")
    tran0.writeAction("slorii X18 X18 12 2764")
    tran0.writeAction("slorii X18 X18 8 204")
    tran0.writeAction("slorii X18 X18 12 3802")
    tran0.writeAction("slorii X18 X18 12 3560")
    tran0.writeAction("slorii X18 X18 8 141")
    tran0.writeAction("vfill.i32 X18 -687 ")
    tran0.writeAction("yieldt")
    return efa
