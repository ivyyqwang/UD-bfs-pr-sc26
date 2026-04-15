from EFA_v2 import *
def vdiv_i32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1526597635, 2038456788, -1130249232, -185078152, -1679640827, -1121247153, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 1944")
    tran0.writeAction("slorii X19 X19 12 97")
    tran0.writeAction("slorii X19 X19 8 212")
    tran0.writeAction("slorii X19 X19 12 2640")
    tran0.writeAction("slorii X19 X19 12 503")
    tran0.writeAction("slorii X19 X19 8 253")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3919")
    tran0.writeAction("slorii X17 X17 12 2030")
    tran0.writeAction("slorii X17 X17 8 120")
    tran0.writeAction("slorii X17 X17 12 3018")
    tran0.writeAction("slorii X17 X17 12 451")
    tran0.writeAction("slorii X17 X17 8 240")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3026")
    tran0.writeAction("slorii X18 X18 12 2848")
    tran0.writeAction("slorii X18 X18 8 79")
    tran0.writeAction("slorii X18 X18 12 2494")
    tran0.writeAction("slorii X18 X18 12 695")
    tran0.writeAction("slorii X18 X18 8 5")
    tran0.writeAction("vdiv.i32 X19 X17 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
