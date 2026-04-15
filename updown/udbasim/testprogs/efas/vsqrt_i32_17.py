from EFA_v2 import *
def vsqrt_i32_17():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-230352718, -1717860310, 1411894950, -1193791385, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2457")
    tran0.writeAction("slorii X19 X19 12 2952")
    tran0.writeAction("slorii X19 X19 8 42")
    tran0.writeAction("slorii X19 X19 12 3876")
    tran0.writeAction("slorii X19 X19 12 1304")
    tran0.writeAction("slorii X19 X19 8 178")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2957")
    tran0.writeAction("slorii X18 X18 12 2096")
    tran0.writeAction("slorii X18 X18 8 103")
    tran0.writeAction("slorii X18 X18 12 1346")
    tran0.writeAction("slorii X18 X18 12 1998")
    tran0.writeAction("slorii X18 X18 8 166")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
