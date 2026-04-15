from EFA_v2 import *
def vmul_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [1564146202, 3069319649, 4219862656, 438782153, 358243747, 2910355459, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 2927")
    tran0.writeAction("slorii X19 X19 12 537")
    tran0.writeAction("slorii X19 X19 8 225")
    tran0.writeAction("slorii X19 X19 12 1491")
    tran0.writeAction("slorii X19 X19 12 2810")
    tran0.writeAction("slorii X19 X19 8 26")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 418")
    tran0.writeAction("slorii X17 X17 12 1864")
    tran0.writeAction("slorii X17 X17 8 201")
    tran0.writeAction("slorii X17 X17 12 4024")
    tran0.writeAction("slorii X17 X17 12 1534")
    tran0.writeAction("slorii X17 X17 8 128")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2775")
    tran0.writeAction("slorii X18 X18 12 2176")
    tran0.writeAction("slorii X18 X18 8 3")
    tran0.writeAction("slorii X18 X18 12 341")
    tran0.writeAction("slorii X18 X18 12 2653")
    tran0.writeAction("slorii X18 X18 8 163")
    tran0.writeAction("vmul.32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
