from EFA_v2 import *
def fmul_64_57():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [6489474849316494319, 3688152430091697948]
    tran0.writeAction("movir X16 23055")
    tran0.writeAction("slorii X16 X16 12 1007")
    tran0.writeAction("slorii X16 X16 12 3620")
    tran0.writeAction("slorii X16 X16 12 1397")
    tran0.writeAction("slorii X16 X16 12 3055")
    tran0.writeAction("movir X17 13102")
    tran0.writeAction("slorii X17 X17 12 3889")
    tran0.writeAction("slorii X17 X17 12 2097")
    tran0.writeAction("slorii X17 X17 12 447")
    tran0.writeAction("slorii X17 X17 12 3868")
    tran0.writeAction("fmul.64 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
