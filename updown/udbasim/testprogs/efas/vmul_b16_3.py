from EFA_v2 import *
def vmul_b16_3():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [13041, 7562, 6430, 44240, 42975, 23401, 46103, 51068, 46168, 31529, 49351, 55900, 5]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2765")
    tran0.writeAction("slorii X19 X19 4 0")
    tran0.writeAction("slorii X19 X19 12 401")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 472")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 815")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3191")
    tran0.writeAction("slorii X17 X17 4 12")
    tran0.writeAction("slorii X17 X17 12 2881")
    tran0.writeAction("slorii X17 X17 4 7")
    tran0.writeAction("slorii X17 X17 12 1462")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 2685")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3493")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 3084")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("slorii X18 X18 12 1970")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 2885")
    tran0.writeAction("slorii X18 X18 4 8")
    tran0.writeAction("vmul.b16 X19 X17 X18 5 ")
    tran0.writeAction("yieldt")
    return efa
