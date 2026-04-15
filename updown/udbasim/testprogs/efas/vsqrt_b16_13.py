from EFA_v2 import *
def vsqrt_b16_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [43004, 58021, 7170, 4680, 8170, 32238, 20800, 61989, 5]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 292")
    tran0.writeAction("slorii X19 X19 4 8")
    tran0.writeAction("slorii X19 X19 12 448")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("slorii X19 X19 12 3626")
    tran0.writeAction("slorii X19 X19 4 5")
    tran0.writeAction("slorii X19 X19 12 2687")
    tran0.writeAction("slorii X19 X19 4 12")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3874")
    tran0.writeAction("slorii X18 X18 4 5")
    tran0.writeAction("slorii X18 X18 12 1300")
    tran0.writeAction("slorii X18 X18 4 0")
    tran0.writeAction("slorii X18 X18 12 2014")
    tran0.writeAction("slorii X18 X18 4 14")
    tran0.writeAction("slorii X18 X18 12 510")
    tran0.writeAction("slorii X18 X18 4 10")
    tran0.writeAction("vsqrt.b16 X19 X18 5 ")
    tran0.writeAction("yieldt")
    return efa
