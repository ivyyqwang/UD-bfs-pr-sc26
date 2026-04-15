from EFA_v2 import *
def vsqrt_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2561601336, 1462003584, 3988665194, 3591250572, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1394")
    tran0.writeAction("slorii X19 X19 12 1127")
    tran0.writeAction("slorii X19 X19 8 128")
    tran0.writeAction("slorii X19 X19 12 2442")
    tran0.writeAction("slorii X19 X19 12 3823")
    tran0.writeAction("slorii X19 X19 8 56")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3424")
    tran0.writeAction("slorii X18 X18 12 3618")
    tran0.writeAction("slorii X18 X18 8 140")
    tran0.writeAction("slorii X18 X18 12 3803")
    tran0.writeAction("slorii X18 X18 12 3635")
    tran0.writeAction("slorii X18 X18 8 106")
    tran0.writeAction("vsqrt.32 X19 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
