from EFA_v2 import *
def vsqrt_i32_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [750100952, -174407916, -13744662, 21471197, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3929")
    tran0.writeAction("slorii X19 X19 12 2751")
    tran0.writeAction("slorii X19 X19 8 20")
    tran0.writeAction("slorii X19 X19 12 715")
    tran0.writeAction("slorii X19 X19 12 1441")
    tran0.writeAction("slorii X19 X19 8 216")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 20")
    tran0.writeAction("slorii X18 X18 12 1951")
    tran0.writeAction("slorii X18 X18 8 221")
    tran0.writeAction("slorii X18 X18 12 4082")
    tran0.writeAction("slorii X18 X18 12 3653")
    tran0.writeAction("slorii X18 X18 8 234")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
