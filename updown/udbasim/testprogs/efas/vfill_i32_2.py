from EFA_v2 import *
def vfill_i32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [196051757, -2087863053, 1101]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2104")
    tran0.writeAction("slorii X18 X18 12 3516")
    tran0.writeAction("slorii X18 X18 8 243")
    tran0.writeAction("slorii X18 X18 12 186")
    tran0.writeAction("slorii X18 X18 12 3971")
    tran0.writeAction("slorii X18 X18 8 45")
    tran0.writeAction("vfill.i32 X18 1101 ")
    tran0.writeAction("yieldt")
    return efa
