from EFA_v2 import *
def vsqrt_i32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-760585885, -1138348189, -1758684720, -1172776088, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3010")
    tran0.writeAction("slorii X19 X19 12 1583")
    tran0.writeAction("slorii X19 X19 8 99")
    tran0.writeAction("slorii X19 X19 12 3370")
    tran0.writeAction("slorii X19 X19 12 2657")
    tran0.writeAction("slorii X19 X19 8 99")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2977")
    tran0.writeAction("slorii X18 X18 12 2267")
    tran0.writeAction("slorii X18 X18 8 104")
    tran0.writeAction("slorii X18 X18 12 2418")
    tran0.writeAction("slorii X18 X18 12 3225")
    tran0.writeAction("slorii X18 X18 8 208")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
