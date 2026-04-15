from EFA_v2 import *
def vfill_i32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-51551250, 13810005, 549]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 13")
    tran0.writeAction("slorii X18 X18 12 697")
    tran0.writeAction("slorii X18 X18 8 85")
    tran0.writeAction("slorii X18 X18 12 4046")
    tran0.writeAction("slorii X18 X18 12 3427")
    tran0.writeAction("slorii X18 X18 8 238")
    tran0.writeAction("vfill.i32 X18 549 ")
    tran0.writeAction("yieldt")
    return efa
