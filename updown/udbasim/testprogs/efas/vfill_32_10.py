from EFA_v2 import *
def vfill_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4265289686, 1926011396, '9.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1836")
    tran0.writeAction("slorii X18 X18 12 3226")
    tran0.writeAction("slorii X18 X18 8 4")
    tran0.writeAction("slorii X18 X18 12 4067")
    tran0.writeAction("slorii X18 X18 12 2855")
    tran0.writeAction("slorii X18 X18 8 214")
    tran0.writeAction("vfill.32 X18 9.75 ")
    tran0.writeAction("yieldt")
    return efa
