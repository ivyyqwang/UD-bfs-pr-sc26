from EFA_v2 import *
def vsub_b16_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6037, 60153, 38229, 16038, 36974, 47586, 2219, 53776, 8272, 30539, 37867, 64604, 10]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1002")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 2389")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 3759")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 377")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3361")
    tran0.writeAction("slorii X17 X17 4 0")
    tran0.writeAction("slorii X17 X17 12 138")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 2974")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 2310")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4037")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2366")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 1908")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 517")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vsub.b16 X19 X17 X18 10 ")
    tran0.writeAction("yieldt")
    return efa
