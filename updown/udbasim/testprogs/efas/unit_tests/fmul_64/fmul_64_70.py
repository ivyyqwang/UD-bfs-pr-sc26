from EFA_v2 import *
def fmul_64_70():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [4144397511539305426, 14610037417371485017]
    tran0.writeAction("movir X16 14723")
    tran0.writeAction("slorii X16 X16 12 3513")
    tran0.writeAction("slorii X16 X16 12 1067")
    tran0.writeAction("slorii X16 X16 12 1282")
    tran0.writeAction("slorii X16 X16 12 3026")
    tran0.writeAction("movir X17 51905")
    tran0.writeAction("slorii X17 X17 12 1145")
    tran0.writeAction("slorii X17 X17 12 4017")
    tran0.writeAction("slorii X17 X17 12 2428")
    tran0.writeAction("slorii X17 X17 12 857")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
