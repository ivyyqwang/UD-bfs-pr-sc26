from EFA_v2 import *
def vsub_i32_12():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-1642248355, 592952002, -1657221922, -1097327535, -950994735, -1476967088, 3]
    tran0.writeAction("movir X19 0")
    tran0.writeAction("slorii X19 X19 12 565")
    tran0.writeAction("slorii X19 X19 12 1978")
    tran0.writeAction("slorii X19 X19 8 194")
    tran0.writeAction("slorii X19 X19 12 2529")
    tran0.writeAction("slorii X19 X19 12 3399")
    tran0.writeAction("slorii X19 X19 8 93")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 3049")
    tran0.writeAction("slorii X17 X17 12 2076")
    tran0.writeAction("slorii X17 X17 8 81")
    tran0.writeAction("slorii X17 X17 12 2515")
    tran0.writeAction("slorii X17 X17 12 2252")
    tran0.writeAction("slorii X17 X17 8 222")
    tran0.writeAction("movir X18 0")
    tran0.writeAction("slorii X18 X18 12 2687")
    tran0.writeAction("slorii X18 X18 12 1861")
    tran0.writeAction("slorii X18 X18 8 80")
    tran0.writeAction("slorii X18 X18 12 3189")
    tran0.writeAction("slorii X18 X18 12 248")
    tran0.writeAction("slorii X18 X18 8 209")
    tran0.writeAction("vsub.i32 X19 X17 X18 3 ")
    tran0.writeAction("yieldt")
    return efa
