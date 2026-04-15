from EFA_v2 import *
def vsqrt_32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3180734638, 588318253, 3300555358, 1724169801, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 561")
    tran0.writeAction("slorii X19 X19 12 262")
    tran0.writeAction("slorii X19 X19 8 45")
    tran0.writeAction("slorii X19 X19 12 3033")
    tran0.writeAction("slorii X19 X19 12 1576")
    tran0.writeAction("slorii X19 X19 8 174")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 1644")
    tran0.writeAction("slorii X18 X18 12 1214")
    tran0.writeAction("slorii X18 X18 8 73")
    tran0.writeAction("slorii X18 X18 12 3147")
    tran0.writeAction("slorii X18 X18 12 2682")
    tran0.writeAction("slorii X18 X18 8 94")
    tran0.writeAction("vsqrt.32 X19 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
