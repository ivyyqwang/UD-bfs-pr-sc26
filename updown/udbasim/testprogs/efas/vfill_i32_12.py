from EFA_v2 import *
def vfill_i32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1521229622, 63305923, 985]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 60")
    tran0.writeAction("slorii X18 X18 12 1528")
    tran0.writeAction("slorii X18 X18 8 195")
    tran0.writeAction("slorii X18 X18 12 1450")
    tran0.writeAction("slorii X18 X18 12 3103")
    tran0.writeAction("slorii X18 X18 8 54")
    tran0.writeAction("vfill.i32 X18 985 ")
    tran0.writeAction("yieldt")
    return efa
