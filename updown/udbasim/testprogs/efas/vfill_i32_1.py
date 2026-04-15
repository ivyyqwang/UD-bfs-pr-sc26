from EFA_v2 import *
def vfill_i32_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1509315179, 1132073964, 1577]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1079")
    tran0.writeAction("slorii X18 X18 12 2579")
    tran0.writeAction("slorii X18 X18 8 236")
    tran0.writeAction("slorii X18 X18 12 2656")
    tran0.writeAction("slorii X18 X18 12 2477")
    tran0.writeAction("slorii X18 X18 8 149")
    tran0.writeAction("vfill.i32 X18 1577 ")
    tran0.writeAction("yieldt")
    return efa
