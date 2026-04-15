from EFA_v2 import *
def vsqrt_32_10():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [324966748, 3803269180, 3721151973, 4060989032, 2]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3627")
    tran0.writeAction("slorii X19 X19 12 328")
    tran0.writeAction("slorii X19 X19 8 60")
    tran0.writeAction("slorii X19 X19 12 309")
    tran0.writeAction("slorii X19 X19 12 3737")
    tran0.writeAction("slorii X19 X19 8 92")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 3872")
    tran0.writeAction("slorii X18 X18 12 3526")
    tran0.writeAction("slorii X18 X18 8 104")
    tran0.writeAction("slorii X18 X18 12 3548")
    tran0.writeAction("slorii X18 X18 12 3141")
    tran0.writeAction("slorii X18 X18 8 229")
    tran0.writeAction("vsqrt.32 X19 X18 2 ")
    tran0.writeAction("yieldt")
    return efa
