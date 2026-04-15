from EFA_v2 import *
def vfill_i32_9():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1061982246, -2075238738, -1960]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2116")
    tran0.writeAction("slorii X18 X18 12 3678")
    tran0.writeAction("slorii X18 X18 8 174")
    tran0.writeAction("slorii X18 X18 12 3083")
    tran0.writeAction("slorii X18 X18 12 879")
    tran0.writeAction("slorii X18 X18 8 218")
    tran0.writeAction("vfill.i32 X18 -1960 ")
    tran0.writeAction("yieldt")
    return efa
