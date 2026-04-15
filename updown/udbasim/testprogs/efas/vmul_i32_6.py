from EFA_v2 import *
def vmul_i32_6():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1809029970, -2050110044, -381952851, 1011499815, 1469350876, 672808504, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2140")
    tran0.writeAction("slorii X19 X19 12 3533")
    tran0.writeAction("slorii X19 X19 8 164")
    tran0.writeAction("slorii X19 X19 12 1725")
    tran0.writeAction("slorii X19 X19 12 923")
    tran0.writeAction("slorii X19 X19 8 82")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 964")
    tran0.writeAction("slorii X17 X17 12 2627")
    tran0.writeAction("slorii X17 X17 8 39")
    tran0.writeAction("slorii X17 X17 12 3731")
    tran0.writeAction("slorii X17 X17 12 3036")
    tran0.writeAction("slorii X17 X17 8 173")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 641")
    tran0.writeAction("slorii X18 X18 12 2622")
    tran0.writeAction("slorii X18 X18 8 56")
    tran0.writeAction("slorii X18 X18 12 1401")
    tran0.writeAction("slorii X18 X18 12 1155")
    tran0.writeAction("slorii X18 X18 8 220")
    tran0.writeAction("vmul.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
