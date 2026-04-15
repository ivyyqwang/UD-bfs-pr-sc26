from EFA_v2 import *
def fdiv_64_55():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3402821030263846846, 4994712499334277646]
    tran0.writeAction("movir X16 12089")
    tran0.writeAction("slorii X16 X16 12 1019")
    tran0.writeAction("slorii X16 X16 12 695")
    tran0.writeAction("slorii X16 X16 12 431")
    tran0.writeAction("slorii X16 X16 12 1982")
    tran0.writeAction("movir X17 17744")
    tran0.writeAction("slorii X17 X17 12 3208")
    tran0.writeAction("slorii X17 X17 12 3606")
    tran0.writeAction("slorii X17 X17 12 94")
    tran0.writeAction("slorii X17 X17 12 2574")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
