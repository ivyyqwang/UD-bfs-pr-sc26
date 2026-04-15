from EFA_v2 import *
def vsub_b16_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [24566, 51743, 45675, 50705, 26500, 29650, 51222, 60381, 30137, 56541, 59972, 61754, 12]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3169")
    tran0.writeAction("slorii X19 X19 4 1")
    tran0.writeAction("slorii X19 X19 12 2854")
    tran0.writeAction("slorii X19 X19 4 11")
    tran0.writeAction("slorii X19 X19 12 3233")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 1535")
    tran0.writeAction("slorii X19 X19 4 6")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3773")
    tran0.writeAction("slorii X17 X17 4 13")
    tran0.writeAction("slorii X17 X17 12 3201")
    tran0.writeAction("slorii X17 X17 4 6")
    tran0.writeAction("slorii X17 X17 12 1853")
    tran0.writeAction("slorii X17 X17 4 2")
    tran0.writeAction("slorii X17 X17 12 1656")
    tran0.writeAction("slorii X17 X17 4 4")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3859")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 3748")
    tran0.writeAction("slorii X18 X18 4 4")
    tran0.writeAction("slorii X18 X18 12 3533")
    tran0.writeAction("slorii X18 X18 4 13")
    tran0.writeAction("slorii X18 X18 12 1883")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("vsub.b16 X19 X17 X18 12 ")
    tran0.writeAction("yieldt")
    return efa
