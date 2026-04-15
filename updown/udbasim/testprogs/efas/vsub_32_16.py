from EFA_v2 import *
def vsub_32_16():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3984224456, 4073604152, 4102693792, 2432752659, 1468076008, 814482517, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3884")
    tran0.writeAction("slorii X19 X19 12 3652")
    tran0.writeAction("slorii X19 X19 8 56")
    tran0.writeAction("slorii X19 X19 12 3799")
    tran0.writeAction("slorii X19 X19 12 2672")
    tran0.writeAction("slorii X19 X19 8 200")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2320")
    tran0.writeAction("slorii X17 X17 12 220")
    tran0.writeAction("slorii X17 X17 8 19")
    tran0.writeAction("slorii X17 X17 12 3912")
    tran0.writeAction("slorii X17 X17 12 2595")
    tran0.writeAction("slorii X17 X17 8 160")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 776")
    tran0.writeAction("slorii X18 X18 12 3076")
    tran0.writeAction("slorii X18 X18 8 85")
    tran0.writeAction("slorii X18 X18 12 1400")
    tran0.writeAction("slorii X18 X18 12 271")
    tran0.writeAction("slorii X18 X18 8 232")
    tran0.writeAction("vsub.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
