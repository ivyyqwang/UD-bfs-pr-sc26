from EFA_v2 import *
def vmul_b16_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [28641, 8248, 23822, 25316, 11314, 36878, 44816, 30782, 33627, 15059, 36584, 44787, 8]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1582")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 1488")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 515")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 1790")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1923")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 2801")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("slorii X17 X17 12 2304")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("slorii X17 X17 12 707")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2799")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2286")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("slorii X18 X18 12 941")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2101")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("vmul.b16 X19 X17 X18 8 ")
    tran0.writeAction("yieldt")
    return efa
