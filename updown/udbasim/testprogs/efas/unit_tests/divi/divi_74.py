from EFA_v2 import *
def divi_74():
    efa = EFA([])
    efa.code_level = "machine"
    state = State()
    efa.add_initId(state.state_id)
    efa.add_state(state)
    event_map = {
        "launch_events": 0,
    }
    tran0 = state.writeTransition("eventCarry", state, state, event_map['launch_events'])
# Input arguments: [-3894883687442611748, -11770]
    tran0.writeAction("movir X16 51698")
    tran0.writeAction("slorii X16 X16 12 2430")
    tran0.writeAction("slorii X16 X16 12 3096")
    tran0.writeAction("slorii X16 X16 12 2128")
    tran0.writeAction("slorii X16 X16 12 476")
    tran0.writeAction("divi X16 X17 -11770")
    tran0.writeAction("yieldt")
    return efa
