from EFA_v2 import *
def vsqrt_i32_4():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1400435668, -736074480, -1737078624, -1506929829, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3394")
    tran0.writeAction("slorii X19 X19 12 101")
    tran0.writeAction("slorii X19 X19 8 16")
    tran0.writeAction("slorii X19 X19 12 1335")
    tran0.writeAction("slorii X19 X19 12 2291")
    tran0.writeAction("slorii X19 X19 8 212")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2658")
    tran0.writeAction("slorii X18 X18 12 3603")
    tran0.writeAction("slorii X18 X18 8 91")
    tran0.writeAction("slorii X18 X18 12 2439")
    tran0.writeAction("slorii X18 X18 12 1608")
    tran0.writeAction("slorii X18 X18 8 160")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
