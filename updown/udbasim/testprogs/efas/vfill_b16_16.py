from EFA_v2 import *
def vfill_b16_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [51573, 23052, 5178, 5711, '44.75']
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 356")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 323")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 1440")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 3223")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("vfill.b16 X18 44.75 ")
    tran0.writeAction("yieldt")
    return efa
