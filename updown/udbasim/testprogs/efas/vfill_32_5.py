from EFA_v2 import *
def vfill_32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2257503075, 966675900, '3.625']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 921")
    tran0.writeAction("slorii X18 X18 12 3661")
    tran0.writeAction("slorii X18 X18 8 188")
    tran0.writeAction("slorii X18 X18 12 2152")
    tran0.writeAction("slorii X18 X18 12 3779")
    tran0.writeAction("slorii X18 X18 8 99")
    tran0.writeAction("vfill.32 X18 3.625 ")
    tran0.writeAction("yieldt")
    return efa
