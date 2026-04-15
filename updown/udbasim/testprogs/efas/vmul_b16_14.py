from EFA_v2 import *
def vmul_b16_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [39512, 53205, 38737, 36580, 32558, 5802, 31357, 3981, 59149, 300, 59054, 15817, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2286")
    tran0.writeAction("slorii X19 X19 4 4")
    tran0.writeAction("slorii X19 X19 12 2421")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 3325")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 2469")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 248")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 1959")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 362")
    tran0.writeAction("slorii X17 X17 4 10")
    tran0.writeAction("slorii X17 X17 12 2034")
    tran0.writeAction("slorii X17 X17 4 14")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 988")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 3690")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 18")
    tran0.writeAction("slorii X18 X18 4 12")
    tran0.writeAction("slorii X18 X18 12 3696")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("vmul.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
