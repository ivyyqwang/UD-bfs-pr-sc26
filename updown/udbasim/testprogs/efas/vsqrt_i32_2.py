from EFA_v2 import *
def vsqrt_i32_2():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1954165842, -933656055, -85496677, 318287606, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3205")
    tran0.writeAction("slorii X19 X19 12 2442")
    tran0.writeAction("slorii X19 X19 8 9")
    tran0.writeAction("slorii X19 X19 12 1863")
    tran0.writeAction("slorii X19 X19 12 2612")
    tran0.writeAction("slorii X19 X19 8 82")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 303")
    tran0.writeAction("slorii X18 X18 12 2222")
    tran0.writeAction("slorii X18 X18 8 246")
    tran0.writeAction("slorii X18 X18 12 4014")
    tran0.writeAction("slorii X18 X18 12 1900")
    tran0.writeAction("slorii X18 X18 8 155")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
