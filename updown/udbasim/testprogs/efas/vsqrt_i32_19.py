from EFA_v2 import *
def vsqrt_i32_19():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [159425229, -330976832, -1476829328, 1000639326, 0]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 3780")
    tran0.writeAction("slorii X19 X19 12 1457")
    tran0.writeAction("slorii X19 X19 8 192")
    tran0.writeAction("slorii X19 X19 12 152")
    tran0.writeAction("slorii X19 X19 12 162")
    tran0.writeAction("slorii X19 X19 8 205")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 954")
    tran0.writeAction("slorii X18 X18 12 1163")
    tran0.writeAction("slorii X18 X18 8 94")
    tran0.writeAction("slorii X18 X18 12 2687")
    tran0.writeAction("slorii X18 X18 12 2399")
    tran0.writeAction("slorii X18 X18 8 112")
    tran0.writeAction("vsqrt.i32 X19 X18 0 ")
    tran0.writeAction("yieldt")
    return efa
