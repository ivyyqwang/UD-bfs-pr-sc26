from EFA_v2 import *
def vsqrt_b16_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [26466, 42079, 20557, 59230, 22438, 41737, 42802, 44417, 9]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3701")
    tran0.writeAction("slorii X19 X19 4 14")
    tran0.writeAction("slorii X19 X19 12 1284")
    tran0.writeAction("slorii X19 X19 4 13")
    tran0.writeAction("slorii X19 X19 12 2629")
    tran0.writeAction("slorii X19 X19 4 15")
    tran0.writeAction("slorii X19 X19 12 1654")
    tran0.writeAction("slorii X19 X19 4 2")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2776")
    tran0.writeAction("slorii X18 X18 4 1")
    tran0.writeAction("slorii X18 X18 12 2675")
    tran0.writeAction("slorii X18 X18 4 2")
    tran0.writeAction("slorii X18 X18 12 2608")
    tran0.writeAction("slorii X18 X18 4 9")
    tran0.writeAction("slorii X18 X18 12 1402")
    tran0.writeAction("slorii X18 X18 4 6")
    tran0.writeAction("vsqrt.b16 X19 X18 9 ")
    tran0.writeAction("yieldt")
    return efa
