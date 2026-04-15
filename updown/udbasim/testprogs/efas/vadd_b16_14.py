from EFA_v2 import *
def vadd_b16_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [14157, 51155, 39870, 16138, 23615, 14616, 62139, 37890, 1735, 29103, 59254, 38211, 15]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1008")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 2491")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 3197")
    tran0.writeAction("slorii X19 X19 4 3")
    tran0.writeAction("slorii X19 X19 12 884")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2368")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 3883")
    tran0.writeAction("slorii X17 X17 4 11")
    tran0.writeAction("slorii X17 X17 12 913")
    tran0.writeAction("slorii X17 X17 4 8")
    tran0.writeAction("slorii X17 X17 12 1475")
    tran0.writeAction("slorii X17 X17 4 15")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2388")
    tran0.writeAction("slorii X18 X18 4 3")
    tran0.writeAction("slorii X18 X18 12 3703")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("slorii X18 X18 12 1818")
    tran0.writeAction("slorii X18 X18 4 15")
    tran0.writeAction("slorii X18 X18 12 108")
    tran0.writeAction("slorii X18 X18 4 7")
    tran0.writeAction("vadd.b16 X19 X17 X18 15 ")
    tran0.writeAction("yieldt")
    return efa
