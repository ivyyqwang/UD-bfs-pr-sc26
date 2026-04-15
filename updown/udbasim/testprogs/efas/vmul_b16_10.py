from EFA_v2 import *
def vmul_b16_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [20487, 40568, 64521, 14741, 22685, 22217, 61386, 47919, 56317, 12497, 46233, 2771, 5]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 921")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 4032")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 2535")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 1280")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2994")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("slorii X17 X17 12 3836")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 1388")
    tran0.writeAction("slorii X17 X17 4 9")
    tran0.writeAction("slorii X17 X17 12 1417")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 173")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2889")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 781")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 3519")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vmul.b16 X19 X17 X18 5 ")
    tran0.writeAction("yieldt")
    return efa
