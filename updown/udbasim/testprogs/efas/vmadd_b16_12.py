from EFA_v2 import *
def vmadd_b16_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [28201, 61528, 61291, 39555, 61047, 47619, 24872, 43830, 20415, 46338, 60092, 26538, 6]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2472")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 3830")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3845")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 1762")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2739")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 1554")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 2976")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 3815")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1658")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3755")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2896")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 1275")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("vmadd.b16 X19 X17 X18 6 ")
    tran0.writeAction("yieldt")
    return efa
