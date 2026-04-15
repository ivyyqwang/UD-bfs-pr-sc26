from EFA_v2 import *
def vdiv_i32_7():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-185038309, -1023585402, -2068736015, -1802578135, 1861091143, 1164830930, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3119")
    tran0.writeAction("slorii X19 X19 12 3411")
    tran0.writeAction("slorii X19 X19 8 134")
    tran0.writeAction("slorii X19 X19 12 3919")
    tran0.writeAction("slorii X19 X19 12 2186")
    tran0.writeAction("slorii X19 X19 8 27")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 2376")
    tran0.writeAction("slorii X17 X17 12 3799")
    tran0.writeAction("slorii X17 X17 8 41")
    tran0.writeAction("slorii X17 X17 12 2123")
    tran0.writeAction("slorii X17 X17 12 407")
    tran0.writeAction("slorii X17 X17 8 241")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1110")
    tran0.writeAction("slorii X18 X18 12 3560")
    tran0.writeAction("slorii X18 X18 8 210")
    tran0.writeAction("slorii X18 X18 12 1774")
    tran0.writeAction("slorii X18 X18 12 3583")
    tran0.writeAction("slorii X18 X18 8 71")
    tran0.writeAction("vdiv.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
