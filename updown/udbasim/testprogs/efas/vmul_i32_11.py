from EFA_v2 import *
def vmul_i32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-151067353, 1167752653, 1105826638, -1951613222, -626382598, -2053217204, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1113")
    tran0.writeAction("slorii X19 X19 12 2685")
    tran0.writeAction("slorii X19 X19 8 205")
    tran0.writeAction("slorii X19 X19 12 3951")
    tran0.writeAction("slorii X19 X19 12 3813")
    tran0.writeAction("slorii X19 X19 8 39")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2234")
    tran0.writeAction("slorii X17 X17 12 3262")
    tran0.writeAction("slorii X17 X17 8 218")
    tran0.writeAction("slorii X17 X17 12 1054")
    tran0.writeAction("slorii X17 X17 12 2451")
    tran0.writeAction("slorii X17 X17 8 78")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2137")
    tran0.writeAction("slorii X18 X18 12 3684")
    tran0.writeAction("slorii X18 X18 8 76")
    tran0.writeAction("slorii X18 X18 12 3498")
    tran0.writeAction("slorii X18 X18 12 2600")
    tran0.writeAction("slorii X18 X18 8 250")
    tran0.writeAction("vmul.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
