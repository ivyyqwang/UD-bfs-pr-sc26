from EFA_v2 import *
def vmul_32_13():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2466760246, 3002824471, 1635762579, 506632573, 4116485581, 1227277225, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2863")
    tran0.writeAction("slorii X19 X19 12 2935")
    tran0.writeAction("slorii X19 X19 8 23")
    tran0.writeAction("slorii X19 X19 12 2352")
    tran0.writeAction("slorii X19 X19 12 1990")
    tran0.writeAction("slorii X19 X19 8 54")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 483")
    tran0.writeAction("slorii X17 X17 12 665")
    tran0.writeAction("slorii X17 X17 8 125")
    tran0.writeAction("slorii X17 X17 12 1559")
    tran0.writeAction("slorii X17 X17 12 4033")
    tran0.writeAction("slorii X17 X17 8 147")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1170")
    tran0.writeAction("slorii X18 X18 12 1731")
    tran0.writeAction("slorii X18 X18 8 169")
    tran0.writeAction("slorii X18 X18 12 3925")
    tran0.writeAction("slorii X18 X18 12 3221")
    tran0.writeAction("slorii X18 X18 8 205")
    tran0.writeAction("vmul.32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
