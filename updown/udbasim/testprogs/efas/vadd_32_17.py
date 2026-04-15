from EFA_v2 import *
def vadd_32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1760645429, 1084203209, 721681131, 1517533862, 3196790358, 805381993, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1033")
    tran0.writeAction("slorii X19 X19 12 4000")
    tran0.writeAction("slorii X19 X19 8 201")
    tran0.writeAction("slorii X19 X19 12 1679")
    tran0.writeAction("slorii X19 X19 12 337")
    tran0.writeAction("slorii X19 X19 8 53")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1447")
    tran0.writeAction("slorii X17 X17 12 954")
    tran0.writeAction("slorii X17 X17 8 166")
    tran0.writeAction("slorii X17 X17 12 688")
    tran0.writeAction("slorii X17 X17 12 1018")
    tran0.writeAction("slorii X17 X17 8 235")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 768")
    tran0.writeAction("slorii X18 X18 12 295")
    tran0.writeAction("slorii X18 X18 8 105")
    tran0.writeAction("slorii X18 X18 12 3048")
    tran0.writeAction("slorii X18 X18 12 2854")
    tran0.writeAction("slorii X18 X18 8 86")
    tran0.writeAction("vadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
