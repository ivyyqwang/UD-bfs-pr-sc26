from EFA_v2 import *
def vsub_b16_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [56982, 49482, 49329, 957, 47973, 58723, 27445, 36034, 24246, 43594, 19168, 44553, 13]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 59")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 3083")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 3092")
    tran0.writeAction("slorii X19 X19 4 10")
    tran0.writeAction("slorii X19 X19 12 3561")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2252")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 1715")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("slorii X17 X17 12 3670")
    tran0.writeAction("slorii X17 X17 4 3")
    tran0.writeAction("slorii X17 X17 12 2998")
    tran0.writeAction("slorii X17 X17 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2784")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1198")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2724")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 1515")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vsub.b16 X19 X17 X18 13 ")
    tran0.writeAction("yieldt")
    return efa
