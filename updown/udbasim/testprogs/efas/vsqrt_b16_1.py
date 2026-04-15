from EFA_v2 import *
def vsqrt_b16_1():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [36572, 58633, 7015, 30247, 41462, 23388, 37963, 30979, 14]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1890")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 438")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 3664")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 2285")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1936")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 2372")
    tran0.writeAction("slorii X18 X18 4 11")
    tran0.writeAction("slorii X18 X18 12 1461")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 2591")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vsqrt.b16 X19 X18 14 ")
    tran0.writeAction("yieldt")
    return efa
