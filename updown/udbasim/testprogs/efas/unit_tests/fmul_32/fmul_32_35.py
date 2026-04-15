from EFA_v2 import *
def fmul_32_35():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [3826938743, 1412356558]
    tran0.writeAction("movir X16 0")
    tran0.writeAction("slorii X16 X16 12 0")
    tran0.writeAction("slorii X16 X16 12 228")
    tran0.writeAction("slorii X16 X16 12 423")
    tran0.writeAction("slorii X16 X16 12 887")
    tran0.writeAction("movir X17 0")
    tran0.writeAction("slorii X17 X17 12 0")
    tran0.writeAction("slorii X17 X17 12 84")
    tran0.writeAction("slorii X17 X17 12 749")
    tran0.writeAction("slorii X17 X17 12 2510")
    tran0.writeAction("fmul.32 X16 X17 X18")
    tran0.writeAction("yieldt")
    return efa
