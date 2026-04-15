from EFA_v2 import *
def vadd_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2461643391, 2841581995, 3929926711, 1996731730, 2927242734, 1835136245, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2709")
    tran0.writeAction("slorii X19 X19 12 3865")
    tran0.writeAction("slorii X19 X19 8 171")
    tran0.writeAction("slorii X19 X19 12 2347")
    tran0.writeAction("slorii X19 X19 12 2482")
    tran0.writeAction("slorii X19 X19 8 127")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 1904")
    tran0.writeAction("slorii X17 X17 12 949")
    tran0.writeAction("slorii X17 X17 8 82")
    tran0.writeAction("slorii X17 X17 12 3747")
    tran0.writeAction("slorii X17 X17 12 3564")
    tran0.writeAction("slorii X17 X17 8 55")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1750")
    tran0.writeAction("slorii X18 X18 12 500")
    tran0.writeAction("slorii X18 X18 8 245")
    tran0.writeAction("slorii X18 X18 12 2791")
    tran0.writeAction("slorii X18 X18 12 2605")
    tran0.writeAction("slorii X18 X18 8 238")
    tran0.writeAction("vadd.32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
