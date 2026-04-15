from EFA_v2 import *
def vdiv_32_8():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [783381830, 1773054238, 3852486233, 2629552378, 2339807977, 1065930272, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1690")
    tran0.writeAction("slorii X19 X19 12 3753")
    tran0.writeAction("slorii X19 X19 8 30")
    tran0.writeAction("slorii X19 X19 12 747")
    tran0.writeAction("slorii X19 X19 12 373")
    tran0.writeAction("slorii X19 X19 8 70")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2507")
    tran0.writeAction("slorii X17 X17 12 3016")
    tran0.writeAction("slorii X17 X17 8 250")
    tran0.writeAction("slorii X17 X17 12 3674")
    tran0.writeAction("slorii X17 X17 12 70")
    tran0.writeAction("slorii X17 X17 8 89")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1016")
    tran0.writeAction("slorii X18 X18 12 2254")
    tran0.writeAction("slorii X18 X18 8 32")
    tran0.writeAction("slorii X18 X18 12 2231")
    tran0.writeAction("slorii X18 X18 12 1698")
    tran0.writeAction("slorii X18 X18 8 233")
    tran0.writeAction("vdiv.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
