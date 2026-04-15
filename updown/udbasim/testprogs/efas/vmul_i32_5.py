from EFA_v2 import *
def vmul_i32_5():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2138387135, 136537751, -952002384, 454198895, -2051238291, 1172363423, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 130")
    tran0.writeAction("slorii X19 X19 12 870")
    tran0.writeAction("slorii X19 X19 8 151")
    tran0.writeAction("slorii X19 X19 12 2056")
    tran0.writeAction("slorii X19 X19 12 2765")
    tran0.writeAction("slorii X19 X19 8 65")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 433")
    tran0.writeAction("slorii X17 X17 12 646")
    tran0.writeAction("slorii X17 X17 8 111")
    tran0.writeAction("slorii X17 X17 12 3188")
    tran0.writeAction("slorii X17 X17 12 408")
    tran0.writeAction("slorii X17 X17 8 176")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1118")
    tran0.writeAction("slorii X18 X18 12 216")
    tran0.writeAction("slorii X18 X18 8 159")
    tran0.writeAction("slorii X18 X18 12 2139")
    tran0.writeAction("slorii X18 X18 12 3222")
    tran0.writeAction("slorii X18 X18 8 109")
    tran0.writeAction("vmul.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
