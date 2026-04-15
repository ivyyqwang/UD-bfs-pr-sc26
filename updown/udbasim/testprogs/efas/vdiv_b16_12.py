from EFA_v2 import *
def vdiv_b16_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [60543, 34969, 41399, 34870, 28085, 33125, 61061, 35722, 14557, 29914, 41939, 31722, 12]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2179")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("slorii X19 X19 12 2587")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 2185")
    tran0.writeAction("slorii X19 X19 4 9")
    tran0.writeAction("slorii X19 X19 12 3783")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2232")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 3816")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 2070")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 1755")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1982")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 2621")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 1869")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 909")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vdiv.b16 X19 X17 X18 12 ")
    tran0.writeAction("yieldt")
    return efa
