from EFA_v2 import *
def modi_23():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-7653869446726669571, -25510]
    tran0.writeAction("movir X16 38343")
    tran0.writeAction("slorii X16 X16 12 4068")
    tran0.writeAction("slorii X16 X16 12 2630")
    tran0.writeAction("slorii X16 X16 12 2626")
    tran0.writeAction("slorii X16 X16 12 2813")
    tran0.writeAction("modi X16 X17 -25510")
    tran0.writeAction("yieldt")
    return efa
