from EFA_v2 import *
def vmul_i32_18():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-2091207491, -955246002, 1685123224, 877903036, 995323981, 586864360, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3185")
    tran0.writeAction("slorii X19 X19 12 26")
    tran0.writeAction("slorii X19 X19 8 78")
    tran0.writeAction("slorii X19 X19 12 2101")
    tran0.writeAction("slorii X19 X19 12 2740")
    tran0.writeAction("slorii X19 X19 8 189")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 837")
    tran0.writeAction("slorii X17 X17 12 956")
    tran0.writeAction("slorii X17 X17 8 188")
    tran0.writeAction("slorii X17 X17 12 1607")
    tran0.writeAction("slorii X17 X17 12 240")
    tran0.writeAction("slorii X17 X17 8 152")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 559")
    tran0.writeAction("slorii X18 X18 12 2774")
    tran0.writeAction("slorii X18 X18 8 232")
    tran0.writeAction("slorii X18 X18 12 949")
    tran0.writeAction("slorii X18 X18 12 880")
    tran0.writeAction("slorii X18 X18 8 77")
    tran0.writeAction("vmul.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
