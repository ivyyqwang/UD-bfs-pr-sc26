from EFA_v2 import *
def vfill_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [744429472, 2421718708, '0.375']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2309")
    tran0.writeAction("slorii X18 X18 12 2174")
    tran0.writeAction("slorii X18 X18 8 180")
    tran0.writeAction("slorii X18 X18 12 709")
    tran0.writeAction("slorii X18 X18 12 3863")
    tran0.writeAction("slorii X18 X18 8 160")
    tran0.writeAction("vfill.32 X18 0.375 ")
    tran0.writeAction("yieldt")
    return efa
