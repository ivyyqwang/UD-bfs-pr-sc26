from EFA_v2 import *
def fdiv_64_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [8779516193255066297, 9979122665394974138]
    tran0.writeAction("movir X16 31191")
    tran0.writeAction("slorii X16 X16 12 439")
    tran0.writeAction("slorii X16 X16 12 1598")
    tran0.writeAction("slorii X16 X16 12 3104")
    tran0.writeAction("slorii X16 X16 12 2745")
    tran0.writeAction("movir X17 35452")
    tran0.writeAction("slorii X17 X17 12 3955")
    tran0.writeAction("slorii X17 X17 12 328")
    tran0.writeAction("slorii X17 X17 12 3754")
    tran0.writeAction("slorii X17 X17 12 3514")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
