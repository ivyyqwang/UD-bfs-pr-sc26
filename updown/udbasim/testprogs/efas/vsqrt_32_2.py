from EFA_v2 import *
def vsqrt_32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1492191554, 723315109, 3199254025, 2576269236, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 689")
    tran0.writeAction("slorii X19 X19 12 3305")
    tran0.writeAction("slorii X19 X19 8 165")
    tran0.writeAction("slorii X19 X19 12 1423")
    tran0.writeAction("slorii X19 X19 12 265")
    tran0.writeAction("slorii X19 X19 8 66")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2456")
    tran0.writeAction("slorii X18 X18 12 3775")
    tran0.writeAction("slorii X18 X18 8 180")
    tran0.writeAction("slorii X18 X18 12 3051")
    tran0.writeAction("slorii X18 X18 12 190")
    tran0.writeAction("slorii X18 X18 8 9")
    tran0.writeAction("vsqrt.32 X19 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
