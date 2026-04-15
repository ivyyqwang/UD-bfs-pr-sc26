from EFA_v2 import *
def vadd_32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3619996333, 1270525934, 3196971008, 2336024889, 966255425, 2262506615, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1211")
    tran0.writeAction("slorii X19 X19 12 2735")
    tran0.writeAction("slorii X19 X19 8 238")
    tran0.writeAction("slorii X19 X19 12 3452")
    tran0.writeAction("slorii X19 X19 12 1218")
    tran0.writeAction("slorii X19 X19 8 173")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2227")
    tran0.writeAction("slorii X17 X17 12 3305")
    tran0.writeAction("slorii X17 X17 8 57")
    tran0.writeAction("slorii X17 X17 12 3048")
    tran0.writeAction("slorii X17 X17 12 3560")
    tran0.writeAction("slorii X17 X17 8 0")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2157")
    tran0.writeAction("slorii X18 X18 12 2844")
    tran0.writeAction("slorii X18 X18 8 119")
    tran0.writeAction("slorii X18 X18 12 921")
    tran0.writeAction("slorii X18 X18 12 2019")
    tran0.writeAction("slorii X18 X18 8 65")
    tran0.writeAction("vadd.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
