from EFA_v2 import *
def fadd_32_56():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3797192871, 966879266]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 226")
    tran0.writeAction("slorii X16 X16 12 1353")
    tran0.writeAction("slorii X16 X16 12 167")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 57")
    tran0.writeAction("slorii X17 X17 12 2582")
    tran0.writeAction("slorii X17 X17 12 2082")
    tran0.writeAction("fadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
