from EFA_v2 import *
def vfill_b16_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [20019, 63187, 14254, 59832, '68.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3739")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 890")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 3949")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1251")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("vfill.b16 X18 68.75 ")
    tran0.writeAction("yieldt")
    return efa
