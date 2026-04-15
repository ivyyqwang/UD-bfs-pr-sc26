from EFA_v2 import *
def vfill_i32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [139290181, 1219095202, -207]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1162")
    tran0.writeAction("slorii X18 X18 12 2538")
    tran0.writeAction("slorii X18 X18 8 162")
    tran0.writeAction("slorii X18 X18 12 132")
    tran0.writeAction("slorii X18 X18 12 3430")
    tran0.writeAction("slorii X18 X18 8 69")
    tran0.writeAction("vfill.i32 X18 -207 ")
    tran0.writeAction("yieldt")
    return efa
