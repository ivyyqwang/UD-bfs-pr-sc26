from EFA_v2 import *
def vfill_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2674360802, 87086433, '16.875']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 83")
    tran0.writeAction("slorii X18 X18 12 213")
    tran0.writeAction("slorii X18 X18 8 97")
    tran0.writeAction("slorii X18 X18 12 2550")
    tran0.writeAction("slorii X18 X18 12 1921")
    tran0.writeAction("slorii X18 X18 8 226")
    tran0.writeAction("vfill.32 X18 16.875 ")
    tran0.writeAction("yieldt")
    return efa
