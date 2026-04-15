from EFA_v2 import *
def vsqrt_32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1252587128, 2535797680, 483918297, 1022688530, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2418")
    tran0.writeAction("slorii X19 X19 12 1331")
    tran0.writeAction("slorii X19 X19 8 176")
    tran0.writeAction("slorii X19 X19 12 1194")
    tran0.writeAction("slorii X19 X19 12 2294")
    tran0.writeAction("slorii X19 X19 8 120")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 975")
    tran0.writeAction("slorii X18 X18 12 1277")
    tran0.writeAction("slorii X18 X18 8 18")
    tran0.writeAction("slorii X18 X18 12 461")
    tran0.writeAction("slorii X18 X18 12 2049")
    tran0.writeAction("slorii X18 X18 8 217")
    tran0.writeAction("vsqrt.32 X19 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
