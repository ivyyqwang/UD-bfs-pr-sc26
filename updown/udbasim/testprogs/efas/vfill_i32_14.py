from EFA_v2 import *
def vfill_i32_14():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1669461610, 133278613, 1722]
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 127")
    tran0.writeAction("slorii X18 X18 12 427")
    tran0.writeAction("slorii X18 X18 8 149")
    tran0.writeAction("slorii X18 X18 12 2503")
    tran0.writeAction("slorii X18 X18 12 3593")
    tran0.writeAction("slorii X18 X18 8 150")
    tran0.writeAction("vfill.i32 X18 1722 ")
    tran0.writeAction("yieldt")
    return efa
