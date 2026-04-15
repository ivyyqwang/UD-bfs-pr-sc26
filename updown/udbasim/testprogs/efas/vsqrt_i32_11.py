from EFA_v2 import *
def vsqrt_i32_11():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1287885515, -1323089292, 1754285199, 1635051505, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2834")
    tran0.writeAction("slorii X19 X19 12 834")
    tran0.writeAction("slorii X19 X19 8 116")
    tran0.writeAction("slorii X19 X19 12 1228")
    tran0.writeAction("slorii X19 X19 12 914")
    tran0.writeAction("slorii X19 X19 8 203")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1559")
    tran0.writeAction("slorii X18 X18 12 1255")
    tran0.writeAction("slorii X18 X18 8 241")
    tran0.writeAction("slorii X18 X18 12 1673")
    tran0.writeAction("slorii X18 X18 12 68")
    tran0.writeAction("slorii X18 X18 8 143")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
