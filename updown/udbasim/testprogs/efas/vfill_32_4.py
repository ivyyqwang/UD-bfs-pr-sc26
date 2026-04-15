from EFA_v2 import *
def vfill_32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1480452789, 2733514078, '3.0']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2606")
    tran0.writeAction("slorii X18 X18 12 3613")
    tran0.writeAction("slorii X18 X18 8 94")
    tran0.writeAction("slorii X18 X18 12 1411")
    tran0.writeAction("slorii X18 X18 12 3562")
    tran0.writeAction("slorii X18 X18 8 181")
    tran0.writeAction("vfill.32 X18 3.0 ")
    tran0.writeAction("yieldt")
    return efa
