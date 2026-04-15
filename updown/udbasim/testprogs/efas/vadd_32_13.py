from EFA_v2 import *
def vadd_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [374143278, 3163763753, 2747852512, 1386790542, 69427999, 990045910, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3017")
    tran0.writeAction("slorii X19 X19 12 820")
    tran0.writeAction("slorii X19 X19 8 41")
    tran0.writeAction("slorii X19 X19 12 356")
    tran0.writeAction("slorii X19 X19 12 3321")
    tran0.writeAction("slorii X19 X19 8 46")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1322")
    tran0.writeAction("slorii X17 X17 12 2238")
    tran0.writeAction("slorii X17 X17 8 142")
    tran0.writeAction("slorii X17 X17 12 2620")
    tran0.writeAction("slorii X17 X17 12 2278")
    tran0.writeAction("slorii X17 X17 8 224")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 944")
    tran0.writeAction("slorii X18 X18 12 742")
    tran0.writeAction("slorii X18 X18 8 214")
    tran0.writeAction("slorii X18 X18 12 66")
    tran0.writeAction("slorii X18 X18 12 867")
    tran0.writeAction("slorii X18 X18 8 31")
    tran0.writeAction("vadd.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
