from EFA_v2 import *
def vsub_i32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [2118637555, 117451525, 1956648545, -790878909, 1325223, -970141282, 1]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 112")
    tran0.writeAction("slorii X19 X19 12 43")
    tran0.writeAction("slorii X19 X19 8 5")
    tran0.writeAction("slorii X19 X19 12 2020")
    tran0.writeAction("slorii X19 X19 12 2007")
    tran0.writeAction("slorii X19 X19 8 243")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3341")
    tran0.writeAction("slorii X17 X17 12 3109")
    tran0.writeAction("slorii X17 X17 8 67")
    tran0.writeAction("slorii X17 X17 12 1866")
    tran0.writeAction("slorii X17 X17 12 22")
    tran0.writeAction("slorii X17 X17 8 97")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3170")
    tran0.writeAction("slorii X18 X18 12 3281")
    tran0.writeAction("slorii X18 X18 8 158")
    tran0.writeAction("slorii X18 X18 12 1")
    tran0.writeAction("slorii X18 X18 12 1080")
    tran0.writeAction("slorii X18 X18 8 167")
    tran0.writeAction("vsub.i32 X19 X17 X18 1 ")
    tran0.writeAction("yieldt")
    return efa
