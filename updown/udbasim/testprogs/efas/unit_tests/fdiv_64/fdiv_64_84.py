from EFA_v2 import *
def fdiv_64_84():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4771037574153314074, 3315596890258145166]
    tran0.writeAction("movir X16 16950")
    tran0.writeAction("slorii X16 X16 12 534")
    tran0.writeAction("slorii X16 X16 12 1353")
    tran0.writeAction("slorii X16 X16 12 1841")
    tran0.writeAction("slorii X16 X16 12 3866")
    tran0.writeAction("movir X17 11779")
    tran0.writeAction("slorii X17 X17 12 1500")
    tran0.writeAction("slorii X17 X17 12 3598")
    tran0.writeAction("slorii X17 X17 12 927")
    tran0.writeAction("slorii X17 X17 12 3982")
    tran0.writeAction("fdiv.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
