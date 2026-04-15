from EFA_v2 import *
def vsqrt_i32_15():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1523790227, 102905024, -183009268, -1544007491, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 98")
    tran0.writeAction("slorii X19 X19 12 564")
    tran0.writeAction("slorii X19 X19 8 192")
    tran0.writeAction("slorii X19 X19 12 1453")
    tran0.writeAction("slorii X19 X19 12 817")
    tran0.writeAction("slorii X19 X19 8 147")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2623")
    tran0.writeAction("slorii X18 X18 12 2128")
    tran0.writeAction("slorii X18 X18 8 189")
    tran0.writeAction("slorii X18 X18 12 3921")
    tran0.writeAction("slorii X18 X18 12 1920")
    tran0.writeAction("slorii X18 X18 8 12")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
