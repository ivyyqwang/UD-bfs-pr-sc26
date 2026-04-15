from EFA_v2 import *
def vsqrt_b16_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [28725, 61655, 46610, 53247, 44192, 55226, 24385, 11105, 7]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3327")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 2913")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 3853")
    tran0.writeAction("slorii X19 X19 4 7")
    tran0.writeAction("slorii X19 X19 12 1795")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 694")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 1524")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 3451")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("slorii X18 X18 12 2762")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("vsqrt.b16 X19 X18 7 ")
    tran0.writeAction("yieldt")
    return efa
