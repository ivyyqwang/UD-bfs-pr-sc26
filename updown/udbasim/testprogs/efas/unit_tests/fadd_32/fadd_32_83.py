from EFA_v2 import *
def fadd_32_83():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [779715140, 3046185626]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 46")
    tran0.writeAction("slorii X16 X16 12 1944")
    tran0.writeAction("slorii X16 X16 12 580")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 181")
    tran0.writeAction("slorii X17 X17 12 2321")
    tran0.writeAction("slorii X17 X17 12 2714")
    tran0.writeAction("fadd.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
