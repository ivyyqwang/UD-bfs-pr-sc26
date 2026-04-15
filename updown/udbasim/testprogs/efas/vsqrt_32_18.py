from EFA_v2 import *
def vsqrt_32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1881301845, 2258184292, 3384300390, 1137667509, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2153")
    tran0.writeAction("slorii X19 X19 12 2344")
    tran0.writeAction("slorii X19 X19 8 100")
    tran0.writeAction("slorii X19 X19 12 1794")
    tran0.writeAction("slorii X19 X19 12 611")
    tran0.writeAction("slorii X19 X19 8 85")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1084")
    tran0.writeAction("slorii X18 X18 12 3949")
    tran0.writeAction("slorii X18 X18 8 181")
    tran0.writeAction("slorii X18 X18 12 3227")
    tran0.writeAction("slorii X18 X18 12 2131")
    tran0.writeAction("slorii X18 X18 8 102")
    tran0.writeAction("vsqrt.32 X19 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
