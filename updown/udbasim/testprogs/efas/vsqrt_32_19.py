from EFA_v2 import *
def vsqrt_32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [314763756, 3651766089, 192205367, 4229662657, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3482")
    tran0.writeAction("slorii X19 X19 12 2439")
    tran0.writeAction("slorii X19 X19 8 73")
    tran0.writeAction("slorii X19 X19 12 300")
    tran0.writeAction("slorii X19 X19 12 745")
    tran0.writeAction("slorii X19 X19 8 236")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 4033")
    tran0.writeAction("slorii X18 X18 12 2951")
    tran0.writeAction("slorii X18 X18 8 193")
    tran0.writeAction("slorii X18 X18 12 183")
    tran0.writeAction("slorii X18 X18 12 1234")
    tran0.writeAction("slorii X18 X18 8 55")
    tran0.writeAction("vsqrt.32 X19 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
