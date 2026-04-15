from EFA_v2 import *
def vfill_32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2319071057, 2776159665, '8.625']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2647")
    tran0.writeAction("slorii X18 X18 12 2261")
    tran0.writeAction("slorii X18 X18 8 177")
    tran0.writeAction("slorii X18 X18 12 2211")
    tran0.writeAction("slorii X18 X18 12 2615")
    tran0.writeAction("slorii X18 X18 8 81")
    tran0.writeAction("vfill.32 X18 8.625 ")
    tran0.writeAction("yieldt")
    return efa
