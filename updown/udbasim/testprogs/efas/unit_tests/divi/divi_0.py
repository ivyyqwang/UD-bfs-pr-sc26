from EFA_v2 import *
def divi_0():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [7594666696913258206, 15119]
    tran0.writeAction("movir X16 26981")
    tran0.writeAction("slorii X16 X16 12 2769")
    tran0.writeAction("slorii X16 X16 12 3937")
    tran0.writeAction("slorii X16 X16 12 16")
    tran0.writeAction("slorii X16 X16 12 1758")
    tran0.writeAction("divi X16 X17 15119")
    tran0.writeAction("yieldt")
    return efa
